from AppointmentStatus import AppointmentStatus

class Appointment:
    def __init__(self, id, patientId, doctorId, slotId) -> None:
        self.id = id
        self.patientId = patientId
        self.doctorId = doctorId
        self.slotId = slotId
        self.status = AppointmentStatus.CREATED
