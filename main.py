import time

time_now = time.localtime()
hour = time_now.tm_hour
minute = time_now.tm_min

end_time = (2, 19)

if end_time[1] < minute:
    end_time = (end_time[0], end_time[1] + 60)
    class_time = (end_time[0], end_time[1] - minute)
else:
    class_time = (end_time[0] - hour, end_time[1] - minute)

minutes = class_time[1]

print("Minutes left: " + str(minutes))
