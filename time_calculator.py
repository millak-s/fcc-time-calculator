def day_statement(num_days):
    day = " (next day)" if num_days == 1 else ""
    return f" ({num_days} days later)" if num_days > 1 else day


def day_finder(day, num_days, week_days):
    day = (",".join(day)).capitalize()
    i = week_days.index(day) if day in week_days else 0

    while num_days > 0:
        i += 1
        num_days -= 1
        i = 0 if i >= len(week_days) else i
    return week_days[i]


def add_time(start, duration, *day):
    week_days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    l, meridiem = start.split(" ")
    h, m = l.split(":")
    dh, dm = duration.split(":")
    morning, evening = ["AM", "PM"]
    hours = int(h)
    minutes = int(m) + int(dm) + (int(dh) * 60)
    num_days = 0

    while minutes >= 60:
        minutes -= 60
        hours += 1
        if hours == 12:
            meridiem = morning if meridiem == evening else evening
            num_days += 1 if meridiem == morning else 0
        hours -= 12 if hours > 12 else 0

    minutes = f"0{minutes}" if len(str(minutes)) < 2 else minutes
    day = f", {day_finder(day, num_days, week_days)}" if day else ""
    num_days_statement = day_statement(num_days)
    return f"{hours}:{minutes} {meridiem}{day}{num_days_statement}"
