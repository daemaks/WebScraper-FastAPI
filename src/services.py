from typing import Dict
import json as _json
import datetime as _dt

def get_all_events() -> Dict:
    with open('events.json') as file:
        data = _json.load(file)

    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    try:
        month_events = events[month.lower()]
        return month_events
    except KeyError:
        return 'this month isn`t real'

def get_day_events(month: str, day: int) -> Dict:
    events = get_all_events()
    try:
        day_events = events[month.lower()][str(day)]
        return day_events
    except KeyError:
        return 'this month or day is fake'

def get_events_of_today():
    today = _dt.date.today()
    month = today.strftime('%B')
    day = str(today.day)
    return get_day_events(month, day)