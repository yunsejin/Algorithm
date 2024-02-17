def solution(my_string, d, s):
    return my_string[:s]+d+my_string[s+len(d):]