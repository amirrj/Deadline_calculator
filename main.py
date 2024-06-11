from datetime import datetime
import math

while True:

    # get today's date
    today = datetime.now()
    # get deadline date
    userInput = input('Please enter a deadline date and time (dd/mm/yyyy hh:mm): ')

    try:
        # convert date str to datetime object
        dt_object = datetime.strptime(userInput, '%d/%m/%Y %H:%M')
        # check for future date
        if dt_object < today:
            raise ()
    except:
        print('Please enter a future date in the correct format')
        continue

    difference = dt_object - today
    print('Time remaining until your deadline: ')
    print(f'{difference.days} {"day" if difference.days == 1 else "days"}')
    print(f'{math.floor(difference.seconds / 3600)} {"hour" if math.floor(difference.seconds / 3600) == 1 else "hours"}')
    print(f'{math.ceil(difference.seconds / 60) - (math.floor(difference.seconds / 3600) * 60)} {"minute" if math.ceil(difference.seconds / 60) - (math.floor(difference.seconds / 3600) * 60) == 1 else "minutes"}')
    break