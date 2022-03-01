import random
from Appoinment import Appoinment
from AppoinmentStatus import AppoinmentStatus
from AvailabilityStatus import AvailabilityStatus
from services.SlotService import SlotService
from utils.Utils import Utils


class BookingService:
    
    def __init__(self, slotService):
        self.slotService = slotService
        self.appointmentsMap = {}

    # def __isPatientAvailable(self, patientId, slotId):
    #     for appoinment in self.appoinmentsMap:
    #         if appoinment.patientId == patientId:


    def bookAppoinment(self, patientId, doctorId, slotId):
        # TODO: How to handle multiple requests at a time in multi threading
        # environment
        slot = self.slotService(slotId)
        if not slot.isAvailable():
            raise Exception("Slot is not available")
        if Utils.isConflictingSlot(self.appointmentsMap, patientId, \
            self.slotService.slotsMap, slotId):
            raise Exception("Patient has a conflicting appointment")
        slot.setAvailabilityStatus(AvailabilityStatus.BOOKED)
        appointmentId = random.randint(20001, 30000)
        self.appointmentsMap[appointmentId] = Appoinment(appointmentId, \
            patientId, doctorId, slotId)
        return appointmentId

    def cancelAppoinment(self, appointmentId):
        if not isinstance(appointmentId, int):
            raise Exception("Appointment ID is not valid")
        if appointmentId not in self.appointmentsMap:
            raise Exception("Appointment ID is not valid")
        appoinment = self.appointmentsMap[appointmentId]
        appoinment.status = AppoinmentStatus.CANCELLED
        self.slotService.updateSlot(appoinment.slotId, AvailabilityStatus.AVAILABLE)
    
    def addToWaitlist():
        pass