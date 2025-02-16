import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        char[] strArray = str.toCharArray();
        strArray[1] = 'a';
        strArray[strArray.length - 2] = 'a';

        System.out.println(String.valueOf(strArray));
    }
}