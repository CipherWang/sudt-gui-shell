import PySimpleGUI as sg


layout = [[sg.Text('My one-shot window.')],      
          [sg.InputText(), sg.Drop(values=('BatchNorm', 'other'), )],      
          [sg.Submit(), sg.Cancel()]]      
sg.theme('SystemDefault')

window = sg.Window('CKB sUDT issuance GUI', layout)    

event, values = window.read()    
window.close()

text_input = values[0]
sg.popup('You entered', text_input)