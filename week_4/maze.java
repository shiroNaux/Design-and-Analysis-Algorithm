
import java.util.*;

public class maze {
    private static int N = 8;
    static int [] visited;
    static int [][] matrix ;
    static int S;
    static int F;
    static int[] p;

    static void __try(int i){
        for (int j = 0; j < 8; j++) {
            if(matrix[p[i -1]][j] == 1 && visited[j] == 0){
                p[i] = j ;
                visited[j] = 1;
                if(p[i] == F){
                    int f = 0;
                    System.out.print("Đường đi là: \t");
                    do{
                        System.out.print(p[f] + "\t");
                        f++;
                    } while (p[f] != F);
                    System.out.println(F);
                    return;
                } else {
                    __try(i+1);
                }

                visited[j] = 0;
            }
        }
    }

    public static void main(String[] args) {

        // test 1: Dựa theo slide bài giảng của giảng viên
        N = 8;
        matrix = new int[][]{
                {0, 1, 0, 0, 0, 0, 0, 1},
                {1, 0, 1, 0, 0, 0, 1, 1},
                {0, 1, 0, 0, 0, 1, 1, 0},
                {0, 0, 0, 0, 1, 1, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0},
                {0, 0, 1, 1, 0, 0, 1, 0},
                {0, 1, 1, 0, 0, 1, 0, 0},
                {1, 1, 0, 0, 0, 0, 0, 0},
        };
        S = 0; F = 4;
        p = new int[N];
        visited = new int[N];
        visited[S] = 1;
        __try(1);
    }
}
