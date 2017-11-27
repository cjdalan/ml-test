from flask import Flask, jsonify, render_template, request
from playhouse.shortcuts import model_to_dict

from database import close_db, initialize_db, Record
from plot import get_result


app = Flask(__name__)


@app.before_request
def before_request():
	initialize_db()


@app.teardown_request
def teardown_request(exception):
	close_db()


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		weekday = int(request.form.get('weekday'))
		monthday = int(request.form.get('monthday'))
		special = request.form.get('special', 0)

		if special == 'on':
			special = 1

		return render_template('result.html', 
			result=get_result(weekday, monthday, special))
	return render_template('index.html')


@app.route('/records')
def records():
	return render_template('records.html')


@app.route('/records/create', methods=['GET', 'POST'])
def create():
	if request.method == 'POST':
		special = request.form.get('special', 0)
		result = request.form.get('result', 0)

		if special == 'on':
			special = 1

		if result == 'on':
			result = 1

		Record.insert(
			weekday=request.form.get('weekday', 1), 
			monthday=request.form.get('monthday', 1), 
			special=special, 
			result=result).execute()

	return render_template('create_record.html')


@app.route('/api/records')
def get_records():
	return jsonify([model_to_dict(record) for record in Record.select()])


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)