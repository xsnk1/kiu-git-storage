def solution(s):
    return [(s[i:i+2]) if i < (len(s) - 1) else (s[-1] + "_") for i in range(0, len(s), 2)]