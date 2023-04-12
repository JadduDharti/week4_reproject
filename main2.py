class RentalProperty:
    def __init__(self, property_name, rent_amount, occupancy_rate, expenses):
        self.property_name = property_name
        self.rent_amount = rent_amount
        self.occupancy_rate = occupancy_rate
        self.expenses = expenses

    def calculate_total_income(self):
        total_income = (self.rent_amount * self.occupancy_rate / 100) - self.expenses
        return total_income


class RentalIncomeCalculator:
    def __init__(self):
        self.properties = []

    def add_property(self):
        property_name = input("Enter property name: ")
        rent_amount = float(input("Enter the rent amount per month: "))
        occupancy_rate = float(input("Enter the occupancy rate (in percentage): "))
        expenses = float(input("Enter the total expenses per month: "))
        property = RentalProperty(property_name, rent_amount, occupancy_rate, expenses)
        self.properties.append(property)
        print("Property added successfully!")

    def view_properties(self):
        print("Properties:")
        for i, property in enumerate(self.properties, 1):
            print(f"{i}. {property.property_name}")

    def calculate_total_income(self):
        total_income = 0
        for property in self.properties:
            total_income += property.calculate_total_income()
        return total_income

    def run(self):
        print("Welcome to the Rental Income Calculator!")
        while True:
            print("Please choose an option:")
            print("1. Add Property")
            print("2. View Properties")
            print("3. Calculate Total Income")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_property()
            elif choice == '2':
                self.view_properties()
            elif choice == '3':
                total_income = self.calculate_total_income()
                print(f"Total rental income across properties per month: ${total_income:.2f}")
            elif choice == '4':
                print("Thank you for using the Rental Income Calculator!")
                break
            else:
                print("Invalid choice. Please choose again.")


# Create an instance of the RentalIncomeCalculator class
calculator = RentalIncomeCalculator()

# Run the calculator
calculator.run()