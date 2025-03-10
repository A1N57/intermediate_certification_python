from datetime import datetime

def display_current_datetime():
    # Получение текущего времени и даты
    now = datetime.now()
    # Форматирование даты и времени
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    # День недели и номер недели
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]

    print(f'Current date and time: {formatted_date}')
    print(f'Day of the week: {day_of_week}')
    print(f'Week number: {week_number}')

if __name__ == '__main__':
    display_current_datetime()
