
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int t = 1; t <= 10; t++) {
			int T = sc.nextInt();

			int N = sc.nextInt();
			int M = sc.nextInt();

			int result = power(N, M);

			System.out.println("#" + T + " " + result);
		}
	}

	private static int power(int N, int M) {
		if (M == 0) {
			return 1;
		}
		if (M == 1) {
			return N;
		}
		return N * power(N, M - 1);

	}
}
