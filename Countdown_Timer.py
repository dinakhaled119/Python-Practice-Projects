import time

print('======================')
print('  Countdown Timer ⏱')
print('======================')

countdown = int(input('Seconds to countdown timer: '))

for i in range(countdown,0,-1):
    print(f'\rTime remaining: {i} seconds', end='')
    time.sleep(1)

print("\nTime's up! ⌛")
