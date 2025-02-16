import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        char strArray[] = str.toCharArray();
        char first = strArray[0];
        char second = strArray[1];
        for (int i = 0; i < strArray.length; i++) {
            if (strArray[i] == first)
                strArray[i] = second;
            else if (strArray[i] == second)
                strArray[i] = first;
        }
        System.out.println(String.valueOf(strArray));
    }
}