public class MainClass {
    public static void main(String[] args) {
        int res = add(5, 10);
        System.out.println("Result: " + res);
        double perc = percent(200, 50);
        System.out.println("Percentage: " + perc);
        double netSalary = salary(65.0, 180, 9.6);
        System.out.println("Net Salary:" + netSalary);
        double exchanged = exchange(1000, 3.5, 2.0);
        System.out.println("Exchanged: " + exchanged);
    }

    public static int add(int a, int b) {
        return a + b;
    }

    public static double percent(double total, double Percentage) {
        return total * (Percentage / 100);     
    }

    public static double salary(double wage, double hours, double taxInPercent) {
        double gross = wage * hours;
        return gross - (gross * (taxInPercent / 100));
    }

    public static double exchange(double nis, double rate, double commissionInPercent) {
        double exchanged = nis * rate;
        return exchanged - (exchanged * (commissionInPercent / 100));
    }
}
