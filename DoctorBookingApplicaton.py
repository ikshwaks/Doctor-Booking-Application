from collections import defaultdict
import random

from Appointment import Appoinment
from Doctor import Doctor
from Patient import Patient
from Slot import Slot
from utils import Utils

appointmentsMap = {}

def bookingManager():
    str = "1. Register doctor"
    print(str)

    slotStr = "9:30-10:00"
    times = slotStr.split('-')
    startTime = int(times[0].split(':')[0]) * 60 + int(times[0].split(':')[1])
    endTime = int(times[1].split(':')[0]) * 60 + int(times[1].split(':')[1])
    slotId = random.randint(10001, 20000)
    if Utils.Utils.isOverlapping(slotsMap, doctorId, startTime, endTime):
        print("You have overlapping slot, please book a slot with different timing")
        # TODO
    slot = Slot(slotId, startTime, endTime, doctorId)
    slotsMap[slotId] = slot
    print("Slot created successfully with ID - {}".format(slotId))
    
    appointmentId = random.randint(20001, 30000)
    if Utils.Utils.isConflictingSlot(appointmentsMap, patientId, slotsMap, slotId):
        print("You have conflicting appointment already, please choose\
             a new slot with different timing")
        # TODO
    appointment = Appoinment(appointmentId, patientId, doctorId, slotId)
    slotsMap[slotId].availabilty = False
    appointmentsMap[appointmentId] = appointment
    print("Appointment created successfully with ID - {}".format(appointmentId))

    # Show slots
    slotsList = [slot for slotId, slot in slotsMap.items() if slot.doctorId == doctorId]
    sortedTimeSlots = Utils.Utils.getSortedTimeSlots(slotsList)
    print(sortedTimeSlots)

    # Cancellation of the appointment
    slotsMap[appointmentsMap[appointmentId].slotId].availability = True
    appointmentsMap.pop(appointmentId)

    # Show appointments
    appointmentSlotsList = [slotsMap[appointment.slotId] \
        for appointment in appointmentsMap.values() \
        if appointment.patientId == patientId]
    sortedTimeSlots = Utils.Utils.getSortedTimeSlots(appointmentSlotsList)
    print(sortedTimeSlots)



if __name__ == "__main__":
    bookingManager()