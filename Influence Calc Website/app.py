from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

numbers = []

@app.route('/')
def counter():
    return render_template("counter.html", numbers=numbers)

@app.route('/submit', methods=['POST'])
def submit():
    all_numbers = request.json.get('number')
    print(all_numbers)
    if all_numbers and all_numbers.strip():
        numbers.append({'numbers': all_numbers.strip(), 'done': False})
        return jsonify({'status': 'success', 'numbers': all_numbers})
    return jsonify({'status': 'error', 'message': 'invalid input'}), 400

if __name__ == "__main__":
	app.run(debug=True)
