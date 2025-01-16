
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int arr [] = new int[9];
		int max = 0;
		
		for (int i = 0; i < 9; i++) {
			int curr = Integer.parseInt(br.readLine());
			arr[i] = curr;
			if(curr > max) {
				max = curr;
			}
		}
		int ans = 0;
		for (int i = 0; i < 9; i++) {
			if(arr[i] == max) ans = i + 1;
		}
		
		System.out.println(max + "\n" + ans);
	}
}
