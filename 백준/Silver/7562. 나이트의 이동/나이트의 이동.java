

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	static int[] dr = { -2, -1, 1, 2, 2, 1, -1, -2 };
	static int[] dc = { 1, 2, 2, 1, -1, -2, -2, -1 };

	static int N; // 한 변의 길이
	static int[] start = new int[2];
	static int[] end = new int[2];

	static int[][] board;
	static boolean[][] visited;

	static class Pos {
		int r;
		int c;
		int d;

		public Pos(int r, int c, int d) {
			this.r = r;
			this.c = c;
			this.d = d;
		}
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int t = 0; t < T; t++) {

			N = sc.nextInt();
			board = new int[N][N];
			visited = new boolean[N][N];

			start[0] = sc.nextInt();
			start[1] = sc.nextInt();
			end[0] = sc.nextInt();
			end[1] = sc.nextInt();

			if( start[0] == end[0] && start[1] == end[1]) {
				System.out.println(0);
			}else bfs(); 
			
			
		}

		//// 확인용 출력문
//		System.out.println(start[0] + " " +   start[1] +  end[0] +  end[1] );


	}

	private static void bfs() {
		Queue<Pos> que = new LinkedList<>();
		que.add(new Pos(start[0], start[1], 1));
		visited[start[0]][start[1]] = true;
		
		while (!que.isEmpty()) {
			Pos curr = que.poll();

			for (int k = 0; k < 8; k++) {
				int nr = curr.r + dr[k];
				int nc = curr.c + dc[k];

				if (nr < 0 || nc < 0 || nr >= N || nc >= N || visited[nr][nc])
					continue;
				que.add(new Pos(nr, nc, curr.d + 1));
				visited[nr][nc] = true;
				
				if (nr == end[0] && nc == end[1]) {
					System.out.println(curr.d);
					return;
				}

			}
		}
	}

}
