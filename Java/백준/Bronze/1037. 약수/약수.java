import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collection;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 제일 큰 수와 제일 작은 수 곱하면 됨.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        PriorityQueue<Integer> pqr = new PriorityQueue<>((a,b) -> b-a);
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(st.nextToken());
            pq.add(a);
            pqr.add(a);
        }
        int a = pq.poll();
        int b = pqr.poll();
        System.out.println(a * b);
    }
}
