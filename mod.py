'''
알고리즘 문제에서 나머지는 10^50 이상의 long long의 범위도 넘어서는 너무 큰 숫자를 다룰 때 사용된다.
나머지 구하기
+의 경우 : (A+B) mod M = ((A mod M)+(B mod M)) mod M
-의 경우 : (A-B) mod M = ((A mod M)-(B mod M)+M) mod M ***음수의 경우 mod의 결과가 프로그래밍 언어마다 다르다. C++&Java는 음수로, python은 양수로 나옴. 결과는 같으므로 무조건 양수를 만들기 위해 M을 더해준다.
*의 경우 : (A*B) mod M = ((A mod M)*(B mod M)) mod M
/의 경우 : (A/B) mod M = A*B^(M-2) mod M ***A랑 B가 서로소일 경우에만, 페르마의 소정리
'''