import java.io.*;
import java.util.*;

public class Main {
    static int gcd(int n, int m) {
        if (m == 0)
            return n;
        return gcd(m, n % m);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n, m;

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        System.out.println(gcd(n, m));
    }
}