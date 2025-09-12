public class MainJavaClass {
    public static void main(String[] args) {
        // taxi(3);
        double result = calculator(3, '/', 5);
        System.out.println("Calculator result: " + result);
    }

    // public static void taxi(int code) {
    //     if (code == 1) {
    //         System.out.println("Taxi A");
    //     } else if (code == 2) {
    //         System.out.println("Taxi B");
    //     } else if (code == 3) {
    //         System.out.println("Taxi C");
    //     } else {
    //         System.out.println("No such taxi");
    //     }
    // }

    public static double calculator(double a, char operation, double b) {
        double result = 0;
        switch (operation) {
            
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case '*':
                result = a * b;
                break;
            case '/':
                if (b == 0) {
                    System.out.println("Cannot divide by zero");                    
                }
                result = a / b;
                break;
            default:
                System.out.println("Unknown operation");
                
        }
        return result;
    }
}
