class RentalProperty:
    def __init__(self, property_name):
        self.property_name = property_name
        self.rent_amount = 0
        self.occupancy_rate = 0
        self.expenses = 0
        self.property_management_fee = 0

    def get_rent_amount(self):
        self.rent_amount = float(input(f"Enter the rent amount for property '{self.property_name}' per month: "))

    def get_occupancy_rate(self):
        self.occupancy_rate = float(input(f"Enter the occupancy rate (in percentage) for property '{self.property_name}': "))

    def get_expenses(self):
        self.expenses = float(input(f"Enter the total expenses per month for property '{self.property_name}': "))

    def get_property_management_fee(self):
        self.property_management_fee = float(input(f"Enter the property management fee (in percentage) for property '{self.property_name}': "))

    def calculate_rental_income(self):
        self.get_rent_amount()
        self.get_occupancy_rate()
        self.get_expenses()
        self.get_property_management_fee()

        total_income = (self.rent_amount * self.occupancy_rate / 100) - self.expenses - (self.rent_amount * self.property_management_fee / 100)
        return total_income


class RentalIncomeCalculator:
    def __init__(self):
        self.properties = {}

    def add_property(self):
        property_name = input("Enter the property name: ")
        property = RentalProperty(property_name)
        self.properties[property_name] = property

    def calculate_rental_income(self, property_name):
        if property_name in self.properties:
            property = self.properties[property_name]
            total_income = property.calculate_rental_income()
            print(f"Total rental income per month for property '{property_name}': ${total_income:.2f}")
        else:
            print(f"Property '{property_name}' not found.")

    def remove_property(self, property_name):
        if property_name in self.properties:
            del self.properties[property_name]
            print(f"Property '{property_name}' removed.")
        else:
            print(f"Property '{property_name}' not found.")

    def run(self):
        print("Welcome to the Rental Income Calculator!")
        while True:
            print("Please choose an option:")
            print("1. Add Property")
            print("2. Calculate Rental Income")
            print("3. Remove Property")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_property()
            elif choice == '2':
                property_name = input("Enter the property name: ")
                self.calculate_rental_income(property_name)
            elif choice == '3':
                property_name = input("Enter the property name: ")
                self.remove_property(property_name)
            elif choice == '4':
                print("Thank you for using the Rental Income Calculator!")
                break
            else:
                print("Invalid choice. Please choose again.")


# Create an instance of the RentalIncomeCalculator class
calculator = RentalIncomeCalculator()

# Run the calculator
calculator.run()