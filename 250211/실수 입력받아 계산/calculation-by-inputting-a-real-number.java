import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        double a, b;
        
        st = new StringTokenizer(br.readLine());
        a = Double.parseDouble(st.nextToken());

        st = new StringTokenizer(br.readLine());
        b = Double.parseDouble(st.nextToken());

        bw.append(String.format("%.2f", a + b));
        bw.flush();
        bw.close();
    }
}