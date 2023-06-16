for x in ('(3+24)/(20*50)'):
    try:
        print(int(x))
    except ValueError:
        print(f'{x} is not a integer')