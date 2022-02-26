import enum

class AvailabilityStatus(enum.Enum):
    AVAILABLE = 1
    BOOKED = 2
    BOOKING_ONGOING = 3 # If the booking in progress and not yet completed
    CANCELLED = 4 # If there is a cancellation of the slot