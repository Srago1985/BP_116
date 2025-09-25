package com.example;

public class Homework {
    public static int digitsCount(int number) {
        if (number == 0) {
            return 1;
        }
        number = Math.abs(number);
        int count = 0;
        for (; number != 0; number /= 10, count++) {
            if (number < 10) {
                return count + 1;
            }            
        }
        return count;
    }
//using for loop
    public static int digitCount(int number, int digit) {
        if (digit < 0 || digit > 9) {
            return 0; // Invalid digit
        }
        number = Math.abs(number);
        int count = 0;
        for (; number != 0; number /= 10) {
            if (number % 10 == digit) {
                count++;
            }
            if (number < 10) {
                return count + (number == digit ? 1 : 0);
            }
        }
        return count;
    }
//using do-while loop
    public static int digitCountDoWhile(int number, int digit) {
        if (digit < 0 || digit > 9) {
            return 0; // Invalid digit
        }
        number = Math.abs(number);
        int count = 0;
        do {
            if (number % 10 == digit) {
                count++;
            }
            number /= 10;
        } while (number != 0);
        return count;
    }

//using for loop
    public static int evensSum(int number) {
        number = Math.abs(number);
        int sum = 0;
        for (; number != 0; number /= 10) {
            int digit = number % 10;
            if (digit % 2 == 0) {
                sum += digit;
            }
        }
        return sum;
    }
//using while loop
    public static int evensSumWhile(int number) {
        number = Math.abs(number);
        int sum = 0;
        while (number != 0) {
            int digit = number % 10;
            if (digit % 2 == 0) {
                sum += digit;
            }
            number /= 10;
        }
        return sum;
    }
}
