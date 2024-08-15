
import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int T = sc.nextInt();
	for (int t = 1; t <= T; t++) {
		
		//ArrayList<String> field = new ArrayList<>();
		String field = sc.next();
		int ballCount = 0;
		for (int i = 0; i < field.length(); i++) {
			char tmp = field.charAt(i);
			if (tmp == '(') {
				ballCount++;
				i++;
			}
			if (tmp == ')') {
				ballCount++;
			}
		}
		System.out.println("#" + t + " " + ballCount);
		
	}
}
}
