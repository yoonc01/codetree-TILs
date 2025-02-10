import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(String.format("%d * %.6f = %.6f\n", 13, 0.165000, 13 * 0.165000));
        bw.flush();
        bw.close();
    }
}
