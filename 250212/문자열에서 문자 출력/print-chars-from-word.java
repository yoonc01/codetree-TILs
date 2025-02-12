import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        for (int i = 0; i < str.length(); i++) {
            bw.append(str.charAt(i)).append("\n");
        }
        bw.close();
    }
}