# 문제 설명
# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다.
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩만 사용해 조합한(이어 붙인) 발음만 할 수 있습니다.
# babbling이라는 문자열 배열이 매개변수로 주어질 때, 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성하세요.

# 제한사항
# 1 ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 15
# - 각 문자열에서는 "aya", "ye", "woo", "ma"는 각각 한 번씩만 등장합니다.
# - 문자열은 알파벳 소문자로만 이루어져 있습니다.

def solution(babbling):
    # 발음할 수 있는 단어 목록을 리스트로 정의합니다.
    possible_words = ["aya", "ye", "woo", "ma"]
    
    # 발음 가능한 단어의 개수를 세기 위한 변수
    answer = 0

    # babbling 리스트를 순회합니다.
    for word in babbling:
        # 임시 변수에 현재 단어를 저장합니다.
        temp = word

        # 발음 가능한 단어를 하나씩 제거합니다.
        for pw in possible_words:
            # 해당 발음 단어를 빈 문자열로 대체합니다.
            temp = temp.replace(pw, "")
        
        # 모든 발음을 제거한 후 남은 문자열이 없다면 조카가 발음할 수 있는 단어입니다.
        if temp == "":
            answer += 1

    # 발음할 수 있는 단어의 총 개수를 반환합니다.
    return answer

# 테스트 예시:
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))  # 출력: 1
print(solution(["ayaye", "uuuuma", "ye", "yemawoo", "ayaaa"]))  # 출력: 3
