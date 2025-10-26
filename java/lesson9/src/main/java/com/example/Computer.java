package com.example;

public class Computer {
    private String company;
    private int ram;
    private String os;
    private String cpu;

    public Computer(String company, int ram, String os, String cpu) {
        setCompany(company);
        setRam(ram);
        setOs(os);
        setCpu(cpu);
        System.out.println("Computer object created");
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public void setRam(int ram) {
        if (ram > 0) {
            this.ram = ram;
        } else {
            System.out.println("Invalid RAM size");
        }
    }

    public void setOs(String os) {
        this.os = os;
    }

    public void setCpu(String cpu) {
        this.cpu = cpu;
    }

    public String getCompany() {
        return company;
    }

    public int getRam() {
        return ram;
    }

    public String getOs() {
        return os;
    }

    public String getCpu() {
        return cpu;
    }
}
