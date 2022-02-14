class Slot:
    def __init__(self, id, startTime, endTime, doctorID) -> None:
        self.id = id
        self.startTime = startTime
        self.endTime = endTime
        self.doctorID = doctorID
        self.availability = True