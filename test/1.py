def is_lucky(ticket):
    n = len(ticket)
    half = n // 2
    
    left = sum(int(ticket[i]) for i in range(half))
    right = sum(int(ticket[i]) for i in range(half, n))
    
    even_sum = sum(int(ticket[i]) for i in range(0, n, 2))
    odd_sum = sum(int(ticket[i]) for i in range(1, n, 2))
    
    return left == right and even_sum == odd_sum

def count_lucky_tickets(n):
    count = 0
    max_number = 10 ** n
    
    for number in range(max_number):
        ticket = str(number).zfill(n)
        if is_lucky(ticket):
            count += 1
            
    return count

n = int(input())
print(count_lucky_tickets(n))


