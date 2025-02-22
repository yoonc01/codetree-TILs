import java.io.*;
import java.util.*;

public class Main {
    static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    static int lcm(int a, int b) {
        return (a * b / gcd(a, b));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n, m;

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        System.out.println(lcm(a, b));
    }
}