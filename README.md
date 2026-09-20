<div align="center">

  <h1>🧮 B.Tech Lab: Basic Calculator in C</h1>

  <p>
    <b>A lightweight, CLI-based calculator program written in C for standard arithmetic operations with input validation.</b>
  </p>

  <!-- Badges -->
  <p>
    <img src="https://img.shields.io/badge/Language-C-blue.svg?style=for-the-badge&logo=c" alt="Language C" />
    <img src="https://img.shields.io/badge/Compiler-GCC-green.svg?style=for-the-badge&logo=gnu" alt="Compiler GCC" />
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License MIT" />
  </p>

  <hr />

</div>

## 📌 Overview

This project is a simple command-line calculator developed as part of the **B.Tech Programming in C Laboratory**. It accepts two floating-point numbers and a mathematical operator from the user, executes the requested calculation, and displays the result formatted to two decimal places.

---

## ✨ Features

- ➕ **Addition (`+`)**: Adds two floating-point numbers.
- ➖ **Subtraction (`-`)**: Subtracts the second number from the first.
- ✖️ **Multiplication (`*`)**: Multiplies two numbers.
- ➗ **Division (`/`)**: Divides the first number by the second.
- 🛡️ **Error Handling**:
  - Prevents **division-by-zero** runtime errors with clear feedback.
  - Rejects **invalid operators** gracefully.
- ⚡ **Buffer Handling**: Uses whitespace-padded `%c` specifier in `scanf` to handle leftover newline characters seamlessly.

---

## 🛠️ Supported Operations

| Operator | Action | Example Output |
| :---: | :--- | :--- |
| **`+`** | Addition | `12.50 + 4.00 = 16.50` |
| **`-`** | Subtraction | `12.50 - 4.00 = 8.50` |
| **`*`** | Multiplication | `12.50 * 4.00 = 50.00` |
| **`/`** | Division | `12.50 / 4.00 = 3.12` |

---

## 📄 Code Snippet

Below is the complete C implementation for the project:

```c
#include <stdio.h>

int main() {
    float num1, num2, result;
    char op;

    printf("=========================================\n");
    printf("        B.TECH LAB: BASIC CALCULATOR     \n");
    printf("=========================================\n\n");

    printf("Enter first number: ");
    scanf("%f", &num1);

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &op); // Space before %c catches leftover newline

    printf("Enter second number: ");
    scanf("%f", &num2);

    printf("\n-----------------------------------------\n");

    switch (op) {
        case '+':
            result = num1 + num2;
            printf("Result: %.2f + %.2f = %.2f\n", num1, num2, result);
            break;
        case '-':
            result = num1 - num2;
            printf("Result: %.2f - %.2f = %.2f\n", num1, num2, result);
            break;
        case '*':
            result = num1 * num2;
            printf("Result: %.2f * %.2f = %.2f\n", num1, num2, result);
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                printf("Result: %.2f / %.2f = %.2f\n", num1, num2, result);
            } else {
                printf("Error: Division by zero is not allowed!\n");
            }
            break;
        default:
            printf("Error: Invalid operator entered.\n");
    }

    printf("-----------------------------------------\n");
    return 0;
}
🚀 Getting Started
Prerequisites
Ensure you have a C compiler installed on your system:

GCC (Linux / macOS / Windows via MinGW)

Clang (macOS / Linux)

📥 Compilation & Execution
Clone the Repository

Bash
git clone [https://github.com/your-username/btech-c-calculator.git](https://github.com/your-username/btech-c-calculator.git)
cd btech-c-calculator
Compile the C Program

Bash
gcc main.c -o calculator
Run the Binary

On Linux / macOS:

Bash
./calculator
On Windows:

DOS
calculator.exe
💻 Output Example
Plaintext
=========================================
        B.TECH LAB: BASIC CALCULATOR     
=========================================

Enter first number: 12.5
Enter an operator (+, -, *, /): *
Enter second number: 4

-----------------------------------------
Result: 12.50 * 4.00 = 50.00
-----------------------------------------
📁 Repository Structure
Plaintext
.
├── main.c        # Source code for the calculator
└── README.md     # Project documentation
