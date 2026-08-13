

A simple command-line calculator built in Python using object-oriented programming. It supports basic arithmetic as well as advanced operations (exponentiation, square root, logarithm), with error handling for invalid operations and non-numeric input.

# Advanced Calculator (OOP)

A simple calculator built in Python using object-oriented programming, run as a Jupyter/Colab notebook. It supports basic arithmetic as well as advanced operations (exponentiation, square root, logarithm), with error handling for invalid operations and non-numeric input.

## Features

- Basic operations: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`)
- Advanced operations: exponentiation (`^`), square root (`sqrt`), logarithm (`log`)
- Operations are stored in a dictionary, making it easy to register new ones dynamically via `add_operation()`
- Error handling for:
  - Invalid/unrecognized operation symbols
  - Non-numeric input
  - Division by zero
  - Invalid math operations (e.g. square root of a negative number, log of zero/negative numbers)
- Interactive loop that lets you run multiple calculations until you choose to exit

## Requirements

- Python 3.x (uses only the standard library — no extra installs needed)

## Usage

Open `basic-calculator.ipynb` in [Google Colab](https://colab.research.google.com/github/TeeMiles01/Data-Science-projects/blob/main/calculator-oop/basic-calculator.ipynb) or Jupyter Notebook, then run the cells from top to bottom.

You'll be prompted for an operation and the numbers involved:

## How It Works

The `Calculator` class stores operations in a dictionary (`self.operations`), mapping symbols like `+` or `sqrt` to their corresponding functions. New operations can be added at runtime with:

```python
calc.add_operation('^', exponentiate)
```

This design makes the calculator easy to extend — just write a function and register it, no need to modify the core class.

## License

Feel free to use, modify, and share this project.
