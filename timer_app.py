from flask import Flask, render_template, jsonify, request
import json
import os
import time
from statistics import mean

app = Flask(__name__)

TIMES_FILE = os.path.expanduser("~/.cubetimer_times.json")

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

@app.route('/')
def index():
    times = load_times()
    return render_template('timer.html', times=times)

@app.route('/api/stats')
def get_stats():
    times = load_times()
    if not times:
        return jsonify({
            "last": None,
            "best": None,
            "worst": None,
            "ao5": None,
            "ao12": None,
            "total": 0,
            "times": []
        })
    
    numeric = [t for t in times if t is not None]
    best = min(numeric) if numeric else None
    worst = max(numeric) if numeric else None
    ao5 = compute_ao(times, 5)
    ao12 = compute_ao(times, 12)
    
    return jsonify({
        "last": fmt(times[-1]) if times else None,
        "best": fmt(best) if best is not None else None,
        "worst": fmt(worst) if worst is not None else None,
        "ao5": fmt(ao5) if ao5 is not None else None,
        "ao12": fmt(ao12) if ao12 is not None else None,
        "total": len(times),
        "times": [fmt(t) for t in times[-10:]]  # Last 10 times
    })

@app.route('/api/save-time', methods=['POST'])
def save_time():
    data = request.json
    time_value = data.get('time')
    
    times = load_times()
    times.append(time_value)
    save_times(times)
    
    return jsonify({"success": True, "message": "Time saved"})

@app.route('/api/undo', methods=['POST'])
def undo():
    times = load_times()
    if times:
        removed = times.pop()
        save_times(times)
        return jsonify({"success": True, "removed": fmt(removed)})
    return jsonify({"success": False, "message": "Nothing to undo"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
