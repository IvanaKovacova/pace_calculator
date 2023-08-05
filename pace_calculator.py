import PySimpleGUI as sg

from functions import distance_calculator, duration_calculator, pace_calculator

# for first page layout
choose_label = sg.Text('What do you want to calculate?')
selections = sg.Combo(['Pace', 'Distance', 'Duration'], key='selections')
select_button = sg.Button('Select', key = 'select')
close_button = sg.Button('Close', key='close')

main_layout = [
    [choose_label],
    [selections], [select_button],
    [close_button]
]

# for calculate pace layout
distance_label = sg.Text('Distance in meters:')
dist_input = sg.InputText(default_text=0, key='distance')
dist_label = sg.Text('meters')
duration_label = sg.Text('Duration:')
duration_min = sg.InputText(default_text=0, key='duration_min')
duration_sec = sg.InputText(default_text=0, key='duration_sec')
duration_min_label = sg.Text('min')
duration_sec_label = sg.Text('sec')

calculate_pace_button =  sg.Button('Calculate Pace', key='calculate_pace')
pace_result = sg.Text('', key='pace_result')

pace_layout = [
    [distance_label],
    [dist_input, dist_label],
    [duration_label], 
    [duration_min, duration_min_label, duration_sec, duration_sec_label],
    [calculate_pace_button],
    [pace_result]
]

# for calculate distance layout
calculate_distance_button = sg.Button('Calculate Distance', key='calculate_distance')
distance_result = sg.Text('', key='distance_result')

pace_label = sg.Text('Pace in min/km:')
pace_min_input = sg.InputText(default_text=0, key ='pace_mins')
pace_min_label = sg.Text('min')
pace_sec_input = sg.InputText(default_text=0, key='pace_secs')
pace_sec_label = sg.Text('sec')

duration_label2 = sg.Text('Duration:')
duration_min2 = sg.InputText(default_text=0, key='duration_min2')
duration_sec2 = sg.InputText(default_text=0, key='duration_sec2')
duration_min_label2 = sg.Text('min')
duration_sec_label2 = sg.Text('sec')

distance_layout = [
    [pace_label],
    [pace_min_input, pace_min_label, pace_sec_input, pace_sec_label],
    [duration_label2], 
    [duration_min2, duration_min_label2, duration_sec2, duration_sec_label2],
    [calculate_distance_button],
    [distance_result]
]

# for calculate duration layout
calculate_duration_button = sg.Button('Calculate Duration', key='calculate_duration')
duration_result = sg.Text('', key='duration_result')

pace_label2 = sg.Text('Pace in min/km:')
pace_min_input2 = sg.InputText(default_text=0, key ='pace_mins2')
pace_min_label2 = sg.Text('min')
pace_sec_input2 = sg.InputText(default_text=0, key='pace_secs2')
pace_sec_label2 = sg.Text('sec')

distance_label2 = sg.Text('Distance in meters:')
dist_input2 = sg.InputText(default_text=0, key='distance2')
dist_label2 = sg.Text('meters')

duration_layout = [
    [pace_label2],
    [pace_min_input2, pace_min_label2, pace_sec_input2, pace_sec_label2],
    [distance_label2],
    [dist_input2, dist_label2],
    [calculate_duration_button],
    [duration_result]
]


window = sg.Window(
    'Calculator',
    layout= main_layout
)
# create a popup that shows on selection
while True: 
    event, values = window.read()
    print(event)
    print(values)
    if event == 'close' or event == sg.WIN_CLOSED:
        break

    elif values['selections'] == 'Pace':
        window2= sg.Window(
            'Calculate Pace',
            layout = pace_layout
        )
        while True:
            event, values = window2.read()
            print(event)
            print(values)
            if event == sg.WIN_CLOSED:
                break
            elif event =='calculate_pace':
                try:
                    pace_in_s = pace_calculator(
                        values['duration_min'],
                        values['duration_sec'],
                        values['distance']
                    )
                    pace_min = int(pace_in_s//60)
                    pace_sec = int(pace_in_s - 60*pace_min)
                    pace_res = f'{pace_min} min {pace_sec} s'
                    window2['pace_result'].update(value=pace_res)
                except ValueError:
                    sg.popup('All inputs must be digits 0-9')    
                continue

            window2.close()

    elif values['selections'] == 'Distance':
        window2= sg.Window(
            'Calculate Distance',
            layout = distance_layout
        )
        while True:
            event, values = window2.read()
            print(event)
            print(values)
            if event == sg.WIN_CLOSED:
                break
            elif event =='calculate_distance':
                try:
                    dist = distance_calculator(
                        values['pace_mins'], 
                        values['pace_secs'],
                        values['duration_min2'],
                        values['duration_sec2'])
                    dist_formated = f'{dist} meters'
                    window2['distance_result'].update(value=dist_formated)
                    print(dist)
                except ValueError:
                    sg.popup('All inputs must be digits 0-9')
                continue

            window2.close()


    elif values['selections'] == 'Duration':
        window2= sg.Window(
            'Calculate Duration',
            layout = duration_layout
        )
        while True:
            event, values = window2.read()
            print(event)
            print(values)
            if event == sg.WIN_CLOSED:
                break
            elif event =='calculate_duration':
                try:
                    dur_in_s = duration_calculator(
                        values['pace_mins2'], 
                        values['pace_secs2'], 
                        values['distance2']
                        )
                    duration_mins = int(dur_in_s//60)
                    duration_secs = int(dur_in_s - 60*duration_mins)
                    duration_res = f'{duration_mins} min {duration_secs} s'
                    window2['duration_result'].update(value=duration_res)
  
                except ValueError:
                    sg.popup('All inputs must be digits 0-9')   
                continue

            window2.close()

window.close()