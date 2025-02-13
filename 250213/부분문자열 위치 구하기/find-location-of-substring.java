import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String inputString = br.readLine();
        String targetString = br.readLine();

        System.out.println(inputString.indexOf(targetString));
    }
}