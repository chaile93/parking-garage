class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket_number] = {"paid": False, "parking_space": parking_space}
            print(f"Ticket {ticket_number} taken. Parking space {parking_space} allocated.")
        else:
            print("Sorry, the parking garage is full.")

    def payForParking(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket:
            if not self.currentTicket[ticket_number]["paid"]:
                amount = input("Enter amount to pay: ")
                if amount:
                    self.currentTicket[ticket_number]["paid"] = True
                    print("Payment successful. You have 15 minutes to leave.")
                else:
                    print("No payment entered.")
            else:
                print("Ticket already paid.")
        else:
            print("Invalid ticket number.")

    def leaveGarage(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]["paid"]:
                parking_space = self.currentTicket[ticket_number]["parking_space"]
                self.parkingSpaces.append(parking_space)
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
                print("Thank you, have a nice day!")
            else:
                print("Payment not made. Please pay before leaving.")
        else:
            print("Invalid ticket number.")


# Example usage:
if __name__ == "__main__":
    parking_garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)

    while True:
        print("\nOptions:")
        print("1. Take a ticket")
        print("2. Pay for parking")
        print("3. Leave garage")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            parking_garage.takeTicket()

        elif choice == '2':
            parking_garage.payForParking()

        elif choice == '3':
            parking_garage.leaveGarage()

        elif choice == '4':
            print("Thank you for using the parking garage system.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")
