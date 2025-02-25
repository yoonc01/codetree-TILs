import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;

    public static int getSquareTotal(int n) {
        if (n < 10)
            return n * n;
        int digit = n % 10;
        return getSquareTotal(n / 10) + digit * digit;
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        System.out.println(getSquareTotal(n));
    }
}