num = input('Enter a number (decimal only): ')

dot_pos = num.find(".")
new_num = num[dot_pos + 1:]
dp = len(new_num)

print('The number', num, 'has', dp, 'decimal places.')