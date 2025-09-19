package com.example;

public class Homework {
    public static int factorial(int n) {
        if (n < 0) {
            return -1; // Error case for negative input
        }
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result = result * i;
        }
        return result;
    }

    public static void printStars(int stars, int inRow){
        for (int i = 1; i <= stars; i++) {
            System.out.print("*");
            if (i % inRow == 0) {
                System.out.println();
            }
        }
        if (stars % inRow != 0) {
            System.out.println();
        }
    }

    public static boolean hasDigit(int number,int digit) {
        if (digit < 0 || digit > 9) {
            return false; // Invalid digit
        }
        if (number == digit ) {
            return true; 
        }
        number = Math.abs(number); // Handle negative numbers
        while (number != 0) {
            int currentDigit = number % 10;
            if (currentDigit == digit) {
                return true;
            }
            number = number / 10;
        }
        return false;
    }
/* with reverse*/
    public static void printNumberInColumn(int number) {
        
        if (number == 0) {
            System.out.println(0);
            return;
        }
        if (number < 0) {
            System.out.println("-");
            number = Math.abs(number);
        }
        int reversed = 0;
        int original = number;
        while (number != 0) {
            int digit = number % 10;
            reversed = reversed * 10 + digit;
            number = number / 10;
        }
        while (reversed != 0) {
            int digit = reversed % 10;
            System.out.println(digit);
            reversed = reversed / 10;
        }
        // Handle trailing zeros in the original number
        int temp = original;
        while (temp % 10 == 0) {
            System.out.println(0);
            temp = temp / 10;
        }       
    }
    /*without reverse*/
    public static void printNumberInColumnWithoutReverse(int number) {
        if (number == 0) {
            System.out.println(0);
            return;
        }
        if (number < 0) {
            System.out.println("-");
            number = Math.abs(number);
        }
        int divisor = 1;
        while (number / divisor >= 10) {
            divisor *= 10;
        }
        while (divisor > 0) {
            int digit = number / divisor;
            System.out.println(digit);
            number = number % divisor;
            divisor = divisor / 10;
        }
    }

}
