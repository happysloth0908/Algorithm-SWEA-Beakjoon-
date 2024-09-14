
import java.util.Scanner;

public class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        map = new int[N][N];
        
        int maxHeight = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = sc.nextInt();
                maxHeight = Math.max(maxHeight, map[i][j]);
            }
        }

        int maxSafeAreas = 1; // 비가 오지 않는 경우를 고려
        for (int rain = 1; rain <= maxHeight; rain++) {
            visited = new boolean[N][N];
            int safeAreas = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j] && map[i][j] > rain) {
                        dfs(i, j, rain);
                        safeAreas++;
                    }
                }
            }
            maxSafeAreas = Math.max(maxSafeAreas, safeAreas);
        }

        System.out.println(maxSafeAreas);
    }

    static void dfs(int r, int c, int rain) {
        visited[r][c] = true;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < N && nc >= 0 && nc < N && !visited[nr][nc] && map[nr][nc] > rain) {
                dfs(nr, nc, rain);
            }
        }
    }
}