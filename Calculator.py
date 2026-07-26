print('====================')
print(' Area Calculator 📐')
print('====================')

print(' 1) Triangle')
print(' 2) Rectangle')
print(' 3) Square')
print(' 4) Circle')
print(' 5) Quit')

answer = int(input('Choose a number: '))
print(answer)



if answer == 1:
    height = int(input('Height: '))
    base = int(input('Base: '))
    triangle = (height * base)/2
    print(f'The area is {triangle}')

elif answer == 2:
    length = int(input('Lenght: '))
    width = int(input('Width: '))
    rectangle = length * width
    print(f'The area is {rectangle}')

elif answer == 3:
    side = int(input('Side: '))
    square = side ** 2
    print(f'The area is {square}')

elif answer == 4:
    radius = int(input('Radius: '))
    circle = 3.14 * radius **2
    print(f'The area is {circle}')

elif answer == 5:
    print('Goodbye!')
    quit()

else:
    print('Error.')


