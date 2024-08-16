
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
			System.out.print( "#" + t);
			int N = sc.nextInt();
			for (int n = 0; n < N; n++) {
				int tmp = sc.nextInt();
				if (1 == tmp) {
					int data = sc.nextInt();
					heap.add(data);
				} else { // 2가 나올 경우
					if (!(heap.isEmpty())) {
						int output = heap.poll();
						System.out.print(" " + output);
					}else System.out.print(" " + -1);
				}
			}
			System.out.println();

		}

	}

}
