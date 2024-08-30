#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return 
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return
    
    a, b = 0, 1 
    result = [a, b]
    
    while len(result) < length:
        a, b = b, a + b
        result.append(b)
        
    print(result)