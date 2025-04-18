import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num;
        num = Integer.parseInt(st.nextToken());
        bw.write(String.format("Your score is %d point.\n", num));
        bw.flush();
        bw.close();
    }
}