import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        String arr[] = new String[10];
        for (int i = 0; i < 10; i++)
            arr[i] = st.nextToken();
        for (int i = 0; i < 10; i++)
            bw.append(arr[9 - i]);
        bw.flush();
        bw.close();

    }
}