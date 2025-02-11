import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine(), "- ");
        int m, d, y;
        m = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        
        bw.append(String.format("%d.%d.%d\n", y, m, d));
        bw.flush();
        bw.close();
    }
}