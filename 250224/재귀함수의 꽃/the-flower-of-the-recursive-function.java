import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int n;

    static void printCnt(int n) {
        if (n == 0)
            return;
        sb.append(n).append(" ");
        printCnt(n - 1);
        sb.append(n).append(" ");
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        printCnt(n);
        System.out.println(sb);

    }
}