class Utils:
    @staticmethod
    def isOverlapping(slotsMap, doctorId, startTime, endTime):
        # TODO: Implement this functionality
        for slot in slotsMap.values():
            if slot.doctorId == doctorId:
                if (slot.startTime < startTime and startTime < slot.endTime) \
                    or (slot.startTime < endTime and endTime < slot.endTime):
                    return True
        return False
    
    @staticmethod
    def isConflictingSlot(appointmentsMap, patientId, slotsMap, slotId):
        # TODO: Implement this functionality
        return False
    
    def getSortedTimeSlots(slots):
        # TODO
        return []