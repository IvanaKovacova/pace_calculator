def duration_calculator(pace_mins, pace_secs, distance):
    pace_in_seconds = float(pace_mins)*60 + float(pace_secs)
    distance_in_kms = float(distance)/1000
    return distance_in_kms*pace_in_seconds

def distance_calculator(pace_mins, pace_secs, duration_mins, duration_secs):
    pace_in_seconds = float(pace_mins)*60 + float(pace_secs)
    duration_in_seconds = float(duration_mins)*60 + float(duration_secs)
    return duration_in_seconds/pace_in_seconds*1000

def pace_calculator(duration_mins, duration_secs, distance):
    distance_in_kms = float(distance)/1000
    duration_in_seconds = float(duration_mins)*60 + float(duration_secs)
    return duration_in_seconds/distance_in_kms

# splits function
def splits_calculator(pace_min, pace_sec, total_distance, splits):
    pace_in_seconds = int(pace_min)*60 + int(pace_sec)
    list_of_distances = list(range(splits, total_distance+1, splits))
    total_seconds = [distance/1000*pace_in_seconds for distance in list_of_distances]
    mins = [int(seconds/60) for seconds in total_seconds]
    sec = [int(seconds%60) for seconds in total_seconds]

    position = 0
    duration_list = []
    while position < len(mins):
        if mins[position] == 0:
            duration = f'{sec[position]}s'
        elif sec[position] == 0:
            duration = f'{mins[position]}min'
        else:
            duration = f'{mins[position]}min {sec[position]}s'
        duration_list.append(duration)
        position +=1

    return list_of_distances, duration_list

def speed_calculator(pace_min, pace_sec):
    pace_in_min = pace_min + pace_sec/60
    speed = 60/pace_in_min
    return round(speed, 1)

def pace_from_speed(speed):
    speed = float(speed)
    pace_min = int(60/speed)
    pace_sec = int((60/speed - pace_min) * 60)
    return f'{pace_min} min {pace_sec} sec'

if __name__ == '__main__':
    sap = pace_from_speed(12.4)
    print(sap)

