def korean_letter_index(letter):
    base_code = 0xAC00
    total_jongseong = 28
    total_jungseong = 21
    
    code = ord(letter)
    
    code -= base_code
    
    jongseong_index = code % total_jongseong
    code //= total_jongseong
    jungseong_index = code % total_jungseong
    code //= total_jungseong
    choseong_index = code
    
    letter_index = choseong_index * total_jungseong * total_jongseong + jungseong_index * total_jongseong + jongseong_index + 1
    return letter_index

letter = input().strip()

print(korean_letter_index(letter))
