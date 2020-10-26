print('Hello, user!')

number = int(input('Enter the number of seconds to convert it in HH:MM:SS format.\n>>>'))

hours = int(number / 60**2)
hours_sec = hours * 60**2

minutes = int((number - hours_sec) / 60)
minutes_sec = minutes * 60

seconds = number - (hours_sec + minutes_sec)

time = f'The result is: {hours}:{minutes}:{seconds}.'
print(time)

