package com.example;

public class HomeworkMethods {
    public static void isAlcoholPermit(int age) {
        if ((age < 18) && (age >= 0)) {
            System.out.println("not permit");
        } else if ((age >= 18) && (age <= 87)) {
            System.out.println("permit");
        } else if ((age > 87) && (age <= 120)) {
            System.out.println("permit with doctor approval");
        } else {
            System.out.println("incorrect age");
        }
    }

    public static void taxi(int driver) {
        switch (driver) {
            case 1:
                System.out.println("Alex, GO!");
                break;
            case 2:
                System.out.println("Hanna, GO!");
                break;
            case 3:
                System.out.println("Iossi, GO!");
                break;
            case 4:
                System.out.println("Ilan, GO!");
                break;
            default:
                System.out.println("ERROR");
                break;
        }
    }

    public static void printStars(int stars)
    {
        int i = 1;
        while (i <= stars) {
            System.out.print("*");
            i++;
        }
        System.out.println();
    }
}


