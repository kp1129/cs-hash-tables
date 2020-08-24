def no_dups(s):
    # Your code here
    if s == "":
        return s
    s = s.split(" ")
    clean = []
    for each in s:
        if each not in clean:
            clean.append(each)
    return " ".join(clean)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))