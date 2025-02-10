import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a, b;
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        bw.append(String.format("%d", a * b));
        bw.flush();
        bw.close();
    }
}