'''
    프로그래머스 : 주차 요금 계산(카카오)
'''

import math

def fee(minutes, fees):
    # ceil() : 올림하여 정수를 반환
    result = fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]
    return result

def solution(fees, records):
    answer = []
    car_intime = dict()
    parking_time = dict()
    
    for record in records:
        time, num, in_out = record.split()
        hour, minute = time.split(':')
        minutes = int(hour) * 60 + int(minute)
        
        if in_out == 'IN':
            car_intime[num] = minutes
        elif in_out == 'OUT':
            try:
                parking_time[num] += minutes - car_intime[num]
            except:
                parking_time[num] = minutes - car_intime[num]
            del car_intime[num]
    
    # 출차 기록이 없는 차량 처리
    for num, minute in car_intime.items():
        try:
            parking_time[num] += 23*60+59 - minute
        except:
            parking_time[num] = 23*60+59 - minute
    
    sorted_time = sorted(list(parking_time.items()), key=lambda x: x[0])
    for num, times in sorted_time:  
        answer.append(fee(times, fees))
    
    return answer
    
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
# [14600, 34400, 5000]