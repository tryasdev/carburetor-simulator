print('введите положение винта - ')
max_speed = 0
while True:
    import random

    otvet = input()
    if otvet == 'откручен':
        rpm = (random.randint(0, 1500))
        max_speed = 0
        print('обороты упали! обороты и максимальная скорость', rpm, max_speed )
        if rpm < 800:
            print('квадроцикл заглох! карбюратор плюется бензином.')
            break
    elif otvet == 'закручен':
        rpm = (random.randint(3000, 5000))
        max_speed = (random.randint(40, 50))
        print('обороты выросли! обороты и максимальная скорость -', rpm, max_speed )
        if rpm > 4500:
            print('ВЫРУБАЙ ОРЕТ!!!!')
            break
    elif otvet == 'норма':
        rpm = (random.randint(1500, 2500))
        max_speed = random.randint(65, 75)
        print('стабильные обороты!, обороты и максимальная скорость -', rpm, max_speed )
        if rpm >= 1800 and rpm <= 2200:
            print('идеально!')
    else:
        print('Винт сорван!!')


