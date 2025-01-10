import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            StringBuilder sb = new StringBuilder();
            int m = Integer.parseInt(st.nextToken());
            String S = st.nextToken();
            for (int j = 0; j < S.length(); j++) {
                sb.append(String.valueOf(S.charAt(j)).repeat(m));
            }

            System.out.println(sb);
        }

    }
}
