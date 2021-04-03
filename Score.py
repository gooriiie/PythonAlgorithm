import sys

t = (int)(input()) # testcase 개수

if 0 < t <= 20:
    for _ in range(t):
        testcase = sys.stdin.readline().rstrip()  # testcase 입력
        if (len(testcase)) <= 50:
            testcase_list = list(testcase)  # 입력받은 문자열을 리스트로 변환
            total = 0  # 총점
            AScore = 1  # A의 점수
            for alphabet in testcase_list:
                if alphabet == 'A':
                    total += AScore  # 총점에 A 점수를 더한다
                    AScore += 1  # A 점수를 1점 올린다
                else:
                    AScore = 1  # A 점수를 1점으로 초기화한다
            print(total)  # 총점 출력
