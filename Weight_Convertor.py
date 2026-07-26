Weight convertor
print('~~~~~~~~~~~~~~~~~~~~~~~~')
print('   Weight Convertor 🏋')
print('~~~~~~~~~~~~~~~~~~~~~~~~')

weight = float(input('Enter your weight: '))
unit = input('Kg or Pounds? (K or L): ').strip().lower()

if unit in ['K', 'k']:
    weight = weight * 2.205
    unit = 'lbs'
    print(weight)
elif unit in ['L', 'l']:
    weight = weight / 2.205
    unit = 'Kgs'
    print(weight)
else:
    print(f'{unit} not found!')

print(f'Your weight is: {weight} {unit}.')
