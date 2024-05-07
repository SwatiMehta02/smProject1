def even_numbers(x,y):
    """To find and print even numbers between x and y   

    Args:
        x (int): first number
        y (int): second number
    """
    for i in range(x,y+1):
        if i%2==0:
            print(i," is even")

def is_even(x):
    """returns boolean:true if x is even else false

    Args:
        x (int): first number
    """
    if x%2==0:
        return True
    else:
        return False

