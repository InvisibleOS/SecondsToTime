def SecondsToTime(time):
    minutes = time // 60
    seconds = time % 60
    hours = minutes // 60
    days = hours // 24
    
    if minutes >= 60:
        minutes = minutes % 60
    if hours >= 24:
        hours = hours % 24
    return [days, hours, minutes, seconds]
