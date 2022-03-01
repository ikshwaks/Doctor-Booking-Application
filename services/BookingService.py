import random

from Appointment import Appointment
from AppointmentStatus import AppointmentStatus
from AvailabilityStatus import AvailabilityStatus
import Constants
from utils.Utils import Utils


class BookingService:
    
    def __init__(self, slotService):
        self.slotService = slotService
        self.appointmentsMap = {}

    # def __isPatientAvailable(self, patientId, slotId):
    #     for appoinment in self.appoinmentsMap:
    #         if appoinment.patientId == patientId:


    def bookAppointment(self, patientId, doctorId, slotId):
        # TODO: How to handle multiple requests at a time in multi threading
        # environment
        slot = self.slotService(slotId)
        if not slot.isAvailable():
            raise Exception(Constants.SLOT_NOT_AVAILABLE_ERR_MSG)
        if Utils.isConflictingSlot(self.appointmentsMap, patientId, \
            self.slotService.slotsMap, slotId):
            raise Exception("Patient has a conflicting appointment")
        slot.setAvailabilityStatus(AvailabilityStatus.BOOKED)
        appointmentId = random.randint(20001, 30000)
        self.appointmentsMap[appointmentId] = Appointment(appointmentId, \
            patientId, doctorId, slotId)
        return appointmentId

    def cancelAppointment(self, appointmentId):
        if not isinstance(appointmentId, int):
            raise Exception(Constants.INVALID_APPOINTMENT_ID_ERR_MSG)
        if appointmentId not in self.appointmentsMap:
            raise Exception(Constants.INVALID_APPOINTMENT_ID_ERR_MSG)
        appoinment = self.appointmentsMap[appointmentId]
        appoinment.status = AppointmentStatus.CANCELLED
        self.slotService.updateSlot(appoinment.slotId, AvailabilityStatus.AVAILABLE)
    
    def addToWaitlist():
        pass