from collections import defaultdict
import random
import traceback

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
    traceback_ = ""
    try:
        doctor1 = userService.createDoctor("John", "john@gmail.com")
        print("Dr. {}'s account created successfully with ID {}".format(doctor1.name, doctor1.id))

        doctor2 = userService.createDoctor("Raju", "raju@gmail.com")
        print("Dr. {}'s account created successfully with ID {}".format(doctor2.name, doctor2.id))

        slot1 = slotService.createSlot(doctor1.id, 230, 260)
        print("Dr. {} created a slot successfully and its ID is {}".format(doctor1.name, slot1.id))

        # slot2 = slotService.createSlot(doctor1.id, 255, 285)
        # print("Dr. {} created a slot successfully and its ID is {}".format(doctor1.name, slot2.id))

        slot3 = slotService.createSlot(doctor2.id, 240, 270)
        print("Dr. {} created a slot successfully and its ID is {}".format(doctor2.name, slot3.id))

        print("Availablility of all doctors \n{}".format(slotService.getAvailability()))
        print("Availablility of doctor with id {} \n{}".format(doctor1.id, slotService.getDoctorAvailability(doctor1.id)))
        
        patient1 = userService.createPatient("Bob", "bob@gmail.com")
        print("Patient {} created with id {} successfully".format(patient1.name, patient1.id))

        patient2 = userService.createPatient("Surya", "surya@gmail.com")
        print("Patient {} created with id {} successfully".format(patient2.name, patient2.id))

        appointment1 = bookingService.bookAppointment(patient1.id, doctor1.id, slot1.id)
        print("Appointment for patient {} with id {} for slot {} by doctor {} booked successfully - ID {}".format(patient1.name, patient1.id, slot1.id, doctor1.name, appointment1.id))

        # appointment2 = bookingService.bookAppointment(patient2.id, doctor2.id, slot1.id)
        # print("Appointment for patient {} with id {} for slot {} by doctor {} booked successfully - ID {}".format(patient2.name, patient2.id, slot1.id, doctor2.name, appointment2.id))

        appointment2 = bookingService.bookAppointment(patient1.id, doctor2.id, slot3.id)
        print("Appointment for patient {} with id {} for slot {} by doctor {} booked successfully - ID {}".format(patient1.name, patient1.id, slot3.id, doctor2.name, appointment2.id))

        doctor1Appointments = bookingService.getDoctorAppointments(doctor1.id)

        print("Doctor 1 appointments - \n{}".format(doctor1Appointments))

        patient1Appointments = bookingService.getPatientAppointments(patient1.id)

        print("Patient 1 appointments -\n{}".format(patient1Appointments))

    except OverlappingException as oe:
        print(repr(oe))

    except Exception as e:
        traceback_ = traceback.format_exc()
        print(repr(e))

    finally:
        print(traceback_)

if __name__ == "__main__":
    bookingManager()