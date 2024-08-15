
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			int T = sc.nextInt();
			for (int t = 1; t <= T; t++) {
				char[][] flag = makeFlag(sc);

				int result = Min(flag);

				System.out.println("#" + t + " " + result);
			}
		}
	}

	static char[][] makeFlag(Scanner sc) {
		int N = sc.nextInt();
		int M = sc.nextInt();
		char[][] flag = new char[N][M];
		for (int i = 0; i < N; i++) {
			String tmp = sc.next();
			for (int j = 0; j < M; j++) {
				flag[i][j] = tmp.charAt(j);
			}
		}
		return flag;
	}

	static int Min(char[][] flag) {
		int N = flag.length;
		int min = Integer.MAX_VALUE;

		for (int w = 0; w < N - 2; w++) {
			int countW = calculate(flag, 0, w, 'W');

			for (int b = w + 1; b < N - 1; b++) {
				int countB = calculate(flag, w + 1, b, 'B');

				int countR = calculate(flag, b + 1, N - 1, 'R');

				int sum = countW + countB + countR;

				if (sum < min)
					min = sum;
			}
		}
		return min;
	}

	static int calculate(char[][] flag, int startR, int endR, char color) {
		int M = flag[0].length;
		int count = 0;
		for (int r = startR; r <= endR; r++) {
			for (int j = 0; j < M; j++) {
				if (!(flag[r][j] == color)) {
					count++;
				}
			}
		}
		return count;
	}

}
