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
