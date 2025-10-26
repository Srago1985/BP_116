package com.example;

public class Car {
    private String model;
    private int year;
    private String color;

    public Car(String m, int y, String c) {
        setModel(m);
        setYear(y);
        setColor(c);
        System.out.println("Car object created");
    }

    public void setModel(String m) {
        model = m;
    }

    public void setYear(int y) {
        if (y > 1885) { // The first car was invented around 1886
            year = y;
        } else {
            System.out.println("Invalid year");
        }
    }

    public void setColor(String c) {
        color = c;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    public String getColor() {
        return color;
    }
}
