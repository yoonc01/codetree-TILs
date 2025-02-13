import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        
        String str = br.readLine();

        String ee = str.contains("ee") ? "Yes" : "No";
        String ab = str.contains("ab") ? "Yes" : "No";

        sb.append(ee).append(" ").append(ab);
        bw.write(sb.toString());
        bw.close();
    }
}