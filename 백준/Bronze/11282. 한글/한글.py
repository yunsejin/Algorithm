def find_korean_letter(n):
    # 한글 초성, 중성, 종성의 개수
    CHO = 19
    JUNG = 21
    JONG = 28
    
    # 유니코드 한글 시작점
    UNICODE_START = 0xAC00
    
    # 인덱스 조정 (0부터 시작)
    index = n - 1
    
    # 초성, 중성, 종성 인덱스 계산
    cho_index = index // (JUNG * JONG)
    jung_index = (index % (JUNG * JONG)) // JONG
    jong_index = (index % (JUNG * JONG)) % JONG
    
    # 유니코드 포인트 계산
    unicode_point = UNICODE_START + (cho_index * JUNG * JONG) + (jung_index * JONG) + jong_index
    
    # 유니코드 포인트를 문자로 변환
    return chr(unicode_point)

inputs = int(input())

print(find_korean_letter(inputs))