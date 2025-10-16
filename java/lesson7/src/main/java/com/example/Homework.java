package com.example;

public class Homework {

    public static void printArray(int[] arr) {        
        for (int el : arr) {
            System.out.print(el + " ");
        }
        System.out.println();
    }
    
    public static int arrayEvensSum(int[] arr) {
        int sum = 0;
        for (int el : arr) {
            if (el % 2 == 0) {
                sum += el;
            }
        }
        return sum;
    }

    public static int arraySumInRange(int[] arr, int start, int end) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            if (i >= start && i <= end) {
                sum += arr[i];
            }
        }
        return sum;       
    }

    public static void reverseArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n / 2; i++) {
            int temp = arr[i];
            arr[i] = arr[n - 1 - i];
            arr[n - 1 - i] = temp;
        }
        System.out.print("Reversed array: ");
        printArray(arr);
    }
}
