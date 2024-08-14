package SWEA;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class 새로운불면증치료법_1288 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int t = 1; t <= T ; t++) {
			int N = sc.nextInt();
			
			String tmp = "";
			Set<Character> oneToTen = new HashSet<>();
			
			int m = 0;
			while (oneToTen.size() < 10) {
				m++;
				tmp = String.valueOf(N * m);

				for (int i = 0; i < tmp.length(); i++) {
 					char tmp2 = tmp.charAt(i);
					oneToTen.add(tmp2);
				}
				
			}
			System.out.println("#" + t + " "+ (N * m));
			
		}
	}
}
