def solution(price, money, count):
    pay = 0
    for i in range(1, count + 1):
        pay += price * i
    
    pay -= money
    return pay if pay >= 0 else 0