def count_words(text):
    words = text.split()
    return len(words)

def char_count(input):
    counter = {}
    for char in input.lower():
        if char.isalpha():
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter

def sort_on_num(item):
    return item["num"]

def sort_on(items):
    lis = []
    for char, num in items.items():
        if char.isalpha():
            dic = {"char": char, "num": num}
            lis.append(dic)
    lis.sort(reverse=True, key=sort_on_num)
    return lis
    