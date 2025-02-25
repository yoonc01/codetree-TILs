import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputSteamReader(System.in));
    static int n;

    static int count(int n) {
        if (n == 1)
            return 0;
        if (n % 2 == 0)
            return count(n / 2) + 1;
        return count(3 * n + 1) + 1;
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        System.out.println(count(n));
    }
}