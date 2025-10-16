package com.example;

public class MainArraysTest {
    public static void main(String[] args) {
        int [] arr = {5, 23, 7, 10, -2, 6};
        for (int i : arr) {
            System.out.print(i + " ");
        }

        System.out.println();

        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }

        System.out.println();

        printArray(arr);
    }

    public static void printArray(int[] array) {
        for (int el : array) {
            if (el % 2 == 0) {
                System.out.print(el + " ");
            }
        }
        System.out.println();
    }
}
