
def fibonacci(n):
     """
    Recursive function that calculat thn number fibonacci

    Arguments:
        n:integer -- the number of sequence we are looking for
        
    Returns:
        nth Number fo the lucas fibonacci
       
    """
    if n == 0:
        return 0
    if n == 1:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2)  

def lucas(n):
    """
    Recursive function that calculat thn number Lucas

    Arguments:
        n:integer -- the number of sequence we are looking for
        
    Returns:
        nth Number fo the lucas series
       
    """
    if n == 0:
        return 2
    if n == 1:
        return 1 
    return lucas(n-1) + lucas(n-2)

def sum_series( n , zero = 0, one = 1):
    """
    Recursive function that solve a sum series similar to Fibonacci and Lucas

    Arguments:
        n:integer -- the number of sequence we are looking for
        a:optional integer -- value of series at index 0
        b:optional integer -- value of series at index 1

    Returns:
        Number similar to Fibonacci and Lucas series 
        but could be any other math series based on the first two values
    """
    if n == 0:
        return zero
    if n == 1:
        return one
    return sum_series(n-1,zero,one) + sum_series(n-2,zero,one)


    
   
    

