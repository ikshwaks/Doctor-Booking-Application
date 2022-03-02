from collections import defaultdict
import random

from Appointment import Appointment
from Doctor import Doctor
from Patient import Patient
from Slot import Slot
from exceptions.OverlappingException import OverlappingException
from services.BookingService import BookingService
from services.SlotService import SlotService
from services.UserService import UserService
from utils import Utils

userService = UserService()

slotService = SlotService()

bookingService = BookingService(slotService)

def bookingManager():
    try:
        doctor1 = userService.createDoctor("John", "john@gmail.com")
        print("Dr. {}'s account created successfully with ID {}".format(doctor1.name, doctor1.id))

        doctor2 = userService.createDoctor("Raju", "raju@gmail.com")
        print("Dr. {}'s account created successfully with ID {}".format(doctor2.name, doctor2.id))

        slot1 = slotService.createSlot(doctor1.id, 230, 260)
        print("Dr. {} created a slot successfully and its ID is {}".format(doctor1.name, slot1.id))

        slot2 = slotService.createSlot(doctor1.id, 255, 285)
        print("Dr. {} created a slot successfully and its ID is {}".format(doctor1.name, slot2.id))

        slot3 = slotService.createSlot(doctor2.id, 240, 270)
        print("Dr. {} created a slot successfully and its ID is {}".format(doctor2.name, slot3.id))

    except OverlappingException as oe:
        print(str(oe))
    # patient1 = userService.createPatient("")

if __name__ == "__main__":
    bookingManager()