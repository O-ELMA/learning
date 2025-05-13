import datetime

def add_time(start_time, duration, start_day=''):
    days_of_week = [
        'Monday', 
        'Tuesday', 
        'Wednesday', 
        'Thursday', 
        'Friday', 
        'Saturday', 
        'Sunday'
    ]
    result = ''

    # Handle generating new time
    current_datetime = datetime.datetime.strptime(start_time, '%I:%M %p')

    hours, minutes = map(int, duration.split(':'))
    time_change = datetime.timedelta(hours=hours, minutes=minutes)
    new_datetime = current_datetime + time_change 

    new_time = new_datetime.strftime('%I:%M %p')
    result += new_time.strip('0')

    days_difference = (new_datetime.date() - current_datetime.date()).days
    # Handle generating start date
    if start_day:
        start_day = start_day.capitalize()
        start_index = days_of_week.index(start_day)
        new_index = (start_index + days_difference) % len(days_of_week)
        result += ', ' + days_of_week[new_index]

    # Handle generating days difference
    if days_difference > 1:
        result += f' ({days_difference} days later)'
    elif days_difference == 1:
        result += ' (next day)'
    
    print('result: ', result)
    return result

# Example usage
add_time('11:43 PM', '24:20', 'tueSday')