import random
from Doctor import Doctor
from Patient import Patient

class UserService:
    def __init__(self) -> None:
        self.doctorsMap = {}
        self.patientsMap = {}

    def createDoctor(self, name, email):
        doctorId = random.randint(1, 10000)
        doctor = Doctor(doctorId, name, email)
        self.doctorsMap[doctorId] = doctor
        return doctor

    def createPatient(self, name, email):
        patientId = random.randint(1, 10000)
        patient = Patient(patientId, name, email)
        self.patientsMap[patientId] = patient
        return patient