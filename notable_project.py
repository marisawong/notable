from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

total_appointments = 3
doctors = [
	{
		'doctor_id': 1,
		'first_name': 'Marisa', 
		'last_name': 'Wong',
		'appointments': [
			{
				'appt_id': 1,
				'patient_name': 'Tony Stark',
				'date': '2020-01-01', 
				'time': '8:00', 
				'kind': 'New Patient'
			}, 
			{
				'appt_id': 2,
				'patient_name': 'Antman',
				'date': '2020-03-01', 
				'time': '13:30', 
				'kind': 'Follow-up'
			}
		]
	},
	{
		'doctor_id': 2,
		'first_name': 'Ashley', 
		'last_name': 'Smith',
		'appointments': [
			{
				'appt_id': 3,
				'patient_name': 'Black Widow',
				'date': '2020-01-03', 
				'time': '8:00', 
				'kind': 'New Patient'
			}
		]
	},
	{
		'doctor_id': 3,
		'first_name': 'Tom', 
		'last_name': 'Holland', 
		'appointments': []
	}	
]


def get_doctor_by_id(doctor_id): 
	for doctor in doctors: 
		if doctor['doctor_id'] == doctor_id: 
			return doctor 


@app.route('/doctors', methods=['GET'])
def get_all_doctors():
	return jsonify(doctors), 200


@app.route('/doctors/<int:doctor_id>/appointments', methods=['GET'])
def get_appointments_for_doctor(doctor_id):
	date = request.args.get('date')

	doctor = get_doctor_by_id(doctor_id)
	doctor_appts = doctor['appointments']
	filtered_appts = [appt for appt in doctor_appts if appt['date'] == date]
	return jsonify(filtered_appts), 200



@app.route('/doctors/<int:doctor_id>/appointments', methods=['POST'])
def create_new_appointment_for_doctor(doctor_id): 
	doctor = get_doctor_by_id(doctor_id)
	global total_appointments
	appt_id = total_appointments 
	patient_name = request.form.get('patient_name')
	kind = request.form.get('kind')
	date = request.form.get('date')
	time = request.form.get('time')
	print(patient_name, kind, date, time)

	# Check that time is in 15 min intervals 
	time_minute = int(time.split(':')[1])
	if time_minute % 15 != 0: 
		return jsonify({'error': 'Invalid time interval'}), 400

	curr_doctor_appt = doctor['appointments']
	filtered_appt_datetime = [appt for appt in curr_doctor_appt if appt['date'] == date and appt['time'] == time]
	if len(filtered_appt_datetime) < 3: 
		total_appointments += 1 
		new_appt = {
			'appt_id': total_appointments,
			'patient_name': patient_name,
			'date': date,
			'time': time,
			'kind': kind
		}
		curr_doctor_appt.append(new_appt)
		return jsonify(new_appt), 201
	else: 
		return jsonify({'error': 'Doctor is overbooked at this time'}), 400

if __name__ == '__main__':
    app.run(debug=True)
