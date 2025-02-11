import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int h, m;
        st = new StringTokenizer(br.readLine(), ": ");
        h = Integer.parseInt(st.nextToken());
        h++;
        m = Integer.parseInt(st.nextToken());
        bw.append(String.format("%d:%d\n", h, m));
        bw.flush();
        bw.close();
    }
}