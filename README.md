# Notable project 

# Setting up 
1. `pip install python`
2. `pip install flask`
3. `pip install flask_restful` 
4. `git clone https://github.com/marisawong/notable.git`

# Starting up the server
1. cd into notable project 
2. `export FLASK_APP=notable_project.py`
3. `flask run` 

# Example Usage
Note: please have `flask run` command running in a separate terminal tab. Open up a new terminal tab and run the following: 

**Get a list of all doctors**

`curl http://127.0.0.1:5000/doctors`

**Get a list of all appointments for a particular doctor and particular day**

`curl http://127.0.0.1:5000/doctors/<DOCTOR_ID>/appointments`

Example: `curl http://127.0.0.1:5000/doctors/1/appointments`

**Optional query parameter to look for appointments on a particular day**

`curl http://127.0.0.1:5000/doctors/<DOCTOR_ID>/appointments?date=<YYYY-MM-DD>`

Example: `curl http://127.0.0.1:5000/doctors/1/appointments?date=2020-01-01`


**Delete an existing appointment from a doctor's calendar**

`curl -X "DELETE" http://localhost:5000/doctors/<DOCTOR_ID>/appointments/<APPT_ID>`

Example: `curl -X "DELETE" http://localhost:5000/doctors/1/appointments/4`

**Add a new appointment to a doctor's calendar**

`curl -i -H "Content-Type: application/json" -X POST -d '{"patient_name":<PATIENT_NAME>, "date":<YYYY-MM-DD>, "time":<HH:MM>, "kind":<KIND>}' http://localhost:5000/doctors/<DOCTOR_ID>/appointments`

Example: `curl -i -H "Content-Type: application/json" -X POST -d '{"patient_name":"Hawkeye", "date":"2020-01-01", "time":"8:00", "kind":"Follow-up"}' http://localhost:5000/doctors/1/appointments`




