package com.example;

public class tank {
    public static void tankOnMines(int [] arr) {
        int tankHealth = 2;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 1) {
                System.out.println("Tank exploded on mine at index: " + i);
                System.out.println("1 HP was lost");
                tankHealth--;
                if (tankHealth == 0) {
                    System.out.println("Tank is destroyed.");
                    return;
                }
            }
        }
        System.out.println("Tank passed safely.");
    }
}
