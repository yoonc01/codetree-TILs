import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int val, sum = 0;

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 10; i++) {
            val = Integer.parseInt(st.nextToken());
            sum = sum + val;
        }
        bw.append(String.valueOf(sum));
        bw.flush();
        bw.close();
    }
}