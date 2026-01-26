
impot Flask
from flask import Flask, render_template, jsonify, request
import json
import os
import time
from statistics import mean

app = Flask(__name__)

TIMES_FILE = os.path.expanduser("~/.cubetimer_times.json")

# ============ TIMER FUNCTIONS ============
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

# ============ HOMEWORK DATA ============
homework_data = {
    "q1": {
        "question": "What do you understand by sequences?",
        "answer": "Sequences are containers with items that are accessible by indexing or slicing. The built-in len() function takes any container as an argument and returns the number of items in the container."
    },
    "q2": {
        "question": "Name all the types of sequences?",
        "answer": [
            "1. Lists",
            "2. Strings",
            "3. Dictionaries",
            "4. Tuples",
            "5. Sets"
        ]
    },
    "q3": {
        "question": "What is concatenation?",
        "answer": "Concatenation is when datatypes are connecting datatypes. For example: Strings concatenate with strings, Integers concatenate with Integers, Integers concatenate with Floats, Floats concatenate with Floats while booleans concatenate with nothing."
    },
    "q4": {
        "question": "What is repetition?",
        "answer": "Repetition is when you use the * operator to repeat a datatype. Example: String 1 * 2 = 11"
    },
    "q5": {
        "question": "What do you understand by Datatypes? Give examples",
        "answer": "Data types are classifications that determine what kind of data a variable can hold and what operations can be performed on it."
    },
    "q6": {
        "question": "Explain 'append' function with few examples",
        "answer": "Append is a function which can add an element to a list after the last one.",
        "example": "Fruits = ['Mango', 'Apple', 'Orange']\nFruits.append('Strawberry')\nResult: ['Mango', 'Apple', 'Orange', 'Strawberry']"
    },
    "q7": {
        "question": "What do you understand by 'List'? Give an example.",
        "answer": "List is the most versatile data type in Python. It can be written as a list of comma-separated values between square brackets. Items in a list need not be of the same datatype.",
        "example": "Sports = ['soccer', 'basketball', 'cricket']"
    },
    "q8": {
        "question": "What is 'remove()' in 'list'? Give an example.",
        "answer": "Remove removes the first occurrence of a specified value from the list."
    },
    "q9": {
        "question": "What is 'reverse()' in list? Give an example",
        "answer": "Reverse is a function which can reverse/flip-flop a list.",
        "example": "Fruits = ['Mango', 'Apple', 'Orange']\nFruits.reverse()\nResult: ['Orange', 'Apple', 'Mango']"
    },
}

# ============ ROUTES ============
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/timer')
def timer():
    times = load_times()
    return render_template('timer.html', times=times)

@app.route('/homework')
def homework():
    return render_template('homework.html', homework=homework_data)

@app.route('/homework/<q_id>')
def homework_question(q_id):
    if q_id in homework_data:
        return render_template('question.html', q_id=q_id, data=homework_data[q_id])
    return "Question not found", 404

# ============ TIMER API ============
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
        "times": [fmt(t) for t in times[-10:]]
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