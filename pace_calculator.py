import PySimpleGUI as sg

from functions import distance_calculator, duration_calculator, pace_calculator

sg.theme('LightGreen6')
options = {
    'font':('Helvetica', 20, 'bold'),
    'title_color':'grey',
    'tab_background_color':'green',
    'selected_title_color':'white',
    'selected_background_color':'lightgreen',
    'enable_events':True,
    'tab_location':'topleft',
}

pace_tab_layout =  [
    [sg.T('Distance in meters:')],
    [sg.InputText(default_text=0, key='distance'), sg.T('meters')],
    [sg.T('Duration:')],
    [sg.InputText(default_text=0, key='duration_min'), sg.T('min'),sg.InputText(default_text=0, key='duration_sec'), sg.T('sec')],
    [sg.B('Calculate Pace', key='calculate_pace')],
    [sg.T('', key='pace_result')]
    ]    

distance_tab_layout =  [
    [sg.T('Pace in min/km:')],
    [sg.InputText(default_text=0, key ='pace_mins'), sg.T('min'),sg.InputText(default_text=0, key='pace_secs'), sg.T('sec')],
    [sg.T('Duration:')],
    [sg.InputText(default_text=0, key='duration_min2'), sg.T('min'),sg.InputText(default_text=0, key='duration_sec2'), sg.T('sec')],
    [sg.B('Calculate Distance', key='calculate_distance')],
    [sg.T('', key='distance_result')]
    ]   

duration_tab_layout =  [
    [sg.T('Pace in min/km:')],
    [sg.InputText(default_text=0, key ='pace_mins2'), sg.T('min'),sg.InputText(default_text=0, key='pace_secs2'), sg.T('sec')],
    [sg.T('Distance:')],
    [sg.InputText(default_text=0, key='distance2'), sg.T('meters')],
    [sg.B('Calculate Duration', key='calculate_duration')],
    [sg.T('', key='duration_result')]
    ]   

layout = [
    [sg.TabGroup([
        [sg.Tab('Calculate Pace', pace_tab_layout),sg.Tab('Calculate Distance', distance_tab_layout),sg.Tab('Calculate Duration', duration_tab_layout)]])],
        [sg.Button('Exit', key='close')]]    

window = sg.Window('Running Calculator', layout, default_element_size=(12,1))    

while True:    
    event, values = window.read()    
    print(event,values)    
    if event == sg.WIN_CLOSED or event=='close':
        break  

    elif event == 'calculate_pace':
        try:
            pace_in_s = pace_calculator(
                values['duration_min'],
                values['duration_sec'],
                values['distance']
            )
            pace_min = int(pace_in_s//60)
            pace_sec = int(pace_in_s - 60*pace_min)
            pace_res = f'{pace_min} min {pace_sec} s'
            window['pace_result'].update(value=pace_res)
        except ValueError:
            sg.popup('All inputs must be digits 0-9')    
        continue

    elif event =='calculate_distance':
        try:
            dist = distance_calculator(
                values['pace_mins'], 
                values['pace_secs'],
                values['duration_min2'],
                values['duration_sec2'])
            dist_formated = f'{int(dist)} meters'
            window['distance_result'].update(value=dist_formated)
            print(dist)
        except ValueError:
            sg.popup('All inputs must be digits 0-9')
        continue

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
            window['duration_result'].update(value=duration_res)

        except ValueError:
            sg.popup('All inputs must be digits 0-9')   
        continue

window.close()