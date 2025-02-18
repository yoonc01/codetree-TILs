import java.util.*;
import java.io.*;

public class Main {
    public static void printRect(StringBuilder sb, int n) {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(cnt + 1).append(" ");
                cnt = (cnt + 1) % 9;
            }
            sb.append("\n");
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        printRect(sb, n);
        System.out.println(sb);
    }
}