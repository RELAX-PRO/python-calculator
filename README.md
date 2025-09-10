# Python Calculator

A simple command-line calculator application written in Python that performs basic arithmetic operations.

## Description

This Python calculator provides an interactive command-line interface for performing basic mathematical operations. It supports addition, subtraction, multiplication, and division operations, and allows users to continue calculations using previous results or start fresh calculations.

## Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Interactive Interface**: User-friendly command-line prompts
- **Continuous Calculations**: Option to continue with the last result or start a new calculation
- **Error Handling**: Handles invalid operations through dictionary-based operation mapping
- **Floating Point Support**: Works with decimal numbers

## Requirements

- Python 3.x (tested with Python 3.12.3)
- No external dependencies required

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RELAX-PRO/python-calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd python-calculator
   ```

3. Run the calculator:
   ```bash
   python3 1.python_calc.py
   ```

## Usage

### Starting the Calculator

Run the calculator script:
```bash
python3 1.python_calc.py
```

### Basic Operations

The calculator will prompt you for:
1. **First number**: Enter any numeric value (integers or decimals)
2. **Operation**: Choose from '+', '-', '*', or '/'
3. **Second number**: Enter the second numeric value

### Example Session

```
Welcome to the python calculator .
Insert the first number : 10
Enter the operation : '+','-','*','/'.+
Insert the second number : 5
The result is 15.0 

Do you want to continue on the last result or try again from the begining.'y','n'y
Enter the operation.'+','-','*','/'*
Enter the second number : 2
The result is 30.0
```

### Continuing Calculations

After each calculation, you can:
- **Continue with last result**: Type 'y' to use the previous result as the first number
- **Start fresh**: Type 'n' to enter a completely new calculation

### Supported Operations

| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | + | 5 + 3 = 8 |
| Subtraction | - | 10 - 4 = 6 |
| Multiplication | * | 7 * 2 = 14 |
| Division | / | 15 / 3 = 5 |

## Code Structure

The calculator uses a function-based approach:

- `add(a, b)`: Performs addition
- `subtract(a, b)`: Performs subtraction  
- `multiply(a, b)`: Performs multiplication
- `divide(a, b)`: Performs division
- `operations`: Dictionary mapping operation symbols to functions

## Limitations

- Division by zero will cause a runtime error
- Invalid operation symbols will cause a KeyError
- Non-numeric input will cause a ValueError
- The program runs in an infinite loop until manually terminated

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Future Enhancements

Potential improvements for this calculator:
- Error handling for division by zero
- Input validation for operations and numbers
- Support for more advanced operations (power, square root, etc.)
- Memory functions (store/recall)
- History of calculations
- Exit option for the main loop

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please open an issue in this repository.