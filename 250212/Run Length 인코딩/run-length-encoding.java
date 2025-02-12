import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine();
        int idx = 0;
        int n = str.length();

        while (idx < n) {
            char current = str.charAt(idx);
            int count = 0;
            while (idx < n && str.charAt(idx) == current) {
                idx++;
                count++;
            }
            sb.append(current).append(String.valueOf(count));
        }
        bw.append(String.valueOf(sb.toString().length())).append("\n").append(sb.toString());
        bw.close();
    }
}