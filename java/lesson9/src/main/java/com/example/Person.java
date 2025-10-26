package com.example;

public class Person {
    private String name;
    private double age;
    private int ID;

    public Person(String n, double a, int i) {
        setName(n);
        setAge(a);
        setID(i);
        System.out.println("Person object created");
    }

    public void setName(String n) {
        name = n;
    }

    public void setAge(double a) {
        if (a > 0) {
            age = a;
        } else {
            System.out.println("Invalid age");
        }
    }

    public void setID(int i) {
        if (i > 0) {
            ID = i;
        } else {
            System.out.println("Invalid ID");
        }
    }

    public String getName() {
        return name;
    }

    public double getAge() {
        return age;
    }

    public int getID() {
        return ID;
    }
}
