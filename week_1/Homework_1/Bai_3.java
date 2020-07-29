
public class Bai_3 {
    public static void main(String[] args) {
        int matrix[][] = {
                {0,1,1,0,1},
                {1,0,0,1,0},
                {1,0,0,1,0},
                {0,1,1,0,0},
                {1,0,0,0,0}
        };
        int m = 0;
        int t[] = new int[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                t[i] += matrix[i][j];
            }
        }

        for (int i = 0; i < t.length; i++) {
            if(t[i] >= m) m = t[i];
        }
        for (int i = 0; i < t.length; i++) {
            if(t[i] == m) System.out.printf("San bay thu " + (i + 1) + " co so luong duong bay nhieu nhat la: " + m);
        }
    }
}
