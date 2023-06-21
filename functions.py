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