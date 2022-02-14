from collections import defaultdict
import random

from Appoinment import Appoinment
from Doctor import Doctor
from Patient import Patient
from Slot import Slot


doctorsMap = defaultdict(int)
patientsMap = {}
slotsMap = {}
appointmentsMap = {}

def bookingManager():
    str = "1. Register doctor"
    print(str)

    doctorId = random.randint(1, 10000)
    doc1 = Doctor(doctorId, "Curious", "curious@gmail.com")
    doctorsMap[doctorId] = doc1
    print("Doctor created successfully with ID - {}".format(doctorId))

    patientId = random.randint(1, 10000)
    patient1 = Patient(patientId, "John", "john@gmail.com")
    patientsMap[patientId] = patient1
    print("Patient created successfully with ID - {}".format(patientId))

    slotStr = "9:30-10:00"
    times = slotStr.split('-')
    startTime = int(times[0].split(':')[0]) * 60 + int(times[0].split(':')[1])
    endTime = int(times[1].split(':')[0]) * 60 + int(times[1].split(':')[1])
    slotId = random.randint(10001, 20000)
    slot = Slot(slotId, startTime, endTime, doctorId)
    slotsMap[slotId] = slot
    print("Slot created successfully with ID - {}".format(slotId))

    appointmentId = random.randint(20001, 30000)
    appointment = Appoinment(appointmentId, patientId, doctorId, slotId)
    slotsMap[slotId].availabilty = False
    appointmentsMap[appointmentId] = appointment
    print("Appointment created successfully with ID - {}".format(appointmentId))


if __name__ == "__main__":
    bookingManager()