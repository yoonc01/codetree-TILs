import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int a, b;

        st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        b = Integer.parseInt(st.nextToken());

        bw.append(String.format("%d\n", a * b));
        bw.flush();
        bw.close();
    }
}