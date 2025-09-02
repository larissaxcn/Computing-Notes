def f(x=1, z=1):
    '''
    Solves the equation: x**2 + x + z
    Input: x (float or int), z (float or int)
    Returns: Solution to equation (float or int)
    '''
    rv = x ** 2 + x + z
    return rv

if __name__ == "__main__":
    # executes only if run as a script
    x = float(input("Enter a value for x: "))
    z = float(input("Enter a value for z: "))
    print("Result for input x={}, z={}. Output:".format(x, z))
    # Alternate approach for string formatting:
    #print(f"Result for input x={x}, z={z}. Output:")
    print(f(x, z))

'''
(base) xuchuning@s-MacBook-Air 05-functions % python example_module.py
Enter a value for x: 1
Enter a value for z: 2
Result for input x=1.0, z=2.0. Output:
4.0
'''

