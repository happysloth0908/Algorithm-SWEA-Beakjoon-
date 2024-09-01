import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N];

		for (int t = 0; t < N; t++) {
			arr[t] = sc.nextInt();
		}

		Arrays.sort(arr);

		Set<Integer> twoSum = new HashSet<>();
		for (int i = 0; i < N; i++) {
			for (int j = i; j < N; j++) {
				twoSum.add(arr[i] + arr[j]);
			}
		}

		for (int i = N - 1; i >= 0; i--) {
			for (int j = 0; j < i; j++) {
				if (twoSum.contains(arr[i] - arr[j])) {
					System.out.println(arr[i]);
					return;
				}
			}
		}
	}

}