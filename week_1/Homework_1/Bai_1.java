

public class Bai_1 {

    public static int gcd(int a, int b)
    {
        if (a == 0) {
            return b;
        }else if (b == 0) return a;
        if(a > b){
            return gcd(a%b, b);
        }else return gcd(b%a, a);
    }

    public static void main(String[] args)
    {
        int a = 10, b = 15, g;
        g = gcd(a, b);
        System.out.println("UCLN cua " + a +  " va  " + b+ " la: " + g);

        a = 35; b = 10;
        g = gcd(a, b);
        System.out.println("UCLN cua " + a +  " va  " + b+ " la: " + g);

        a = 2; b = 32;
        g = gcd(a, b);
        System.out.println("UCLN cua " + a +  " va  " + b+ " la: " + g);

    }
}
