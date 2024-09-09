import java.util.Scanner;

public class Main {
    static int N, M;
    static int[][] board;
    static int maxSum = 0;

    // 테트로미노의 모든 가능한 모양 정의
    static int[][][] tetrominos = {
        {{0,0}, {0,1}, {0,2}, {0,3}},
        {{0,0}, {1,0}, {2,0}, {3,0}},
        {{0,0}, {1,0}, {0,1}, {1,1}},
        {{0,0}, {1,0}, {2,0}, {2,1}},
        {{0,1}, {1,1}, {2,1}, {2,0}},
        {{0,0}, {0,1}, {1,1}, {2,1}},
        {{0,0}, {0,1}, {1,0}, {2,0}},
        {{0,0}, {1,0}, {1,1}, {1,2}},
        {{0,2}, {1,0}, {1,1}, {1,2}},
        {{0,0}, {0,1}, {0,2}, {1,2}},
        {{0,0}, {1,0}, {0,1}, {0,2}},
        {{0,0}, {1,0}, {1,1}, {2,1}},
        {{0,1}, {1,0}, {1,1}, {2,0}},
        {{0,1}, {0,2}, {1,0}, {1,1}},
        {{0,0}, {0,1}, {1,1}, {1,2}},
        {{0,0}, {0,1}, {0,2}, {1,1}},
        {{0,1}, {1,0}, {1,1}, {1,2}},
        {{0,0}, {1,0}, {1,1}, {2,0}},
        {{0,1}, {1,1}, {1,0}, {2,1}}
    };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        solve();
        System.out.println(maxSum);
    }

    static void solve() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                checkAllTetrominos(i, j);
            }
        }
    }

    static void checkAllTetrominos(int x, int y) {
        for (int[][] tetromino : tetrominos) {
            int sum = 0;
            boolean isValid = true;

            for (int[] block : tetromino) {
                int nx = x + block[0];
                int ny = y + block[1];

                if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                    isValid = false;
                    break;
                }

                sum += board[nx][ny];
            }

            if (isValid) {
                maxSum = Math.max(maxSum, sum);
            }
        }
    }
}