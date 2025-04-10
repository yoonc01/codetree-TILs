import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        double d;

        d = Double.parseDouble(st.nextToken());
        bw.write(String.format("%.1f\n", d * 30.48));
        bw.flush();
        bw.close();
    }
}