package com.example;

public class LoopMethods {
    public static void printStars(int stars) {
        for (int i = 0; i < stars; i++) {
            System.out.print("*");
        }
        System.out.println();
    }

    public static void printStars2(int stars) {
        int i = 0;
        while (i < stars) {
            System.out.print("*");
            i++;
        }
        System.out.println();
    }

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

    public static int digitsCount(int n) {
        if (n == 0) {
            return 1; // Special case for 0
        }
        int count = 0;
        while (n != 0) {
            n = n / 10;
            count++;
        }
        return count;
    }
}
