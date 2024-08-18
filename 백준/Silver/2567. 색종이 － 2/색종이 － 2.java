

import java.util.Scanner;

public class Main {

	public static int N = 100; // 보드 가로 세로 길이

	public static int[] dr = { -1, 0, 1, 0 };
	public static int[] dc = { 0, 1, 0, -1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[][] board = new int[N][N];

		int pnum = sc.nextInt();
		for (int t = 0; t < pnum; t++) {
			int r = sc.nextInt();
			int c = sc.nextInt();

			for (int i = r; i < r + 10; i++) { // 색종이 있는 부분 다 1로 바꿈
				for (int j = c; j < c + 10; j++) {
					board[i][j] = 1;
				}
			}
		}

		int sum = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] == 1) { // 1이면 사방 탐색 시작
					for (int d = 0; d < 4; d++) {
						int nr = i + dr[d];
						int nc = j + dc[d];
						if (nc >= N || nr >= N || nc < 0 || nr < 0) {
							sum++;
							continue;
						}
						if ( board[nr][nc] == 0) {
							sum++;
						}

					}
				}
			}
		}
		System.out.println(sum);

	}
}
