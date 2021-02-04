#include<iostream>
#include<cmath>
using namespace std;
 
int main(int argc, char** argv)
{
    int test_case;
    int T,p,q,r,a,b,c,d,cirT,cirB,cirL,cirR;
    bool red,blue;
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin>>T;
    for(test_case = 1; test_case <= T; ++test_case)
    {
        cin >> p >> q >> r >> a >> b >> c >> d;
        cirT = p+r; cirB = p-r; cirL=q-r; cirR = q+r;
        if (cirB < a || cirT > c || cirL < b || cirR > d){
            red = true;
        } else {
            red = false;
        }
        if (pow(a-p,2) + pow(b-q,2) > pow(r,2) || pow(a-p,2)+pow(d-q,2) > pow(r,2) || pow(c-p,2) + pow(b-q,2) > pow(r,2) || pow(c-p,2) + pow(d-q,2) > pow(r,2)){
            blue = true;
        } else{
            blue = false;
        }
         
        cout << "#" <<test_case<<' '<<(red ? "Y" : "N") << (blue ? "Y":"N") << '\n';
 
    }
    return 0;//정상종료시 반드시 0을 리턴해야합니다.