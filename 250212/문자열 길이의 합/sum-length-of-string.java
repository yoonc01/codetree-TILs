import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int totalLen = 0, countStartsWithA = 0;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            totalLen = totalLen + str.length();
            if (str.charAt(0) == 'a') countStartsWithA++;
        }
        sb.append(String.valueOf(totalLen)).append(" ").append(String.valueOf(countStartsWithA));
        bw.append(sb.toString());
        bw.close();
    }
}