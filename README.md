<div align="center">

  <h1>🧮 B.Tech Lab: Basic Calculator</h1>
  <p><strong>A simple, robust command-line calculator written in C for fundamental arithmetic operations.</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Language-C-blue.svg" alt="Language C" />
    <img src="https://img.shields.io/badge/Compiler-GCC-green.svg" alt="Compiler GCC" />
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License MIT" />
  </p>

</div>

<hr />

## 🚀 Overview

This repository contains a C program created for B.Tech laboratory assignments. It takes two float numbers and an operator from the user, then processes the calculation using a `switch-case` control structure.

---

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h3>➕ Core Arithmetic</h3>
      <ul>
        <li><strong>Addition (<code>+</code>)</strong></li>
        <li><strong>Subtraction (<code>-</code>)</strong></li>
        <li><strong>Multiplication (<code>*</code>)</strong></li>
        <li><strong>Division (<code>/</code>)</strong></li>
      </ul>
    </td>
    <td width="50%">
      <h3>🛡️ Built-in Safeguards</h3>
      <ul>
        <li><strong>Zero Division Prevention:</strong> Displays error message if second number is zero.</li>
        <li><strong>Input Validation:</strong> Handles unknown operator inputs gracefully.</li>
        <li><strong>Clean Formatting:</strong> Displays results rounded to 2 decimal places.</li>
      </ul>
    </td>
  </tr>
</table>

---

## 💻 Code Snippet

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
    scanf(" %c", &op); // Note the space before %c to catch leftover newline

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


🛠️ How to Build and Run
Prerequisites
A C compiler such as GCC or Clang.

Steps
Clone the repository:


git clone [https://github.com/your-username/repository-name.git](https://github.com/your-username/repository-name.git)
cd repository-name

gcc calculator.c -o calculator

# On Linux/macOS
./calculator

# On Windows
calculator.exe


=========================================
        B.TECH LAB: BASIC CALCULATOR     
=========================================

Enter first number: 12.5
Enter an operator (+, -, *, /): *
Enter second number: 4

-----------------------------------------
Result: 12.50 * 4.00 = 50.00
-----------------------------------------
