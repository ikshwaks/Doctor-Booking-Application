import enum

class AppointmentStatus(enum.Enum):
    CREATED = 1
    COMPLETED = 2
    CANCELLED = 3