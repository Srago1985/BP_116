package com.example;

public class ArrayMethods {
    public static int arrayOddsSum(int[] array) {
        int sum = 0;
        for (int el : array) {
            if (el % 2 != 0) {
                sum += el;
            }
        }
        return sum;
    }

    public static void printArrayStrReverse(String[] arrayStr) {
        for (int i = arrayStr.length - 1; i >= 0; i--) {
            System.out.print(arrayStr[i] + " ");
        }   
        System.out.println();
    }

    public static void fillArrayEvens(int[] array) {
        int start = 2;
        for (int i = 0; i < array.length; i++) {
            array[i] = start;
            start += 2;
        }
    }

}
