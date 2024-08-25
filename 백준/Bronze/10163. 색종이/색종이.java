
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int[][] board = new int[1001][1001];

		for (int t = 1; t <= T; t++) {

			int r = sc.nextInt();
			int c = sc.nextInt();

			int cl = sc.nextInt();
			int rl = sc.nextInt();

			for (int i = r; i < (r + cl); i++) {
				for (int j = c; j < (c + rl); j++) {
					board[i][j] = t;
				}
			}
		}
//		for (int i = 0; i < board.length; i++) {
//			for (int j = 0; j < board.length; j++) {
//				System.out.print(board[i][j]);
//		}
//			System.out.println();
//		}

		int[] count = new int[(T + 1)];
		for (int t_ = 1; t_ < count.length; t_++) {
			for (int i = 0; i < board.length; i++) {
				for (int j = 0; j < board.length; j++) {
					if (board[i][j] == t_) {
						count[t_]++;
					}
				}
			}
			
		}
		
		for (int i = 1; i < count.length; i++) {
			System.out.println(count[i]);			
		}

	}
}
