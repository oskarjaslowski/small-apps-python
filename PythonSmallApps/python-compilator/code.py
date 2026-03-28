import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['km to mile','miles to km','pounds to kg','kg to pound','sec to min','min to sec'], key = '-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-'),
    ],
    [sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window("Converter",layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214,2)
                    output_string = f'{input_value} kilometers are {output} miles.'
                case 'miles to km':
                    output = round(float(input_value) / 0.6214,2)
                    output_string = f'{input_value} miles are {output} kilometers.'
                case 'pounds to kg':
                    output = round(float(input_value) / 2,20462,2)
                    output_string = f'{input_value} pounds are {output} kilograms.'
                case 'kg to pound':
                    output = round(float(input_value) * 2,20462,2)
                    output_string = f'{input_value} kilograms are {output} pounds.'
                case 'sec to min':
                    output = round(float(input_value) / 60,2)
                    output_string = f'{input_value} seconds are {output} minutes.'
                case 'min to sec':
                    output = round(float(input_value) * 60,2)
                    output_string = f'{input_value} minutes are {output} seconds.'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')

window.close()