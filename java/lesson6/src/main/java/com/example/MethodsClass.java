package com.example;

public class MethodsClass {
    public static void printFigure(int i, int j) {
        for ( ; j > 0; j--) {
            for ( ; i > 0; i--) {
            System.out.print("*");
            }
            System.out.println("");
        }
    }
}
// why inner loops do not work? Because the loop variables i and j are not being initialized properly. how to fix it?