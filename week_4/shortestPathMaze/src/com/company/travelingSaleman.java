package com.company;

public class travelingSaleman {
    static int N ;
    static int[] visited;
    static int matrix[][];
    static int S ;
    static int [] p;
    static int[] result ;
    static int bestCost ;
    static void __try(int i, int c){
        for (int j = 0; j < N; j++) {
            if (matrix[p[i - 1]][j] > 0 && visited[j] == 0){
                int c1 = c + matrix[p[i - 1]][j];

                if( c1 < bestCost){
                    p[i] = j;
                    visited[j] = 1;

                    if( i == N   && p[i] == S){
                        result = p.clone();
                        bestCost = c1;
                    } else if (i < N){
                        __try(i + 1, c1);
                    }

                    visited[j] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {

        // test 1:
        N = 4;
        S = 0;
        visited = new int[N];
        matrix = new int[][]{
                {0, 10, 15, 20},
                {10, 0, 35, 25},
                {15, 35, 0, 30},
                {20, 25, 30, 0}
        };
        result =  new int[N + 1];
        bestCost = Integer.MAX_VALUE;
        p = new int[N + 1];
        p[0] = S ;
        __try(1, 0);

        System.out.printf("Đường đi là: ");
        for (int i = 0; i < N + 1; i++) {
            System.out.printf(result[i]+  "\t");
        }
        System.out.println("\n giá trị tối thiểu: " + bestCost);

        System.out.println("-------------------");

        // test 2:
        N = 5;
        S = 2;
        visited = new int[N];
        matrix = new int[][]{
                {0, 7, 9, 6, 1},
                {7, 0, 3, 4, 9},
                {9, 3, 0, 2, 5},
                {6, 4, 2, 0, 3},
                {1, 9, 5, 3, 0}
        };
        result =  new int[N + 1];
        bestCost = Integer.MAX_VALUE;
        p = new int[N + 1];
        p[0] = S ;
        __try(1, 0);

        System.out.printf("Đường đi là: ");
        for (int i = 0; i < N + 1; i++) {
            System.out.printf(result[i]+  "=>");
        }
        System.out.println("\n giá trị tối thiểu: " + bestCost);
    }
}
