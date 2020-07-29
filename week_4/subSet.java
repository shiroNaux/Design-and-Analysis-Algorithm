

public class subSet {
    static int N ;
    static int K;
    static int result[];
    static int used[];


    static boolean check(int[] arr){
        for (int k = 1; k < K; k++) {
            if (arr[k] != (N - K + k + 1)){
//                System.out.println(arr[k] != (N - K + k + 1));
                return false;
            }
        }
        return true;
    }
    static void __try(int i, int m){
        for (int j = 0; j < N; j++) {
            if (used[j] == 0 && j >= m){
                result[i - 1] = j + 1;
                used[j] = 1;
                if (i == K){
                    for (int x:result
                    ) {
                        System.out.printf(x + " | ");
                    }
                    System.out.println("");
//                    if (check(result)) result = new int[K];
                } else __try(i + 1, j);

                used[j] = 0;
            }
        }
    }

    public static void main(String[] args) {

        // test 1: Tổ hợp con có 5 phần tử của các số tự nhiên từ 1 đến 7
        N = 7;
        K = 5;
        result = new int[K];
        used = new int[N];

        __try(1, 0);

        System.out.println("--------------------");
        // test 2: Tổ hợp con có 3 phần tử của các số tự nhiên từ 1 đến 6
        N = 6;
        K = 3;
        result = new int[K];
        used = new int[N];

        __try(1, 0);

    }
}
