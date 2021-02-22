#include <string>
#include <vector>

using namespace std;

int max(int a, int b){
    if (a>b) return a;
    else return b;
}

int solution(vector<vector<int>> triangle) {
    for (int i=triangle.size()-1; i>0; i--){
        for (int j=0; j<i; j++){
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1]);
        }
    }
    
    
    return triangle[0][0];
}