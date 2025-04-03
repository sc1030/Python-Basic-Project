'''weight = float(input("Enter Weight (KG): "))
height = float(input("Enter Height (m): "))
bmi = weight / (height ** 2)
print(f"Your BMI: {bmi:.2f}")
'''

from typing import Tuple, Optional

class BMICalculator:
    def __init__(self):
        self.bmi_categories = {
            (0, 18.5): "Underweight",
            (18.5, 25): "Normal weight",
            (25, 30): "Overweight",
            (30, float('inf')): "Obese"
        }
    
    def get_valid_input(self, prompt: str, min_val: float) -> float:
        """Get and validate numeric input"""
        while True:
            try:
                value = float(input(prompt))
                if value <= min_val:
                    print(f"Value must be greater than {min_val}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number")
    
    def calculate_bmi(self, weight: float, height: float) -> float:
        """Calculate BMI from weight and height"""
        return weight / (height ** 2)
    
    def get_bmi_category(self, bmi: float) -> str:
        """Determine BMI category"""
        for (min_val, max_val), category in self.bmi_categories.items():
            if min_val <= bmi < max_val:
                return category
        return "Unknown"
    
    def convert_units(self, weight_kg: float, height_m: float) -> Tuple[float, float]:
        """Convert metric units to imperial"""
        weight_lbs = weight_kg * 2.20462
        height_in = height_m * 39.3701
        return weight_lbs, height_in

def main():
    calculator = BMICalculator()
    
    print("Welcome to BMI Calculator")
    print("-------------------------")
    
    while True:
        # Get validated input
        weight = calculator.get_valid_input("Enter weight (kg): ", 0)
        height = calculator.get_valid_input("Enter height (m): ", 0)
        
        # Calculate BMI
        bmi = calculator.calculate_bmi(weight, height)
        
        # Get category
        category = calculator.get_bmi_category(bmi)
        
        # Convert to imperial units
        weight_lbs, height_in = calculator.convert_units(weight, height)
        
        # Display results
        print("\nResults:")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print(f"Weight: {weight:.1f} kg ({weight_lbs:.1f} lbs)")
        print(f"Height: {height:.2f} m ({height_in:.1f} inches)")
        
        # Health information
        print("\nBMI Categories:")
        for (min_val, max_val), cat in calculator.bmi_categories.items():
            if max_val == float('inf'):
                print(f"{cat}: {min_val}+")
            else:
                print(f"{cat}: {min_val} - {max_val}")
        
        # Ask to calculate again
        again = input("\nCalculate another BMI? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using BMI Calculator!")
            break
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    main()