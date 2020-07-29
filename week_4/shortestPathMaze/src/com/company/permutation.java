package com.company;

public class permutation {
    static int N ;
    static int result[];
    static int used[];
    static void __try(int i){
        for (int j = 0; j < N; j++) {
            if (used[j] == 0){
                result[i - 1] = j + 1;
                used[j] = 1;
                if (i == N){
                    for (int x:result
                         ) {
                        System.out.printf(x + " | ");
                    }
                    System.out.println("");
                } else __try(i + 1);

                used[j] = 0;
            }
        }
    }

    public static void main(String[] args) {

        // test 1: Sinh hoán vị của tập các số tự nhiên từ 1 đến 4
        N = 4;
        result = new int[N];
        used = new int[N];
        __try(1);

        System.out.println("--------------------------");

        // test 2: Sinh hoán vị của tập các số tự nhiên từ 1 đến 6
        N = 6;
        result = new int[N];
        used = new int[N];
        __try(1);
    }
}
