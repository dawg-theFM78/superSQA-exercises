import time
timer_set = input('Enter yout time in seconds: ')
timer_set = int(timer_set)
print('Countdown begins')
for i in range(timer_set):
    print(f'{timer_set - i}s')
    time.sleep(1)
print('Your time is over')