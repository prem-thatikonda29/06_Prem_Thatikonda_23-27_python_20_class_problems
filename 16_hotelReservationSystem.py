from datetime import datetime, timedelta
from time import sleep

class Room:
    def __init__(self, roomID, capacity, hourly_rate):
        self.roomID = roomID
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.booked_slots = {}

    def is_available(self, start_time, end_time):
        for booked_start, booked_end in self.booked_slots.values():
            if start_time < booked_end and end_time > booked_start:
                return False
        return True

    def book_room(self, user, start_time, end_time):
        if self.is_available(start_time, end_time):
            booking_id = f"{user.userID}_{len(self.booked_slots) + 1}"
            self.booked_slots[booking_id] = (start_time, end_time)
            print(f"Room {self.roomID} booked by {user.name} from {start_time} to {end_time}. Booking ID: {booking_id}")
            return booking_id
        else:
            print("Room not available for the specified time")
            return None

    def calculate_cost(self, booking_id):
        start_time, end_time = self.booked_slots.get(booking_id, (None, None))
        if start_time and end_time:
            duration = (end_time - start_time).total_seconds() / 3600  # convert seconds to hours
            return duration * self.hourly_rate
        else:
            return 0

class User:
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room, user, start_time, end_time):
        booking_id = room.book_room(user, start_time, end_time)
        if booking_id:
            return booking_id
        else:
            return None

    def generate_invoice(self, room, booking_id):
        booking_info = room.booked_slots.get(booking_id)
        if booking_info:
            start_time, end_time = booking_info
            cost = room.calculate_cost(booking_id)
            print("----------------------------------------------------")
            print(f"Invoice for Room {room.roomID} - Booking ID {booking_id}:")
            print(f"Duration: {start_time} to {end_time}")
            print(f"Total Cost: ${cost:.2f}")
            print("----------------------------------------------------")
        else:
            print("Error generating invoice. Booking ID not found.")

    def check_availability(self):
        print("Fetching available rooms...")
        sleep(1.5)
        print("Available rooms:")
        for room in self.rooms:
            print(f"Room {room.roomID}, Capacity: {room.capacity}, Hourly Rate: ${room.hourly_rate}")

    def find_room(self, roomID):
        for room in self.rooms:
            if room.roomID == roomID:
                return room
        return None

def main():
    room1 = Room(101, 30, 10.0)
    room2 = Room(102, 25, 8.0)
    room3 = Room(103, 25, 12.0)
    room4 = Room(104, 30, 15.0)
    room5 = Room(105, 50, 20.0)

    hotel = Hotel()
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)
    hotel.add_room(room4)
    hotel.add_room(room5)

    print("Enter name: ", end="")
    name = input("")
    user1 = User(name, 1234)

    print("Welcome to Trivago!")
    while True:
        print("\n1)Check available rooms")
        print("2)Book room")
        print("3)Generate Invoice")
        print("4)Exit")
        cmd = input("\nPlease enter your command (or 'q' to quit): ")
        if cmd == '1':
            hotel.check_availability()
        
        elif cmd == '2':
            print("\nEnter the room number you want to book: ", end='')
            rid = int(input())
            roomToBook = hotel.find_room(rid)
            if roomToBook is not None:
                print("Enter booking start time (YYYY-MM-DD HH:MM): ", end='')
                start_time = datetime.strptime(input(), "%Y-%m-%d %H:%M")
                print("Enter booking end time (YYYY-MM-DD HH:MM): ", end='')
                end_time = datetime.strptime(input(), "%Y-%m-%d %H:%M")
                print("Booking room...")
                sleep(1)
                booking_id = hotel.book_room(roomToBook, user1, start_time, end_time)
                if booking_id:
                    print(f"Room booked successfully. Booking ID: {booking_id}")
            else:
                print("Room unavailable")

        elif cmd == '3':
            print("\nEnter the room number for which you want to generate an invoice: ", end='')
            rid = int(input())
            roomToInvoice = hotel.find_room(rid)
            if roomToInvoice is not None:
                print("Enter booking ID: ", end='')
                booking_id = input()
                hotel.generate_invoice(roomToInvoice, booking_id)
            else:
                print("Room not found")

        elif cmd == '4':
            print("Exiting. Thank you!")
            break

if __name__ == "__main__":
    main()
