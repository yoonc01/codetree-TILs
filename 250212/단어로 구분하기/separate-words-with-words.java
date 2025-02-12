import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        String str;
        for (int i = 0; i < 10; i++) {
            str = st.nextToken();
            sb.append(str).append("\n");
        }
        bw.append(sb.toString());
        bw.close();
        
    }
}