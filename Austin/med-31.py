def clock_angle(time):
    (hour, minute) = time.split(":")
    hour_hand = float(hour) * (360.0/12.0) + (float(minute) * (360.0/720.0))
    minute_hand = float(minute) * (360.0/60.0)
    return abs(hour_hand - minute_hand)

print(clock_angle("3:30"))
print(clock_angle("1:15"))
print(clock_angle("12:30"))
