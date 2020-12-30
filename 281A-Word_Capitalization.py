# https://codeforces.com/problemset/problem/281/A
def split(word):
    return list(word)


capital_Input = input("")
compare_List = split(capital_Input)
a = compare_List[0].upper()
print(a+capital_Input[1:])
