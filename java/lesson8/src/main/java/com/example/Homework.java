package com.example;

public class Homework {
    public static int findMax(int[] arr) {
        int max = arr[0];
        for (int el : arr) {
            if (el > max) {
                max = el;
            }
        }
        return max;
    }

    public static boolean minToEnd(int[] arr) {
        if (arr == null || arr.length == 0) {
            return false;
        }
        int minIndex = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[minIndex]) {
                minIndex = i;
            }
        }
        return minIndex == arr.length - 1;
    }

    public static int[] moveMinToEnd(int[] arr) {
        if (arr == null) return null;
        if (arr.length == 0) return arr;
        int minIndex = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[minIndex]) {
                minIndex = i;
            }
        }
        int minValue = arr[minIndex];
        for (int i = minIndex; i < arr.length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr[arr.length - 1] = minValue;
        System.out.println("Array after moving minimum to end: ");
        for (int el : arr) {
            System.out.print(el + " ");
        }
        return arr;
    }

    public static boolean evenToEnd(int[] arr) {
        if (arr == null || arr.length == 0) {
            return false;
        }
        int left = 0;
        int right = arr.length - 1;
        while (left < right) {
            while (left < right && arr[left] % 2 != 0) {
                left++;
            }
            while (left < right && arr[right] % 2 == 0) {
                right--;
            }
            if (left < right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
        return true;
    }

    public static boolean minToMax(int[] arr) {
        if (arr == null || arr.length == 0) {
            return false;
        }
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            if (arr[left] % 2 == 0) {
                left++;
            } else if (arr[right] % 2 != 0) {
                right--;
            } else {
                int tmp = arr[left];
                arr[left] = arr[right];
                arr[right] = tmp;
                left++;
                right--;
            }
        }

        int evCount = left; // количество чётных в начале

        // сортировка чётной части 
        for (int i = 0; i < evCount - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < evCount; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            if (minIdx != i) {
                int tmp = arr[i];
                arr[i] = arr[minIdx];
                arr[minIdx] = tmp;
            }
        }

        // сортировка нечетной части 
        for (int i = evCount; i < arr.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIdx]) minIdx = j;
            }
            if (minIdx != i) {
                int tmp = arr[i];
                arr[i] = arr[minIdx];
                arr[minIdx] = tmp;
            }
        }

        return true;
    }
}
