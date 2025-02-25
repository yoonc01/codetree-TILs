import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n;

    public static int getTotal(int n) {
        if (n == 1)
            return 1;
        return getTotal(n - 1) + n;
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        System.out.println(getTotal(n));
    }
}