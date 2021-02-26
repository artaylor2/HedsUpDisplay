import PySimpleGUI as sg

sg.theme('Dark Amber')

# All the stuff inside the window
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the window
window = sg.Window('Window Title', layout)

# Event loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered: ', values[0])

window.close()