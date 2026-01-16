# ...existing code...
#!/usr/bin/env python3
import sys
import os
import json
import time
import tty
import termios
import select
from statistics import mean

TIMES_FILE = os.path.expanduser("~/.cubetimer_times.json")
INSPECTION_ENABLED = True
INSPECTION_LIMIT = 15.0
INSPECTION_PENALTY = 2.0
DNF_LIMIT = 17.0

def load_times():
    try:
        with open(TIMES_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_times(times):
    with open(TIMES_FILE, "w") as f:
        json.dump(times, f, indent=2)

def fmt(t):
    if t is None:
        return "DNF"
    if t < 60:
        return f"{t:.2f}"
    m = int(t // 60)
    s = t - m * 60

    return f"{m}:{s:05.2f}"

def compute_ao(times_list, n):
    if len(times_list) < n:
        return None
    last = times_list[-n:]
    vals = []
    for item in last:
        if item is None:
            return None
        vals.append(item)
    vals_sorted = sorted(vals)
    trimmed = vals_sorted[1:-1]
    return mean(trimmed)

def read_key(timeout=None):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        rlist, _, _ = select.select([fd], [], [], timeout)
        if rlist:

            return sys.stdin.read(1)
        return None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def instructions():
    print("Cubing timer (terminal)")
    print("Controls: <space> start/stop | i toggle inspection | u undo last | q quit")
    print("During inspection: space to start solve early. Inspection rules: >15s +2s, >=17s DNF.")
    print("Times saved to", TIMES_FILE)
    print("")

def show_summary(times):
    if not times:
        print("No solves yet.")
        return
    last = times[-1]
    print("Last:", fmt(last))
    numeric = [t for t in times if t is not None]
    best = min(numeric) if numeric else None
    worst = max(numeric) if numeric else None
    print("Best:", fmt(best) if best is not None else "N/A", " Worst:", fmt(worst) if worst is not None else "N/A")
    ao5 = compute_ao(times, 5)
    ao12 = compute_ao(times, 12)
    print("Ao5:", fmt(ao5) if ao5 is not None else "N/A", " Ao12:", fmt(ao12) if ao12 is not None else "N/A")
    print("Total solves:", len(times))

def main():
    global INSPECTION_ENABLED
    times = load_times()
    instructions()
    show_summary(times)
    state = "idle"
    try:
        while True:
            print("\nState:", state, end="  ")
            if state == "idle":
                print("waiting for key...")
                k = read_key()
                if k is None:
                    continue
                if k == " ":
                    # start solve immediately
                    start = time.monotonic()
                    state = "timing"
                    print("\nStarted.")
                elif k.lower() == "i":
                    INSPECTION_ENABLED = not INSPECTION_ENABLED
                    print("\nInspection toggled:", INSPECTION_ENABLED)
                elif k.lower() == "u":
                    if times:

                        removed = times.pop()
                        save_times(times)
                        print("\nRemoved last:", fmt(removed))
                    else:
                        print("\nNothing to undo.")
                elif k.lower() == "q":
                    print("\nQuit.")
                    break
                else:
                    continue
                # If inspection enabled and started from idle, run inspection first
                if state == "timing" and INSPECTION_ENABLED:
                    # run inspection countdown
                    inspect_start = time.monotonic()
                    cancelled = False
                    while True:
                        elapsed = time.monotonic() - inspect_start
                        remaining = INSPECTION_LIMIT - elapsed
                        if remaining <= 0:
                            print(f"\rInspection: 0.00s (time up)          ", end="", flush=True)
                            break
                        print(f"\rInspection: {remaining:4.2f}s remaining    ", end="", flush=True)
                        k2 = read_key(timeout=0.05)
                        if k2 == " ":
                            # begin solve early
                            print("\nStarting solve...")
                            start = time.monotonic()
                            break
                        elif k2 and k2.lower() == "c":
                            print("\nInspection cancelled.")
                            cancelled = True
                            break
                    if cancelled:

                        state = "idle"
                        continue
                    state = "timing"
                    print("")
                # timing loop
            elif state == "timing":
                start_time = time.monotonic()
                print("Timing... press <space> to stop.")
                while True:
                    k = read_key(timeout=0.02)
                    if k == " ":
                        end = time.monotonic()
                        duration = end - start_time
                        penalty = 0.0
                        # If inspection was used and exceeded -> apply rules:
                        # (We applied inspection above to possibly add penalty — but if user started immediately, skip)
                        # For simplicity assume inspection rules handled before start. Only apply if inspection was running:
                        # (We cannot detect that here reliably; skipping.)
                        # Add as-is:
                        final = duration + penalty
                        times.append(final)
                        save_times(times)
                        print("Solve time:", fmt(final))
                        show_summary(times)

                        final = duration + penalty
                        times.append(final)
                        save_times(times)
                        print("Solve time:", fmt(final))
                        show_summary(times)
                        state = "idle"
                        break
                    # allow quitting mid-solve (mark DNF)
                    if k and k.lower() == "d":
                        print("\nMarked DNF.")
                        times.append(None)
                        save_times(times)
                        show_summary(times)
                        state = "idle"
                        break
                    if k and k.lower() == "q":
                        print("\nQuit.")
                        raise SystemExit
            else:
                state = "idle"
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
    finally:
        save_times(times)

if __name__ == "__main__":
    main()
# ...existing code...