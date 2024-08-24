

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] seats = new String[1];
		seats[0] = sc.next();
		
		char[] seats2 = new char[seats[0].length()];
		
		for (int i = 0; i < seats[0].length(); i++) {
			seats2[i] = seats[0].charAt(i);
		}
//		System.out.println(Arrays.toString(seats2));
		
//		ArrayList<Character> cupHolder = new ArrayList<Character>();
//		String[] cupHolder = new String[N + N];
//		cupHolder[0] = "C";
//		cupHolder[N + N - 1] = "C";
		Queue<String> cupHolder = new LinkedList<>(); 
		cupHolder.add("C");
		
		for (int i = 0; i < N; i++) {
			if  (seats2[i] == 'S') {
				cupHolder.add("S");
				if (i < (N - 1))
					cupHolder.add("C");
			} else {
				cupHolder.add("L");
				cupHolder.add("L");
				i++;
				if (i < (N - 1))
				cupHolder.add("C");
			}
		}

		cupHolder.add("C");
		int tmp = cupHolder.size();
		
		int cupHolderCount = 0;
		for (int i = 0; i < tmp; i++) {
			String temp = cupHolder.poll();
//			System.out.print(temp);
			if ( temp == "C" ) cupHolderCount++;
		}
		if (cupHolderCount > N) {
			System.out.println(N);
		}
		else System.out.println(cupHolderCount);
		
	}
}
