def get_hour_minutes(time):
  removed_time_period = time.split()[0]
  split_time = removed_time_period.split(":")
  hour = int(split_time[0])
  minutes = int(split_time[1])

  return hour, minutes

def get_weekday(day, added_days):
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  i = days.index(day.lower())

  weekday = days[(i + added_days) % len(days)].capitalize()
  

  return weekday



def is_next_day(added_days):
  if added_days == 1:
    return True
  else:
    return False

def is_PM(period):
  if period == "PM":
    return True
  else:
    return False

def is_noon(hours):
  if hours == 12:
    return True
  
  else:
    return False

def is_midnight(hours):
  if hours == 0:
    return True
  else:
    return False

def get_period(hours):
  if hours >= 12:
    period = "PM"
  
  else:
    period = "AM"
  
  return period

def get_time_string(hours, minutes, period):
  if is_PM(period):
    if is_noon(hours):
      pass
    else:
      hours -= 12
  
  if is_midnight(hours):
    hours += 12
    
  hours_string = str(hours)
  mins_string = str(minutes).rjust(2, "0")

  time_string = hours_string + ":" + mins_string + " " + period

  return time_string

def is_new_hour(minutes):
  if minutes > 59:
    return True

  else:
    return False

def not_same_day(hours):
  if hours > 23:
    return True
  
  else:
    return False

def to_24h_format(hours, minutes, period):
  if is_PM(period):
    hours = 12 + hours
  
  return hours, minutes

def add_time(start, duration, day = None):
  hrs, mins = get_hour_minutes(start)
  period_0 = start.split()[1]
  hrs_0, mins_0 = to_24h_format(hrs, mins, period_0)


  added_hrs, added_mins = get_hour_minutes(duration)

  end_mins = mins_0 + added_mins

  if is_new_hour(end_mins):
    added_hrs += 1
    end_mins -= 60

  
  end_hrs = hrs_0 + added_hrs

  if not_same_day(end_hrs):
    added_days = end_hrs // 24
    end_hrs -= added_days * 24
    is_new_day = True
  else:
    is_new_day = False
    added_days = 0


  end_period = get_period(end_hrs)

  new_time = get_time_string(end_hrs, end_mins, end_period)

  if day:
    weekday = get_weekday(day, added_days)
    new_time += ", %s" % weekday

  if is_new_day:
    if is_next_day(added_days):
      new_time += " (next day)"
    else: 
      new_time += " (%d days later)" % added_days
  

  return new_time
