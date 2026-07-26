#Weight convertor
weight = float(input('Enter your weight: '))
unit = input('Kg or Pounds? (K or L): ').strip().lower()

if unit == 'K' or 'k':
    weight = weight * 2.205
    unit = 'LBS'
    print(weight)
elif unit == 'L' or 'l':
    weight = weight / 2.205
    unit = 'Kgs'
    print(weight)
else:
    print(f'{unit} not found!')

print(f'Your weight is: {weight} {unit}.')

