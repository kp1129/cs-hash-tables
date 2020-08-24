import re

def word_count(s):
    # Your code here
    my_dict = {}
    if s != "":
        s = s.split(" ")
        for word in s:
            word = re.sub("[^a-z'A-Z]+", " ", word).split(" ")
            for each in word:
                each = each.lower()
                if each in my_dict:
                    my_dict[each] += 1
                else:
                    my_dict[each] = 1    
        if "" in my_dict:
            del my_dict[""]        
    return my_dict


if __name__ == "__main__":
    print(word_count('a a\ra\na\ta \t\r\n'))    
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))