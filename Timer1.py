import Timer
import sys
import tty
import termios
import select

def read_key(timeout=None):
    """Read a single key press from terminal"""
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

def display_menu():
    """Display the main menu with 2 button options"""
    print("\n" + "="*50)
    print("Welcome to our Rubik's cubing timer")
    print("This is where you will find your avg, worst time, best time and more!")
    print("="*50)
    print("\nSelect an option:")
    print("[1] Start Timer - Begin a new solve")
    print("[2] View Statistics - See your times and stats")
    print("[q] Quit - Exit the program")
    print("="*50)

def main():
    """Main menu loop with 2 button options"""
    while True:
        display_menu()
        print("\nPress [1] or [2] to select: ", end="", flush=True)
        key = read_key()
        
        if key is None:
            continue
        elif key == "1":
            print("\n[1] Starting Timer...")
            print("-" * 50)
            Timer.main()
        elif key == "2":
            print("\n[2] View Statistics...")
            print("-" * 50)
            times = Timer.load_times()
            Timer.show_summary(times)
        elif key.lower() == "q":
            print("\n[q] Quitting... Goodbye!")
            break
        else:
            print(f"\nInvalid option '{key}'. Please press [1], [2], or [q].")

if __name__ == "__main__":
    main()