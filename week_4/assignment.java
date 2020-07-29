
public class assignment {

    static int N ;
    static int matrix[][] ;

    static int bestCost = Integer.MAX_VALUE;
    static int [] used ;
    static int [] assign ;
    static int [] result;


    static void __try(int i, int cost){
        for (int j = 0; j < N; j++) {
            if ( matrix[i - 1][j] > 0 && used[j] == 0){
                int c1 = cost + matrix[i - 1][j];

                if(c1 < bestCost){
                    assign[i - 1] = j + 1;
                    used[j] = 1;
                    if(i == N ){
                        result = assign.clone();
                        bestCost = c1;
                    } else if (i <= N) __try(i + 1, c1);

                    used[j] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {

        N = 3;
        matrix = new int[][]{
                {2500, 4000, 3500},
                {4000, 6000, 3500},
                {2000, 4000, 2500}
        };
        used = new int[N];
        result = new int[N];
        assign = new int[N];
        __try(1,0);

        for (int i = 0; i < N; i++) {
            System.out.print("Người thứ" + (i + 1)+ " thực hiên công việc " + result[i] + "\n");
        }
        System.out.println("Giá trị tối thiểu "+ bestCost);
    }
}
