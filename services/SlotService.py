from collections import defaultdict
from email.policy import default
import random
from Slot import Slot

from AvailabilityStatus import AvailabilityStatus
import Constants
from exceptions.OverlappingException import OverlappingException
from exceptions.InvalidInstanceException import InvalidInstanceException
from utils import Utils

class SlotService:
    def __init__(self) -> None:
        self.slotsMap = defaultdict(Slot)

    def createSlot(self, doctorId, startTime, endTime):
        # TODO: What happen if this method is called by threads in parallel
        slotId = random.randint(10001, 20000)
        if Utils.Utils.isOverlapping(self.slotsMap, doctorId, startTime, endTime):
            raise OverlappingException("You have a overlapping slot, please book a slot with different timing")
        slot = Slot(slotId, startTime, endTime, doctorId)
        self.slotsMap[slotId] = slot # REVISIT: Think about moving to different method

    def getDoctorAvailability(self, doctorId):
        if not isinstance(doctorId, int):
            raise InvalidInstanceException(Constants.INVALID_DOCTOR_ID_ERROR_MSG)
        availability = []
        for id, slot in self.slotsMap.items():
            if slot.doctorId == doctorId and slot.availability == \
                AvailabilityStatus.AVAILABLE:
                availability.append((id, (slot.startTime, slot.endTime)))
        availability.sort(key = lambda tple:tple[1][0])
        return availability
    
    def getAvailability(self):
        availability = []
        for id, slot in self.slotsMap.items():
            if slot.availability == AvailabilityStatus.AVAILABLE:
                availability.append((id, slot.doctorId, (slot.startTime, slot.endTime)))
        # TODO: Think about moving sort functionality to a new function
        availability.sort(key = lambda tple:tple[2][0]) 
        return availability

    def updateSlot(self, slotId, status):
        # TODO: Revisit and update it as private or public, can have multiple
        # functions dedicate to one responsibility
        if slotId not in self.slotsMap.keys():
            # raise
            pass
        self.slotsMap[slotId].setAvailabilityStatus(status)