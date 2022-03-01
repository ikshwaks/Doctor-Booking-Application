from collections import deque
from AvailabilityStatus import AvailabilityStatus
import Constants

class Slot:
    def __init__(self, id, startTime, endTime, doctorId) -> None:
        self.id = id
        self.startTime = startTime
        self.endTime = endTime
        self.doctorId = doctorId
        self.availability = AvailabilityStatus.AVAILABLE
        self.waitList = deque()
    
    def setAvailabilityStatus(self, status):
        if status not in (AvailabilityStatus):
            raise Exception(Constants.INVALID_STATUS_ERROR_MSG)
        # TODO: What if two threads trying to change the same slot - one solution is we can add mutex
        self.availability = status
    
    def isAvailable(self):
        if self.availability == AvailabilityStatus.AVAILABLE:
            return True
        return False