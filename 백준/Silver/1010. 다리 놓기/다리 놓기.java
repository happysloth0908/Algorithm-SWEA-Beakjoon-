

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
	
		for (int t = 0; t < T; t++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
	
			double totalN = 1; // 더블로 넣지 않으면 큰 수는 못 받아들임. 
			double totalM = 1;
			
		for (int i = 0; i < N; i++) {
			totalM *= M;
			M--;
		}
		int tmpN = N;
		for (int i = 0; i < N; i++) {
			totalN *= tmpN;
			tmpN--;
		}
		
		// 0f 니까 소수점 이하 아무것도 출력 안 함
		System.out.printf("%.0f\n",totalM / totalN);
		}
		
	}
}
