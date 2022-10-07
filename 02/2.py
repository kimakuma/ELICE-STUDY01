def main():
    x = input()

    arr = list(input())

    dic = {'upper': 0, 'lower': 0, 'digit': 0}
    
    for i in arr:
        if i.isupper(): dic['upper'] += 1
        elif i.islower(): dic['lower'] += 1
        else: dic['digit'] += 1 

    print(dic['upper'], dic['lower'], dic['digit'])
    

if __name__=="__main__":
    main()

"""
import itertools as it
import string
from collections import Counter

classification_char_type = lambda c: 'lower' if c in string.ascii_lowercase else 'upper' if c in string.ascii_uppercase else 'digit' if c in string.digits else 'special'

len = input()

str = input()

counter = Counter(list(iter(lambda str = iter(str): classification_char_type(next(str)), [])))

print(counter['upper'], counter['lower'], counter['digits']) """
