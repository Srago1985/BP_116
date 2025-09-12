public class Homework_MainMethods {
    public static void main(String[] args) {  
        double change = change(360, 400, 10);
        System.out.println("Change: " + change);
        fan(3);
    }

    public static double change(double total, double cash, double discount) {
        double discountedPrice = total - (total * discount / 100);
        double change = cash - discountedPrice;
        return change;
    }

    public static void fan(int mode) {
        switch (mode) {
            case 0:
                System.out.println("Fan is OFF");
                break;
            case 1:
                System.out.println("Speed 1");
                break;
            case 2:
                System.out.println("Speed 2");
                break;
            case 3:
                System.out.println("Turbo mode");
                break;
            default:
                System.out.println("ERROR");
        }
    }
}

