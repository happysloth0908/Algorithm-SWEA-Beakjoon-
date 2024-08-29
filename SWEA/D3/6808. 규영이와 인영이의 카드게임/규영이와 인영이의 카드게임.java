
import java.util.Scanner;

public class Solution {

	static int[] gCards;
	static int[] iCards;
	static int N = 9;
	static boolean[] visited;
	
	static int win;
	static int lose;
	
	static int[] result;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {

			gCards = new int[N];
			for (int i = 0; i < N; i++) {
				gCards[i] = sc.nextInt();
			}

			/////

			// 인영이의 카드 구하기
			int[] allCards = new int[19];
			iCards = new int[N];
			int tmp = 0;
			for (int i = 0; i < gCards.length; i++) {
				allCards[gCards[i]]++;
			}
			for (int i = 1; i < allCards.length; i++) {
				if (allCards[i] == 0 && tmp <= N)
					iCards[tmp++] = i;
			}



			// 인영이 카드 순열 조합을 찾아내야 함.
			visited = new boolean[N];
			result = new int[N];
			perm(0);
			
			System.out.println("#" + t + " " + win + " " + lose);
			win = 0;
			lose = 0;
		}

	}

	private static void perm(int idx) {
		if (idx == N ) {
			calculateScore();
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if ( visited[i]) continue;
			result[idx] = iCards[i];
			visited[i] = true;
			perm(idx + 1);
			visited[i] = false;
		}
	}

	private static void calculateScore() {
		int gScore = 0;
		int iScore = 0;
		
		for (int i = 0; i < N; i++) {
			if(gCards[i] > result[i]) {
				gScore += gCards[i] + result[i];
			}else {
				iScore += gCards[i] + result[i];
			}
		}
		
		if (gScore > iScore) win++;
		else if (gScore < iScore) lose++;
	}

}
