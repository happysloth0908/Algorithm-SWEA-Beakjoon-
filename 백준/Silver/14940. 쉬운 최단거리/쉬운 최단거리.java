
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int arr [][];
    static int n;
    static int m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int [n][m];
        int a = 0;
        int b = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if(arr[i][j] == 2) {
                	a = i;
                	b = j;
                }
            }
        }
        
        
        bfs(a , b);

    }
    static int [] dr = {0, 0, -1, 1};
    static int [] dc = {-1, 1, 0, 0};

    private static void bfs(int x, int y) {
        int visited [][] = new int[n][m]; // 여기에 누적합
        
        for (int i = 0; i < n; i++) {
			Arrays.fill(visited[i], -1);
		}
        
        Queue<int[]> que = new LinkedList<>();

        visited[x][y] = 0;
        que.add(new int[]{x, y, 0});

        while (!que.isEmpty()) {
            int[] curr = que.poll();
            for (int i = 0; i < 4; i++) {
                int nr = curr[0] + dr[i];
                int nc = curr[1] + dc[i];
                if(nr < 0 || nc < 0 || nr >= n || nc >= m || visited[nr][nc] != -1 || arr[nr][nc] == 0) continue;
                que.add(new int[] {nr, nc, curr[2] + 1});
                visited[nr][nc] = curr[2] + 1;
            }
        }
//        visited[0][0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
            	if(arr[i][j] == 0 ) {
            		System.out.print(0 + " ");
            	}else {
            		System.out.print(visited[i][j] + " ");
            	}
            }
                System.out.println();
        }


    }
}
