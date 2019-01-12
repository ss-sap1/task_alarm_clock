'''
для сна надо X минут. ложимся спать после полуночи в H часов и M минут.
на какое время поставить будильник, чтобы он прозвенел ровно через X минут после того, как ляжем спать.
Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.
 Input1: 480 1 2, Output1: 9 2
 Input2: 475 1 55, Output2: 9 50
 '''

# total_sleep_mins = int(input())
total_sleep_mins = 480
hours_to_sleep = 1
mins_to_sleep = 2
translated_hours_to_sleep = int(hours_to_sleep * 60)
sum_mins_to_sleep = translated_hours_to_sleep + mins_to_sleep + total_sleep_mins
hours_alarm_clock = int(sum_mins_to_sleep / 60)
mins_alarm_clock = int(sum_mins_to_sleep % 60)

print(hours_alarm_clock)
print(mins_alarm_clock)

