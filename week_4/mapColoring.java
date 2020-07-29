
public class mapColoring {
    private static int N ;
    static int numberColor ;
    static int [] colored;
    static int [][] matrix ;

    static boolean check(int vertex, int color){
        for (int i = 0; i < N; i++) {
            if (matrix[vertex][i] == 1 & colored[i] == color) return false;
        }
        return true;
    }

    static void __try(int i){
        for (int j = 1; j < numberColor + 1; j++) {
            if(check(i-1, j)){
                colored[i-1] = j;

                if(i == N){
                    return;
                } else if(i < N) __try(i + 1);
            }
        }
    }

    public static void main(String[] args) {

        matrix = new int[][]{
                {0, 1, 0, 0, 0, 0, 0, 1},
                {1, 0, 1, 0, 0, 1, 1, 1},
                {0, 1, 0, 0, 0, 1, 1, 0},
                {0, 0, 0, 0, 1, 1, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0},
                {0, 1, 1, 1, 0, 0, 1, 0},
                {0, 1, 1, 0, 0, 1, 0, 0},
                {1, 1, 0, 0, 0, 0, 0, 0},
        };
        N = 8;
        numberColor = 4;
        colored = new int[N];

        __try(1);

        System.out.println("________________________________");
        for (int i = 0; i < N; i++) {
            System.out.print("Tô màu " + colored[i] + " cho quốc gia thứ " + (i + 1) + "\n");
        }
    }
}
