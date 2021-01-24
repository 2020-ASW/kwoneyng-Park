// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int answer;
int cnt;

void rcsv(int n, int plus, int mul) {
	if (n == 3 && plus == mul*2) {
		answer += 1;
		return;
	}
	else if (n % 3 == 0) {
		if (plus >= mul * 2) {
			rcsv(n / 3, plus, mul + 1);
			if (plus < cnt * 2) {
				rcsv(n - 1, plus + 1, mul);
			}
		}
		else {
			rcsv(n - 1, plus + 1, mul);
		}
	}
	else if (n > 3) {
		rcsv(n - 1, plus + 1, mul);
	}
}

int solution(int n) {
    answer = 0;
    long long rs = 1;
    cnt = 0;
    while (rs < n){
        rs *= 3;
        cnt += 1;
    }
    
    n -= 2;
    if (n==3){
        return 1;
    } else{
        rcsv(n,2,1);
    }
    
    return answer;
}