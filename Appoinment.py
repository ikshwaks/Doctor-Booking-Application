from AppoinmentStatus import AppoinmentStatus


class Appoinment:
    def __init__(self, id, patientID, doctorID, slotID) -> None:
        self.id = id
        self.patientID = patientID
        self.doctorID = doctorID
        self.slotID = slotID
        self.status = AppoinmentStatus.CREATED
