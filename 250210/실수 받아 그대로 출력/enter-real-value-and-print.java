import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        double number;
        
        number = Double.parseDouble(st.nextToken());

        bw.write(String.format("%.2f\n", number));
        bw.flush();
        bw.close();
    }
}