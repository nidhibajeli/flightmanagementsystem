import random
#made a simple parent class called flight and added attributes like flight no, destination, runway stat and fuel lvl
class Flight:
    def __init__(self, flight_number, destination, runway_status, fuel_level):
        self.flight_number = flight_number
        self.destination = destination
        self.runway_status = runway_status
        self.fuel_level = fuel_level
        #here we are creating empty set and dictionary with passenger info
        self.passengers = []
        self.seats = {}
        self.luggage_weights = {}
#making another fn about passenger alloting to details
    def add_passenger(self, passenger_name, seat_number, luggage_weight):
        self.passengers.append(passenger_name)
        self.seats[passenger_name] = seat_number
        self.luggage_weights[passenger_name] = luggage_weight
#runway status is checked here
    def check_runway(self):
        if self.runway_status == "free":
            return "Land now"
        elif self.fuel_level == "low":
            return "Emergency landing"
        else:
            return "Circle in the air"

    def get_flight_to_land(self):
        return self.check_runway()

    def get_passenger_check(self):
        return [f"Passenger {passenger} is checked in." for passenger in self.passengers]

    def get_items_from_conveyor_belt(self):
        return "Please take your items from the conveyor belt."
#the baggage clearance is done here 
    def check_baggage_weight(self, airline, luggage_weight):
        AI_weight_limit = 30
        EM_weight_limit = 35
        if airline == "AirIndia":
            if luggage_weight <= AI_weight_limit:
                return "Check-in cleared"
            else:
                return "Remove some luggage and come back"
        elif airline == "Emirates":
            if luggage_weight <= EM_weight_limit:
                return "Check-in cleared"
            else:
                return "Remove some luggage and come back"
        else:
            return "Invalid airline"
#preferance of luggage loading
    def luggage_loading_order(self, weights):
        first = min(weights)
        last = max(weights)
        return f"{first} kg luggage will be loaded first\n{last} kg luggage will be loaded last"
#if u want to check available flights at airpport
    def flights_at_airport(self, flights_originally, no_of_landing, no_of_takeoffs):
        no_of_flights_at_airport = no_of_landing - no_of_takeoffs + flights_originally
        return f"Number of flights at the airport: {no_of_flights_at_airport}"
#haha, made this for fun , this is a small menu
    def display_menu(self):
        menu = (
            "________________________________________________________________________\n"
            "BREAD BASKET\n"
            "Looking for a healthy breakfast, this is the place for you!!\n"
            "________________________________________________________________________\n"
            "ITEM                          RATE\n"
            "Raisin Toast                $2.50\n"
            "French Toast                $2.80\n"
            "Mushroom Toast              $3.00\n"
            "Pancake                     $4.00\n"
            "Pancake with Ice-cream      $7.50\n"
            "Chef's speciality           $10.00\n"
            "__________________________________________________________________________"
        )
        return menu
#allotment of ticket is done here
    def allot_tickets(self, no_of_passengers, starting_ticket_number):
        tickets = []
        ticket_number = starting_ticket_number
        while no_of_passengers > 0:
            tickets.append(f"T - {ticket_number}")
            ticket_number += 1
            no_of_passengers -= 1
        return tickets

# Generate fictional data for 100 passengers
def generate_passenger_data():
    specified_names = ["Nidhi", "Harsh", "Vijay", "Deepa", "Ajay", "Aditya", "Vanya", "Neha", "Kavya", "Sana", "Akhand", "Mannu", "Riddhi", "Ayush"]
    random_names = [f"Passenger_{i}" for i in range(1, 87)]
    all_names = specified_names + random_names
    seats = [f"{random.randint(1, 30)}{chr(random.randint(65, 70))}" for _ in range(100)]
    luggage_weights = [random.randint(20, 40) for _ in range(100)]
    return list(zip(all_names, seats, luggage_weights))

# Example usage
def main():
    print("We welcome you to 202 by NIDHI!")
    flight1 = Flight("AI101", "New York", "free", "full")
    passenger_data = generate_passenger_data()
    for name, seat, weight in passenger_data:
        flight1.add_passenger(name, seat, weight)
    while True:
        user_type = input("Are you a pilot or a passenger? (pilot/passenger): ").strip().lower()
        #pilot verification
        if user_type == "pilot":
            pilot_name = input("Please verify your name: ").strip()
            if pilot_name.lower() == "nidhi":
                print("\nInternal Flight Details:")
                print(f"Flight Number: {flight1.flight_number}")
                print(f"Destination: {flight1.destination}")
                print(f"Runway Status: {flight1.runway_status}")
                print(f"Fuel Level: {flight1.fuel_level}")
                print(f"Number of Passengers: {len(flight1.passengers)}")
                print(f"Next Flight to Land: {flight1.get_flight_to_land()}")
            else:
                print("Verification failed. You are not authorized to access this information.")
            break
        #passenger 
        elif user_type == "passenger":
            passenger_name = input("Enter your name: ").strip()
            if passenger_name in flight1.seats:
                while True:
                    print(f"\nWelcome, {passenger_name}!")
                    print("Options:")
                    print("1. Check flight details")
                    print("2. Check ticket details")
                    choice = input("Enter your choice: ").strip()
                    if choice == "1":
                        print(f"Flight Number: {flight1.flight_number}")
                        print(f"Destination: {flight1.destination}")
                        print(f"Runway Status: {flight1.runway_status}")
                        print(f"Fuel Level: {flight1.fuel_level}")
                    elif choice == "2":
                        print(f"Passenger Name: {passenger_name}")
                        print(f"Seat Number: {flight1.seats[passenger_name]}")
                        print(f"Luggage Weight: {flight1.luggage_weights[passenger_name]} kg")
                    else:
                        print("Invalid choice.")
                    
                    show_menu = input("Would you like to see the food menu? (yes/no): ").strip().lower()
                    if show_menu == "yes":
                        print(flight1.display_menu())
                    else:
                        print("Thank you! Have a great flight!")
                    
                    check_fellow_passenger = input("Would you like to check for a fellow passenger? (yes/no): ").strip().lower()
                    if check_fellow_passenger == "yes":
                        fellow_passenger = input("Enter the name of the fellow passenger: ").strip()
                        if fellow_passenger in flight1.seats:
                            print(f"Fellow Passenger Name: {fellow_passenger}")
                            print(f"Seat Number: {flight1.seats[fellow_passenger]}")
                            print(f"Luggage Weight: {flight1.luggage_weights[fellow_passenger]} kg")
                        else:
                            print("Fellow passenger not found.")
                    else:
                        print("Thank you! Have a great flight!")
                    
                    go_back = input("Would you like to go back to the main menu? (yes/no): ").strip().lower()
                    if go_back != "yes":
                        print("thankyou! have a nice day ahead!")
                        break
            else:
                print("Your name is not on the list. Please check at the reception area.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
#for anybody who is new to coding .strip() is used so that even if someone enters a space after or before the input their ans still gets verified and no error occurs
