def mutation(string, position, character):
    li = list(string)
    li[position] = character
    string = "".join(li)
    return string


s = input()
p, c = input().split()      # p is the position ['5'] change the string to integer int(p) and c is the character to be replaced
res = mutation(s, int(p), c)
print(res)                  # kodnest
                            # 0 C
                            # Codnest