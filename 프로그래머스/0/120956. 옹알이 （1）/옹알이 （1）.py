def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for i in babbling:
        temp_word = i
        used_sounds = set()
        
        for j in valid_sounds:
            if j in temp_word:
                if j not in used_sounds:
                    temp_word = temp_word.replace(j, " ", 1)
                    used_sounds.add(j)
                else:
                    temp_word = ""
                    break

        for j in valid_sounds:
            if j in temp_word:
                temp_word = ""
                break
                
        if temp_word.strip() == "":
            count += 1

    return count