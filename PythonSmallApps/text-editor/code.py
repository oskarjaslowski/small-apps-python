import PySimpleGUI as sg
from pathlib import Path

sentences = [
    'Poems',['Life me, me','Roses are violet sometimes','Lungs full of cigarette smoke'],
    'Quotes',['Set yourself free','Keep going','Chose to shine','No pain No gain']
]
sentences_events = sentences[1] + sentences[3]

lennyfaces = [
    'Basic',['( ͡° ͜ʖ ͡°)','( ͠° ͟ʖ ͡°)','( ͡ʘ ͜ʖ ͡ʘ)','( ͡° ʖ̯ ͡°)'],
    'Fight',['(ง ͠° ͟ل͜ ͡°)ง','(╯ ͠° ͟ʖ ͡°)','( ͡° ͜ʖ ͡°)╭∩╮','ᕦ( ͡° ͜ʖ ͡°)ᕤ'],
    'Weird',['ಠ_ಠ','(✿❦ ͜ʖ ❦)']
]
lenny_events = lennyfaces[1] + lennyfaces[3] + lennyfaces[5]

menu_layout = [
    ['File',['Open','Save','---','Exit']],
    ['Tools',['Word Count','Big Letters','Small Letters','Change Letters']],
    ['Add',sentences],
    ['( ͡° ͜ʖ ͡°)',lennyfaces]]

sg.theme('Dark')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untilted', key = '-DOCNAME-')],
    [sg.Multiline(no_scrollbar = True, size = (40,30), key = '-TEXTBOX-')]
]

window = sg.Window('Text editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        file_path = sg.popup_get_file('open',no_window = True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Save':
        file_path = sg.popup_get_file('Save as',no_window = True, save_as = True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == "Exit":
        window.close()

    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n',' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'words: {word_count}\ncharacters: {char_count}')

    if event == 'Big Letters':
        string = values['-TEXTBOX-']
        newstring = ''
        for a in string:
            if (a.isupper()) == True:
                newstring += (a.upper())
            elif (a.islower()) == True: 
                newstring += (a.upper())
            elif (a.isspace()) == True: 
                newstring += a
        window['-TEXTBOX-'].update(newstring)

    if event == 'Small Letters':
        string = values['-TEXTBOX-']
        newstring = ''
        for a in string:
            if (a.isupper()) == True:
                newstring += (a.lower())
            elif (a.islower()) == True: 
                newstring += (a.lower())
            elif (a.isspace()) == True: 
                newstring += a
        window['-TEXTBOX-'].update(newstring)

    if event == 'Change Letters':
        string = values['-TEXTBOX-']
        newstring = ''
        for a in string:
            if (a.isupper()) == True:
                newstring += (a.lower())
            elif (a.islower()) == True: 
                newstring += (a.upper())
            elif (a.isspace()) == True: 
                newstring += a
        window['-TEXTBOX-'].update(newstring)
    
    if event in sentences_events:
        current_text = values['-TEXTBOX-']
        new_text = current_text + event
        window['-TEXTBOX-'].update(new_text)

    if event in lenny_events:
        current_text = values['-TEXTBOX-']
        new_text = current_text + event
        window['-TEXTBOX-'].update(new_text)

window.close()