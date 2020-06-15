import doctest

def suma(num1, num2):
    
    """
    Esta función suma num1 con num2
    
    >>> suma(2,3)
    'La suma es:5'
  
        
    """
    
    return "La suma es: " + str(num1 + num2)

def resta(num1, num2):
    
    """Esta función resta num2 a num1"""
    
    return num1 - num2

doctest.testmod()










