public class MainTypesPrint {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        int num = 42;
        double d = 3.14;
        boolean flag = true;
        char c = 'A'; 
        System.out.println("Integer: " + num);
        System.out.println("Double: " + d);
        System.out.println("Boolean: " + flag);
        System.out.println("Character: " + c);
        System.out.printf("Formatted output: %d, %.1f, %b, %c%n \n", num, d, flag, c); // \n - new line
    }
}