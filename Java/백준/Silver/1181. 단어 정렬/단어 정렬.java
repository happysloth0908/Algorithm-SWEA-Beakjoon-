import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException {
//        PriorityQueue<String> pq = new PriorityQueue<>((a,b) -> {
        TreeSet<String> ts = new TreeSet<>((a,b)->{
        if (a.length() > b.length()){
                return 1;
            }else if (a.length() < b.length()){
                return -1;
            } else{ // 길이가 같은 경우
                return a.compareTo(b);
            }
        });
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            ts.add(br.readLine());
        }
        for (String t: ts) {
            System.out.println(t);
        }
    }
}
