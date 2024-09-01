
import java.util.Scanner;

public class Main {
	static int N ;
	static int [] arr ;
	static boolean[] visited ;
	static int [] result ;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		arr = new int[N];
		visited = new boolean[N];
		result = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = i + 1;
		}	
		perm(0);
	}

	private static void perm(int idx) {
		if (idx == N) {
			for (int i = 0; i < N; i++) {
				System.out.print(result[i] + " ");				
			}
			System.out.println();
			return;
		}
		for (int i = 0; i < N; i++) {
			if (visited[i]) continue;
			
			result[idx] = arr[i];
			
			visited[i] = true;
			perm(idx + 1);
			visited[i] = false;
		}
		
		
	}
	
}
