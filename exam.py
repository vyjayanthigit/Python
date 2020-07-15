data = 50
try:
    data = data/10
except ZeroDivisionError:
    print('Cannot divide by 0 ', end = '')
finally:
    print('End of program ', end = '')
else:
    print('Division successful ', end = '')