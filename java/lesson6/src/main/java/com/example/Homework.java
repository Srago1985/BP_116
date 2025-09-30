package com.example;

public class Homework {
    public static void printMagenDavid(int size) {
        if (size < 6) {
            System.out.println("Size should be at least 6");
            return;        
        }
        if (size / 6 != 0) {
            size = Math.round(size / 6.0f) * 6;
            System.out.println("For optimal proportions, size adjusted to " + size);
            System.out.println(" ");
        }
        for (int i = 0; i <= size * 2 / 3; i++) {
            for (int j = 0; j <= size; j++) {
                if (
                    (j == size / 2 && (i == 0 || i == size * 2 / 3)) ||
                    (i == size / 6 || i == size / 2) && (j == size || j == size * 2 / 3 || j == size / 3 || j == 0) ||
                    (i == size / 3 && (j == size / 6 || j == size * 5 / 6))
                ) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    public static int oddsCountWithFor(int number) {
        int count = 0;
        for (int i = number; i != 0; i /= 10) {
            int digit = i % 10;
            if (digit % 2 != 0) {
                count++;
            }
        }
        return count;
    }

    public static int oddsCountWithWhile(int number) {
        int count = 0;
        int i = number;
        while (i != 0) {
            int digit = i % 10;
            if (digit % 2 != 0) {
                count++;
            }
            i /= 10;
        }
        return count;
    }

    public static void printNumberReverseWithFor(int number) {
        for (int i = number; i != 0; i /= 10) {
            int digit = i % 10;
            System.out.print(digit);
        }
        System.out.println();
    }

    public static void printNumberReverseWithWhile(int number) {
        int i = number;
        while (i != 0) {
            int digit = i % 10;
            System.out.print(digit);
            i /= 10;
        }
        System.out.println();
    }

    public static boolean hasNumber(int number, int sub) {
        if (sub < 0 || number < 0) {
            sub = Math.abs(sub);
            number = Math.abs(number);
        }
        int subLength = 0;
        int tempSub = sub;
        while (tempSub != 0) {
            subLength++;
            tempSub /= 10;
        }

        int divisor = (int) Math.pow(10, subLength);
        int tempNumber = number;

        while (tempNumber != 0) {
            if (tempNumber % divisor == sub) {
                return true;
            }
            tempNumber /= 10;
        }
        return false;
    }

    public static boolean hasNumberString(int number, int sub) {
        String numberStr = Integer.toString(number);
        String subStr = Integer.toString(sub);
        return numberStr.contains(subStr);
    }

    public static void printSquareWithHoles(int size) {
        if (size < 5) {
            System.out.println("Size should be at least 5");
            return;
        }
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                
                if ((i == size * .2 && (j == size * .4 || j == size * .6)) || (i == size * .4 && j == size * .6)) {
                    System.out.print(" ");                    
                }
                else {
                    System.out.print("*");
                }
            }
            System.out.println();
        }
    }

    public static void printFullTriangle(int size) {
        if (size < 1) {
            System.out.println("Size should be at least 1");
            return;
        }
        for (int i = 0; i < size; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void printSquareWithM(int size) {
        if (size < 5) {
            System.out.println("Size should be at least 5");
            return;
        }
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                
                if ((i == size * .2 && j == size * .4) || (i == size * .4 && (j == size * .6 || j == size * .2)))  {
                    System.out.print(" ");                    
                }
                else {
                    System.out.print("*");
                }
            }
            System.out.println();
        }
    }

    public static void printEmptyIsoscalesTriangle(int size) {
        if (size < 3 || size % 2 == 0) {
            System.out.println("Size should be an odd number and at least 3");
            return;
        }
        int middle = size / 2 + 1;
        for ( int i = 0; i < middle; i++) {
            for ( int j = 0; j < size; j++) {

                if (j == middle - i - 1 || j == middle + i - 1 || i == middle - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    public static void printMultiplicationTable(int size) {
        if (size < 1) {
            System.out.println("Size should be at least 1");
            return;
        }
        for (int i = 1; i <= size; i++) {
            for (int j = 1; j <= size; j++) {
                System.out.print(i + "*" + j + "=" + (i * j) + "\t");
            }
            System.out.println();
        }
    }
}