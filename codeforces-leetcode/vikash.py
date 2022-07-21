import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from random import choice

s = input()

def longest_subsequence(string): 
    def hel(chosen="", i=0): 
        if i == len(string):
            if set("aeiou").issubset(set(chosen)):
            
                return chosen
        
            return ""
  
        hashable = (chosen[-1] if chosen else None, len(chosen), i) 
  
        if hashable in memo: 
            return memo[hashable] 
  
        if not chosen: 
            res = hel("a" if string[i] == "a" else chosen, i + 1)
            
        elif chosen[-1] == string[i]: 
            res = hel(chosen + string[i], i + 1)
            
        elif mapping[chosen[-1]] + 1 == mapping[string[i]]: 
            sub1 = hel(chosen + string[i], i + 1) 
            sub2 = hel(chosen, i + 1) 
            if len(sub1) > len(sub2):
                res = sub1
            else:
                res = sub2 
        else: 
            res = hel(chosen, i + 1) 
  
        memo[hashable] = res 
        return res 
  
    mapping = {x: i for i, x in enumerate("aeiou")} 
    memo = {} 
    return hel()

print(len(longest_subsequence(s)))