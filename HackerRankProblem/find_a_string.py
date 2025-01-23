def subString(main_str, sub_str):
    count = 0
    n = len(main_str) - len(sub_str) + 1
    for i in range(n):
        if (main_str[i : i + len(sub_str)] == sub_str):
            count += 1
        return count
    
subString("ABCDCDC", "CDC")

