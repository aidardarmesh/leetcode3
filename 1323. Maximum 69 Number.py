def max_69(num):
    digits = list(str(num))
    changed, limit = 0, 1

    for i in range(len(digits)):
        if digits[i] == "6":
            if changed < limit:
                changed += 1
                digits[i] = "9"
    
    return int(''.join(digits))
