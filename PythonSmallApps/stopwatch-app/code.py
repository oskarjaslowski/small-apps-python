import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('Black')
    layout = [
        [sg.Push(), sg.Image ('x.png', pad = 0, enable_events = True, key = '-CLOSE-')],
        [sg.VPush()],
        [sg.Text('TIME', font = 'Impact 100', key = '-TIME-')],
        [sg.Button('Start', button_color = ('#FFFFFF','#666666'), font = 'Impact 15', border_width = 0, key = '-START-'),
        sg.Button('Lap', button_color = ('#FFFFFF','#666666'), font = 'Impact 15', border_width = 0, key = '-LAP-', visible = False)],
        [sg.Column([[]], key = '-LAPS-')],
        [sg.VPush()]]
    return sg.Window(
        'StopWatch',
        layout,
        size = (400,800),
        no_titlebar = True,
        element_justification = 'center')

window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-START-':
        if active:
            active = False
            window['-START-'].update('Reset')
            window['-LAP-'].update(visible = False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
            else:
                start_time = time()
                active = True
                window['-START-'].update('Stop')
                window['-LAP-'].update(visible = True)

    if active:
        elapsed_time = round(time() - start_time,1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount, font = 'Impact 10'),sg.VSeparator(),sg.Text(elapsed_time, font = 'Impact 10')]])
        lap_amount += 1
window.close()