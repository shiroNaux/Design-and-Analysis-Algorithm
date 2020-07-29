//
// Created by Shiro on 4/27/2020.
//
#include <limits>
#include "iostream"
using namespace std;

const int N = 4;
int visited[] = {0, 0, 0, 0};
int matrix[][N] = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
};
int S = 0;
int bestCost = std::numeric_limits<int>::max();
int result[N] ;
int p[] = {0, 0, 0, 0, 0};

void _try(int i, int c){
    for (int j = 0; j < N; j++) {
        if (matrix[p[i - 1]][j] > 0 && visited[j] == 0){
            int c1 = c + matrix[p[i - 1]][j];

            if( c1 < bestCost){
                p[i] = j;
                visited[j] = 1;

                if( i == N && p[i] == S){
                    std::copy(std::begin(p), std::end(p), std::begin(result));
                    bestCost = c1;
                } else if (i <= N){
                    _try(i + 1, c1);
                }

                visited[j] = 0;
            }
        }
    }
}

int main(){
    _try(1, 0);

    for (int i = 0; i < N; ++i) {
        std::cout << result[i] << " \t";
    }
}