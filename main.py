from datetime import datetime, date




def get_birthdays_per_week(users):
    today = date.today() #актуальна дата

    if today.weekday() == 0:
        today = today.replace(day=today.day - 2)
    elif today.weekday() == 6:
        today = today.replace(day=today.day - 1)
    # Ми зробили зміну дня тижня для того щоб в понеділок ми бачили повідомлення за суботу та неділю

    user_list = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    for user in users:
        newdate = date(
            year=today.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day)
        interval = newdate - today
    # змінюємо рік народження на актуальний для того щоб шукати лише по місяцю та даті, та знаходимо интервал між датами

        if interval.days >=0 and interval.days < 7:
            weekdays = newdate.strftime("%A")
            if weekdays in ["Saturday","Sunday"]:
                weekdays = "Monday"
            user_list.get(weekdays).append(user.get("name"))

    print_users_list(user_list)

def print_users_list(users_list: dict):
    for key, value in users_list.items():
        if value:
            print(f"{key}: {', '.join(value)}")




if __name__ == '__main__':
    get_birthdays_per_week(users)
