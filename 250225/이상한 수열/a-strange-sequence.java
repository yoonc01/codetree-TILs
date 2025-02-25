import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;

    static int seq(int n) {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;
        return seq(n / 3) + seq(n - 1);
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        System.out.println(seq(n));
    }
}