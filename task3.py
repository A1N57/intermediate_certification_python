from datetime import datetime, timedelta

def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество дней от текущей даты.
    """
    today = datetime.now()
    future_date = today + timedelta(days=days_from_now)
    return future_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    days = 30  # Количество дней для вычисления
    print(f'Date {days} days from now: {future_date(days)}')
