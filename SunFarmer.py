import PySimpleGUI as sg
import main_func

sg.theme('LightBlue')

win_count = 0
name_flore = ""

def sseer():
    while True:
        print(1)

layout = [

          [sg.pin(sg.Text(text="AUTOFARMER", font=("normal"), pad=(20,1)))],
          [sg.pin(sg.Input(key="_input_", size=(21, 1), tooltip="Введите количество окон с фермами", visible=False))],
          [sg.pin(sg.Text(text="Введите число > 0", visible=False, key="_warn_"))],
          [sg.pin(sg.Button(button_text="ОКЕЙ", size=(16, 1), font=("normal"), key="_ok_", visible=False))],
          [sg.pin(sg.Button(button_text="emperty", size=(16, 1), font=("normal"), button_color="#66CC66", key="new", visible=False, disabled=True, disabled_button_color="White"))],
          [sg.pin(sg.Button(button_text="YES", size=(16, 1), font=("normal"), key="_yes_", visible=False))],
          [sg.pin(sg.Button(button_text="NO", size=(16, 1), font=("normal"), key="_no_", visible=False))],
          [sg.pin(sg.Button(button_text="CANCEL", size=(16, 1), font=("normal"), button_color="#E96D71", key="_cancel_", visible=False))],
          [sg.pin(sg.Button(button_text="Sunflower", size=(16, 1), font=("normal"), key="sunflower"))],
          [sg.pin(sg.Button(button_text="Potato", size=(16, 1), font=("normal"), key="potato"))],
          [sg.pin(sg.Button(button_text="Pumpkin", size=(16, 1), font=("normal"), key="pumpkin"))],
          [sg.pin(sg.Button(button_text="Carrot", size=(16, 1), font=("normal"), key="carrot"))],
          [sg.pin(sg.Button(button_text="Cabbage", size=(16, 1), font=("normal"), key="cabbage"))],
          [sg.pin(sg.Button(button_text="EXIT", size=(16, 1), font=("normal"), button_color="#E96D71", key="_exit_"))],
          [sg.pin(sg.Text(text="by @asynco", key="auth"))],
          [sg.pin(sg.Image(source="house.png", pad=(20,1), key="butt8"))]

          ]

window = sg.Window('SunFarmer by @asynco', layout, element_justification="c")

while True:
    flag = False
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "_exit_"):
        break

    elif event == "_yes_":
        flag = True

        window['sunflower'].Update(visible=False)
        window['potato'].Update(visible=False)
        window['pumpkin'].Update(visible=False)
        window['carrot'].Update(visible=False)
        window['cabbage'].Update(visible=False)
        window['auth'].Update(visible=False)
        window['_exit_'].Update(visible=False)
        window['new'].Update(f"{event.capitalize()}", visible=False)
        window['_yes_'].Update("YES", visible=False)
        window['_no_'].Update("NO", visible=False)

    elif event == "_no_" or event == "_cancel_":
        window['sunflower'].Update(visible=True)
        window['potato'].Update(visible=True)
        window['pumpkin'].Update(visible=True)
        window['carrot'].Update(visible=True)
        window['cabbage'].Update(visible=True)
        window['_exit_'].Update(visible=True)

        window['_input_'].Update(visible=False)
        window['_ok_'].Update(visible=False)
        window['_cancel_'].Update(visible=False)

        window['new'].Update(f"{event.capitalize()}", visible=False)
        window['_yes_'].Update("YES", visible=False)
        window['_no_'].Update("NO", visible=False)
        window['_warn_'].Update(visible=False)

    elif event in ('sunflower', 'potato', 'pumpkin', 'carrot', 'cabbage'):
        window['sunflower'].Update(visible = False)
        window['potato'].Update(visible = False)
        window['pumpkin'].Update(visible = False)
        window['carrot'].Update(visible = False)
        window['cabbage'].Update(visible = False)
        window['_exit_'].Update(visible = False)

        window['_input_'].Update(visible=True)
        window['_ok_'].Update(visible=True)
        window['_cancel_'].Update(visible=True)

        flower_choice = event.capitalize()

    elif event in ('_ok_'):
        if values['_input_'] != "" and int(values['_input_']) > 0:
            window['_input_'].Update(visible=False)
            window['_ok_'].Update(visible=False)
            window['_cancel_'].Update(visible=False)
            window['_warn_'].Update(visible=False)

            window['new'].Update(f"{int(values['_input_'])} {flower_choice}", visible=True)
            window['_yes_'].Update("YES", visible=True)
            window['_no_'].Update("NO", visible=True)

            win_count = int(values['_input_'])
            name_flore = flower_choice

        else:
            print("Пустое значение")
            window['_warn_'].Update(visible=True)

    if flag:
        break

if name_flore != None and values['_input_'] != None and values['_input_'] != '' and name_flore != "_exit_":
    main_func.farmer(flower_name=name_flore.lower(), win_count=int(win_count))
else:
    print("Введено неверное значение, ошибка")