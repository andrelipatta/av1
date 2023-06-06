import PySimpleGUI as sg

sg.theme('Dark Amber') 

layout = [ 
  
              [sg.Text('Índice de massa corpórea')],
              [sg.Text('Massa: '),sg.Input(key='-MASS-' , size=(20,1))],
              [sg.Text('Altura: '),sg.Input(key='-HEIGHT-' , size=(20,1))],
              [sg.Push(),sg.Button('Calcular'),sg.Push()]
          ]
    
    
window = sg.window('IMC', layout=layout, font='Monaco 18')


while True:
    event, value = window.read() 
    print(event, value)
    massa = float(value['-MASS-'])
    altura = float(value['-HEIGHT-'])
    imc = massa/(altura**2)
    sg.Popup(f'SEU IMC É {imc:.2f}' , font='26'
    if event == sg.WIN_CLOSED or event == 'Exit' :
       break

window.close()
