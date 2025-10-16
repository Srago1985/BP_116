package com.example;

public class Main {
    public static void main(String[] args) {
        int arr[] = {9, 2, 5, 1, -2, 7};
        com.example.Homework.printArray(arr);        
        System.out.println(com.example.Homework.arrayEvensSum(arr));
        System.out.println(com.example.Homework.arraySumInRange(arr, 1, 4));
        com.example.Homework.reverseArray(arr);
    }
}
