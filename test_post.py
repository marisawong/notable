import requests

appt_example = {
	'patient_name': 'Hawkeye',
	'date': '2020-01-01', 
	'time': '8:00', 
	'kind': 'Follow-up'
}
resp = requests.post("http://localhost:5000/doctors/1/appointments", data=appt_example)
print(resp)