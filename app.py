from flask import Flask, render_template, request, redirect
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# ==========================
# FIREBASE INITIALIZATION
# ==========================

cred = credentials.Certificate("firebase-key.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://caresync360-b1751-default-rtdb.firebaseio.com/'
})

# ==========================
# DEPARTMENTS
# ==========================

departments = [
    "General Medicine",
    "Emergency",
    "Cardiology",
    "Orthopedics",
    "Neurology",
    "Pediatrics",
    "Gynecology",
    "Dermatology",
    "Radiology",
    "Oncology"
]

# ==========================
# HOME
# ==========================

@app.route('/')
def home():
    return render_template("index.html", departments=departments)

# ==========================
# REGISTER PATIENT (SAVE TO FIREBASE)
# ==========================

@app.route('/register', methods=['POST'])
def register():

    name = request.form['name']
    age = request.form['age']
    department = request.form['department']
    category = request.form['priority']

    priority_map = {
        "Emergency": 1,
        "Senior": 2,
        "Normal": 3
    }

    # Get existing patients
    patients_ref = db.reference('patients')
    patients_data = patients_ref.get() or {}

    count = len(patients_data) + 1

    patient_id = f"P{1000 + count}"
    token = f"T{count:02d}"

    new_patient = {
        "patient_id": patient_id,
        "token": token,
        "name": name,
        "age": age,
        "department": department,
        "priority": priority_map[category],
        "category": category,
        "status": "Waiting",
        "time": str(datetime.now())
    }

    patients_ref.push(new_patient)

    return redirect('/dashboard')

# ==========================
# DASHBOARD (READ FROM FIREBASE)
# ==========================

@app.route('/dashboard')
def dashboard():

    patients_ref = db.reference('patients')
    patients_dict = patients_ref.get() or {}

    patients = []

    for key, value in patients_dict.items():
        value["id"] = key
        patients.append(value)

    # Sort by priority
    patients.sort(key=lambda x: x["priority"])

    total_waiting = len([p for p in patients if p["status"] == "Waiting"])
    emergency_count = len([p for p in patients if p["priority"] == 1])
    completed_count = len([p for p in patients if p["status"] == "Completed"])

    return render_template(
        "dashboard.html",
        patients=patients,
        total_waiting=total_waiting,
        emergency_count=emergency_count,
        completed_count=completed_count,
        departments=departments
    )

# ==========================
# CONSULT PATIENT
# ==========================

@app.route('/consult/<pid>')
def consult(pid):
    db.reference(f'patients/{pid}').update({
        "status": "In Consultation"
    })
    return redirect('/dashboard')

# ==========================
# COMPLETE PATIENT
# ==========================

@app.route('/complete/<pid>')
def complete(pid):
    db.reference(f'patients/{pid}').update({
        "status": "Completed"
    })
    return redirect('/dashboard')

# ==========================
# PATIENT HISTORY
# ==========================

@app.route('/history', methods=['GET', 'POST'])
def history():
    visits = []

    if request.method == 'POST':
        name = request.form['name'].strip().lower()

        patients_ref = db.reference('patients')
        patients_dict = patients_ref.get() or {}

        for key, value in patients_dict.items():
            if value["name"].lower() == name:
                value["id"] = key
                visits.append(value)

    return render_template("history.html", visits=visits)


if __name__ == '__main__':
    app.run(debug=True)