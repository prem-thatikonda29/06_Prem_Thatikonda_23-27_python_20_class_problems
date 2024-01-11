from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.reservations = []

    def is_available(self, start_time, end_time):
        for reservation in self.reservations:
            if not (end_time <= reservation["start_time"] or start_time >= reservation["end_time"]):
                return False
        return True

    def book_room(self, user, start_time, end_time):
        if self.is_available(start_time, end_time):
            self.reservations.append({"user": user, "start_time": start_time, "end_time": end_time})
            print(f"Room {self.room_number} booked successfully for {user} from {start_time} to {end_time}.")
        else:
            print(f"Room {self.room_number} is not available during the specified time.")

    def __str__(self):
        return f"Room {self.room_number} - Capacity: {self.capacity}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class ConferenceRoomBookingSystem:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def display_available_rooms(self, start_time, end_time):
        available_rooms = [room for room in self.rooms if room.is_available(start_time, end_time)]
        if not available_rooms:
            print("No rooms are available during the specified time.")
        else:
            print("Available Rooms:")
            for room in available_rooms:
                print(room)

# Menu Interface
def print_menu():
    print("\nConference Room Booking System Menu:")
    print("1. View Room Availability")
    print("2. Book a Room")
    print("3. Exit")

def get_booking_duration():
    try:
        minutes = int(input("Enter the number of minutes to book the room for: "))
        if minutes <= 0:
            raise ValueError("Invalid duration. Please enter a positive number of minutes.")
        return minutes
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    # Creating dummy instances of rooms, users, and the booking system
    room1 = Room(101, 20)
    room2 = Room(102, 15)
    room3 = Room(103, 25)
    room4 = Room(104, 30)
    room5 = Room(105, 50)
    user1 = User(1, "John Doe")
    user2 = User(2, "Jane Smith")
    booking_system = ConferenceRoomBookingSystem()

    # Add rooms to the booking system
    booking_system.add_room(room1)
    booking_system.add_room(room2)
    booking_system.add_room(room3)
    booking_system.add_room(room4)
    booking_system.add_room(room5)

    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # View Room Availability
            room_number = int(input("Enter room number: "))
            room_to_check = booking_system.find_room(room_number)
            if room_to_check:
                current_time = datetime.now()
                availability_status = room_to_check.is_available(current_time, current_time)
                print(f"Room {room_to_check.room_number} availability: {availability_status}")
            else:
                print(f"Room {room_number} not found.")

        elif choice == "2":
            # Book a Room
            booking_duration = get_booking_duration()
            if booking_duration is not None:
                current_time = datetime.now()
                end_time = current_time + timedelta(minutes=booking_duration)
                booking_system.display_available_rooms(current_time, end_time)
                room_number = int(input("Enter the room number you want to book: "))
                room_to_book = booking_system.find_room(room_number)
                if room_to_book:
                    user_name = input("Enter your name: ")
                    room_to_book.book_room(user_name, current_time, end_time)
                else:
                    print(f"Room {room_number} not found.")

        elif choice == "3":
            # Exit
            print("Exiting the Conference Room Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
