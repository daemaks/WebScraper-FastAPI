import datetime as _dt
import json as _json
from typing import Iterator, Dict

import scraper as _scraper

def _date_range(start: _dt.date, end: _dt.date) -> Iterator[_dt.date]:
    pass
    for n in range(int((end - start).days)):
        yield start + _dt.timedelta(n)

def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for date in _date_range(start_date, end_date):
        month = date.strftime('%B').lower()
        if month not in events:
            events[month] = dict()

        events[month][date.day] = _scraper.events_of_the_day(month, date.day)

    return events

if __name__ == '__main__':
    events = create_events_dict()
    with open('events.json', mode='w') as file:
        _json.dump(events, file, ensure_ascii=False)
