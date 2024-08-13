
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		for (int T = 1; T <= 10; T++) {
			int N = sc.nextInt(); // 원본 암호문 개수
			LinkedList<Integer> ciperText = new LinkedList<>();
			for (int i = 0; i < N; i++) {
				ciperText.add(sc.nextInt()); // 원본 암호문
			}

			int M = sc.nextInt(); // 명령어 개수
			for (int m = 0; m < M; m++) {
				String command = sc.next();

				switch (command) {
				case "I":
					int Ix = sc.nextInt(); // x번째 암호문 다음에
					int Iy = sc.nextInt(); // y개의 암호문 추가
					for (int i = 0; i < Iy; i++) {
						ciperText.add(Ix + i, sc.nextInt());
					}
					break;

				case "D":
					int Dx = sc.nextInt(); // x번째 암호문 다음에
					int Dy = sc.nextInt(); // y개의 암호문 삭제
					for (int i = 0; i < Dy; i++) {
						ciperText.remove(Dx);
					}
					break;
				case "A":
					int Sy = sc.nextInt();
					for (int i = 0; i < Sy; i++) {
						int Ss = sc.nextInt();
						ciperText.add(Ss);
					}
					break;

				default:
					break;
				}
				
			}
			System.out.print("#" + T + " ");
			for (int i = 0; i < 10; i++) {
				int result = ciperText.poll();
				System.out.print(result + " ");
			}
			System.out.println();
		}
	}
}
