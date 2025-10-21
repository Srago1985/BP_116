package com.example;

public class Main {
    public static void main(String[] args) {
        int arr[] = {3, 5, 4, 7, 2, 8, -15, 0};
        // int max = com.example.Homework.findMax(arr);
        // System.out.println("Maximum value is: " + max);
        // System.out.println("Minimum value at the end: " + com.example.Homework.minToEnd(arr));        
        // com.example.Homework.moveMinToEnd(arr);
        // System.out.println();
        // com.example.Homework.evenToEnd(arr);
        //     for (int el : arr) {
        //         System.out.print(el + " ");
        //     }
        // System.out.println();

        com.example.Homework.minToMax(arr);
        for (int el : arr) {
            System.out.print(el + " ");
        }
    }
}