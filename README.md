# Vending Machine for Train Tickets

This repository contains a Python program that simulates a vending machine for selling train tickets. The program loads ticket information from a file and allows users to buy tickets for various destinations, handling payment and change calculation.

## Features

1. **Load Initial Data**: The machine initializes with ticket availability and fare information from a text file.
2. **Select Destination**: Users can choose from a list of destinations displayed in the main menu.
3. **Purchase Tickets**: Handles ticket purchases, checks for ticket availability, and processes payments.
4. **Payment Handling**: Accepts coins, calculates the total, and dispenses change if needed. Allows cancellation during payment.
5. **Exit Option**: Users can exit the vending machine at any time.

## Rules and Specifications

1. **Input File Format**:
   - The first line specifies the total number of tickets available.
   - Subsequent lines list destinations and their respective fares (e.g., `DestinationName Fare`).
   - Example file:
     ```
     5
     CityA 15
     CityB 10
     CityC 20
     ```

2. **Main Menu**:
   - Displays the list of destinations and prompts the user to select one or exit.

3. **Ticket Purchase**:
   - Users specify the number of tickets. If the machine has insufficient tickets, an error is shown.

4. **Payment Process**:
   - Users insert coins until the total matches or exceeds the ticket price.
   - Coins accepted: $1, $2, $5, $10.
   - If canceled, inserted coins are returned in ascending order.

5. **Out of Service**:
   - If tickets are sold out, the machine notifies the user and exits upon confirmation.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vending-machine.git
   cd vending-machine
   ```

2. Prepare an input file (e.g., `init.txt`) with the required format.

3. Run the program:
   ```bash
   python vending_machine.py
   ```

4. Follow the on-screen prompts to:
   - Choose a destination.
   - Specify the number of tickets.
   - Insert coins to complete the purchase.

## Example Run

Input file (`init.txt`):
```
3
CityA 15
CityB 10
CityC 20
```

Sample output:
```
File to initialize the vending machine:
init.txt


Station(s): CityA, CityB, CityC.
Please choose a destination or enter 'Exit':
CityA


Please enter the number of tickets:
2


Destination: CityA, Quantity: 2, Price: $30, Inserted: $0.
Please insert a coin or enter 'Cancel':
10


Destination: CityA, Quantity: 2, Price: $30, Inserted: $10.
Please insert a coin or enter 'Cancel':
20


Destination: CityA, Quantity: 2, Price: $30, Inserted: $30.
Dropped ticket(s). Your change: $0.


Station(s): CityA, CityB, CityC.
Please choose a destination or enter 'Exit':
Exit


Bye
```

## Functions in the Program

- **File Initialization**: Loads ticket count and fare chart from a file.
- **Main Menu**: Displays available destinations and handles user input.
- **Payment Process**: Manages coin insertion, change calculation, and ticket dispensing.
- **Error Handling**: Ensures valid inputs and appropriate responses for insufficient tickets or payment.

## Notes

- Ensure the input file is in the same directory as the script.
- Only valid coins ($1, $2, $5, $10) are accepted.
- Cancellation returns inserted coins in ascending order.

---

Feel free to contribute or provide feedback!
