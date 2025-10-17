def hm2m(h,m):
    return h*60 + m

def solution(fees, records):
    DEF_TIME, DEF_FEE, UNIT_TIME, UNIT_FEE = fees
    in_times = dict()
    park_times = dict()
    cars = set()
    for record in records:
        time_str, car_num_str, in_out = record.split()
        h, m = map(int,time_str.split(':'))
        car_num = int(car_num_str)
        if in_out == "IN":
            in_times[car_num] = hm2m(h,m)
            cars.add(car_num)
        else:
            ptime = hm2m(h,m) - in_times[car_num]
            in_times.pop(car_num)
            if car_num in park_times:
                park_times[car_num]+=ptime
            else:
                park_times[car_num] = ptime
    for car_num in in_times:
        ptime = hm2m(23,59) - in_times[car_num]
        if car_num in park_times:
            park_times[car_num]+=ptime
        else:
            park_times[car_num] = ptime
    cars = [c for c in cars]
    cars.sort()
    answer = []
    for car in cars:
        ptime = park_times[car]
        if ptime<=DEF_TIME:
            final_fee = DEF_FEE
        else:
            final_fee = DEF_FEE+((ptime-DEF_TIME)//UNIT_TIME)*UNIT_FEE
            if ((ptime-DEF_TIME)%UNIT_TIME) > 0:
                final_fee += UNIT_FEE
        answer.append(final_fee)
    return answer