def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

result = function(10, 0) #result will be 0 