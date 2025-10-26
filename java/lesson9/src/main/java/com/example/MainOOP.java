package com.example;

public class MainOOP {
    public static void main(String[] args) {
        Person person1 = new Person();
        // person1.name = "Alice";
        // person1.age = 30;
        // person1.ID = 3752165;
        person1.setName("Alice");
        person1.setAge(30);
        person1.setID(3752165);
        System.out.println("Person 1:");
        System.out.println("Name: " + person1.getName());
        System.out.println("Age: " + person1.getAge());
        System.out.println("ID: " + person1.getID());

        Person person2 = new Person();
        // person2.name = "Bob";
        // person2.age = 25.5;
        // person2.ID = 4827391;
        person2.setName("Bob");
        person2.setAge(25.5);
        person2.setID(4827391);
        System.out.println("Person 2:");
        System.out.println("Name: " + person2.getName());
        System.out.println("Age: " + person2.getAge());
        System.out.println("ID: " + person2.getID());
    }
}
