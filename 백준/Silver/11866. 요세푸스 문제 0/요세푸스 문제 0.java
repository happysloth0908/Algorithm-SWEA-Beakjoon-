
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		Queue<Integer> que = new LinkedList<>();
		
//		int arr [] = new int [N];
		for (int i = 1; i <= N; i++) {
//			arr[i] = i + 1; // 0 ~ N - 1 인덱스에 1 ~ N 까지 숫자를 넣음
			que.offer(i); //1 ~ N 까지 숫자를 넣음
		}
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		while(que.size() != 1) {
			for( int i = 0; i < K - 1; i++ ) {
				que.offer(que.poll());
			}
			sb.append(que.poll() + ", ");
		}
		sb.append(que.poll() + ">");
		System.out.println(sb);
		
		
	}
}
