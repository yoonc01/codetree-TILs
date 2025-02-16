import java.util.*;
import java.io.*;

public class Main {
    static void swap(char strArray[], int a, int b) {
        char temp = strArray[a - 1];
        strArray[a - 1] = strArray[b - 1];
        strArray[b - 1] = temp;
    }

    static void change(char strArray[], char a, char b) {
        for (int i = 0; i < strArray.length; i++) {
            if (strArray[i] == a)
                strArray[i] = b;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        char strArray[];

        st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        strArray = s.toCharArray();
        int q = Integer.parseInt(st.nextToken());

        while(q-- > 0) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());

            if (cmd == 1) {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                swap(strArray, a, b);
            } else {
                char a = st.nextToken().charAt(0);
                char b = st.nextToken().charAt(0);
                change(strArray, a, b);
            }
            sb.append(strArray).append("\n");
        }
        System.out.print(sb);
    }
}