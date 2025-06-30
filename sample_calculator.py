#!/usr/bin/env python3
"""
Simple Calculator with Error Handling
Created as part of the Warp Tutorial

This calculator demonstrates:
- Basic arithmetic operations
- Error handling for division by zero
- Input validation
- User-friendly interface
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract second number from first"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide first number by second with zero-division protection"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    """Get a valid operation from user"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in operations:
            return operations[op]
        print("Please enter a valid operation (+, -, *, /)")

def main():
    """Main calculator loop"""
    print("Welcome to the Warp Tutorial Calculator!")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Check if user wants to quit
            first_input = input("\nEnter first number (or 'quit'): ").strip()
            if first_input.lower() == 'quit':
                print("Goodbye!")
                break
                
            # Get first number
            first_num = float(first_input)
            
            # Get operation
            operation = get_operation()
            
            # Get second number
            second_num = get_number("Enter second number: ")
            
            # Perform calculation
            result = operation(first_num, second_num)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
