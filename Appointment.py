from AppointmentStatus import AppointmentStatus

class Appointment:
    def __init__(self, id, patientID, doctorID, slotID) -> None:
        self.id = id
        self.patientID = patientID
        self.doctorID = doctorID
        self.slotID = slotID
        self.status = AppointmentStatus.CREATED
