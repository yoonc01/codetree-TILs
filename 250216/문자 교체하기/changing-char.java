import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        String str1, str2;

        str1 = st.nextToken();
        str2 = st.nextToken();
        
        sb.append(str1.substring(0, 2)).append(str2.substring(2));
        System.out.println(sb.toString()); 
    }
}