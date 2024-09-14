
import java.util.Scanner;

public class Main {
	static int MAX;
	static int N;
	static int[][] board;
	static int[] dr = {-1, 1, 0, 0};
	static int[] dc = {0, 0, -1, 1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		MAX = 1;
		N = sc.nextInt();
		board = new int[N][N];
		int maxWater = 0;
		int minWater = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				board[i][j] = sc.nextInt();
				if (board[i][j] > maxWater) maxWater = board[i][j];
				if (board[i][j] < minWater) minWater = board[i][j];
			}
		}
		/// 보드 완성
//		for (int i = 0; i < N; i++) {
//			for (int j = 0; j < N; j++) {
//				System.out.print(board[i][j]);
//			}
//			System.out.println();
//		}
//		System.out.println("maxWater = " + maxWater + " " + "minWater = " + minWater);
		////// 테스트용 코드 
		
		for (int i = minWater; i < maxWater; i++) {
			boolean[][] visited = new boolean[N][N];
			dfs(i, visited);
		}
		
		System.out.println(MAX);
		
		
	}
	
	public static void dfs(int wLevel, boolean[][] visited){
		int safePlace = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if ( wLevel < board[i][j] && !visited[i][j]) {
					DFS(i, j , visited, wLevel);
					safePlace++;
//					System.out.println(safePlace);
				}
			}
		}
		if (MAX < safePlace) MAX = safePlace;
	}

	private static void DFS(int i, int j, boolean[][] visited, int wLevel) {
//		for (int k = 0; k < N; k++) {
//			for (int k2 = 0; k2 < N; k2++) {
//				if (visited[k][k2]) {
//					System.out.print("v");
//				}else {
//					System.out.print(0);					
//				}
//			}
//			System.out.println();
//		}
//		System.out.println("-----------");
		/// 테스트용 출력
		
		visited[i][j] = true;
		
		for (int d = 0; d < 4; d++) {
			int nr = i + dr[d];
			int nc = j + dc[d];
			
			// 판 밖을 넘어가거나 이미 들린 곳이라면 패스 
			if (nc < 0 || nr < 0 || nc >= N || nr >= N || visited[nr][nc]) continue;
			
			if (board[nr][nc] > wLevel) {
				DFS(nr, nc, visited, wLevel);
			}
		}
		
	}
}
