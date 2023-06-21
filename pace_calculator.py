import PySimpleGUI as sg
from functions import distance_calculator, duration_calculator, pace_calculator

pace_label = sg.Text('Pace in min/km:')
pace_min_input = sg.InputText(default_text=0, key ='pace_mins')
pace_min_label = sg.Text('min')
pace_sec_input = sg.InputText(default_text=0, key='pace_secs')
pace_sec_label = sg.Text('sec')
calculate_pace_button =  sg.Button('Calculate Pace', key='calculate_pace')


distance_label = sg.Text('Distance in meters:')
dist_input = sg.InputText(default_text=0, key='distance')
dist_label = sg.Text('meters')
calculate_distance_button = sg.Button('Calculate Distance', key='calculate_distance')


duration_label = sg.Text('Duration:')
duration_min = sg.InputText(default_text=0, key='duration_min')
duration_sec = sg.InputText(default_text=0, key='duration_sec')
duration_min_label = sg.Text('min')
duration_sec_label = sg.Text('sec')
calculate_duration_button = sg.Button('Calculate Duration', key='calculate_duration')


close_button = sg.Button('Close', key='close')

window = sg.Window(
    'Pace Calculator',
    layout= [
        [pace_label],
        [pace_min_input, pace_min_label, pace_sec_input, pace_sec_label],
        [calculate_pace_button],
        [distance_label],
        [dist_input, dist_label],
        [calculate_distance_button],
        [duration_label], 
        [duration_min, duration_min_label, duration_sec, duration_sec_label],
        [calculate_duration_button],
        [close_button]
    ]
)

while True:
    event, values = window.read()

    #print(event)
    #print(values)

    if event == 'calculate_duration':

        dur_in_s = duration_calculator(
            values['pace_mins'], 
            values['pace_secs'], 
            values['distance']
            )
        duration_mins = int(dur_in_s//60)
        duration_secs = int(dur_in_s - 60*duration_mins)
        window['duration_min'].update(value=duration_mins)
        window['duration_sec'].update(value=duration_secs)

    elif event == 'calculate_distance':

        dist = distance_calculator(
            values['pace_mins'], 
            values['pace_secs'],
            values['duration_min'],
            values['duration_sec'])
        window['distance'].update(value=dist)

    elif event == 'calculate_pace':

        pace_in_s = pace_calculator(
            values['duration_min'],
            values['duration_sec'],
            values['distance']
        )
        pace_min = int(pace_in_s//60)
        pace_sec = int(pace_in_s - 60*pace_min)
        window['pace_mins'].update(value=pace_min)
        window['pace_secs'].update(value=pace_sec)        

    elif event == 'close' or event == sg.WIN_CLOSED:
        break

window.close()