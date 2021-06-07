
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2)  

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1 
    return lucas(n-1) + lucas(n-2)

def sum_series( n , zero = 0, one = 1):
    if n == 0:
        return zero
    if n == 1:
        return one
    return sum_series(n-1,zero,one) + sum_series(n-2,zero,one)


    
   
    

