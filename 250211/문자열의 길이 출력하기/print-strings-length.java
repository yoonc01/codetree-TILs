import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        String a, b;

        st = new StringTokenizer(br.readLine());
        a = st.nextToken();
        st = new StringTokenizer(br.readLine());
        b = st.nextToken();
        int len = a.length() + b.length();
        sb.append(String.valueOf(len));
        bw.write(sb.toString());
        bw.close();  
    }
}