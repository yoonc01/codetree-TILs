import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine();
        int n = str.length();
        int idx = 0;

        while (idx < n) {
            char current = str.charAt(idx);
            int count = 0;

            while (idx < n && str.charAt(idx) == current) {
                idx++;
                count++;
            }

            sb.append(current).append(count);
        }
        sb.insert(0, sb.length() + "\n");
        bw.append(sb.toString());

        bw.flush();
        bw.close();
    }
}
