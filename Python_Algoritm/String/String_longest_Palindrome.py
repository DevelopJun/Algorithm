'''
가장 긴 팰린드롬 부분 문자열을 출력하라 
- 컴퓨터과학의 오랜 문제 중에 '최장 공통 부분 문자열'이라는 문제가 있다. 
여러 개의 입력 문자열이 있을 때 서로 공통된 가장 긴 부분 문자열을 찾는
문제로 다이나믹 프로그래밍을 풀 수 있는 전형적인 문제다. 이 문제 또한
동일한 유형의 문제로서, 동일하게 다이나믹 프로그래밍으로 풀 수 있다. 
그러나 이 문제는 아래와 같은 방식 
'''

Inputdata1 = "babadab"
Inputdata2 = "cbbd"


def longestPalindrome(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 화장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이싱 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        # max 를 key=len 으로 잡아서 문자열에서 가장 긴 문자열 반환한다.
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)

    return result
    pass


print(longestPalindrome(Inputdata1))
