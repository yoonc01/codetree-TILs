import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;

    static int untilOne(int n) {
        if (n == 1)
            return 0;
        if (n % 2 == 0)
            return untilOne(n / 2) + 1;
        return untilOne(n / 3) + 1;
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        System.out.println(untilOne(n));
    }
}