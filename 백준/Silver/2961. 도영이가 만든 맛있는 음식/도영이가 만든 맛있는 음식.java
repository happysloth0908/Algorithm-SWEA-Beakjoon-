
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int Sarr[];
	static int Barr[];
	static boolean sel[];
	static int T;
	static int Min;
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		T = sc.nextInt();
		Sarr = new int[T];
		Barr = new int[T];
		sel = new boolean[T];

		for (int t = 0; t < T; t++) {
			int N = sc.nextInt();
			Sarr[t] = N;
			int M = sc.nextInt();
			Barr[t] = M;
		}
	//	System.out.println(Arrays.toString(Sarr));
	//	System.out.println(Arrays.toString(Barr));

		부분집합();
		System.out.println(Min);
	}

	private static void 부분집합() {
		Min = 999999999;
		for (int i = 1; i < (1 << T); i++) {
			int Stotal = 1;
			int Btotal = 0;
			for (int j = 0; j < T; j++) {
				if ((i & (1 << j)) > 0) {
					Stotal *= Sarr[j];
					Btotal += Barr[j];
				}
			}
			int tmp = Math.abs(Stotal - Btotal);
			if ( tmp < Min ) Min = tmp;
		}
	}

}
