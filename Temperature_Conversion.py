temp = int(input('Enter the Temperature: '))
unit = input('Is it in Celsius or Fahrenheit (C/F): ')

if unit in ['C', 'c']:
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'The temperature is {temp}°F')
elif unit in ['F', 'f']:
    temp = round((temp - 32) * 5 / 9, 1)
    print(f'The temperature is {temp}°C')
else:
    print(f'{unit} is an invalid unit of measurement.')
