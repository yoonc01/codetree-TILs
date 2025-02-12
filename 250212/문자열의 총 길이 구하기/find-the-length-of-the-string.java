import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int ans = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 10; i++)
        {
            String str = st.nextToken();
            ans = ans + str.length();
        }
        sb.append(String.valueOf(ans));
        bw.append(sb.toString());
        bw.close();
        
    }
}