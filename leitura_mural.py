import PySimpleGUI as sg
from list import coursesList
from lerMural import getAnnouncements
from teachers import getName
i = 0

def janela(title):
    sg.theme('Reddit')
    sg.SetOptions(element_padding=(2, 5))
    lista = coursesList()
    sg.popup('Vamos aguardar o Google responder', 'Estamos buscando as informações no Google\n Carregando suas turmas no Classroom.', auto_close=True,
             auto_close_duration=5, non_blocking=True, no_titlebar=True, )
    #print(lista)
    turmas = []
    ids = []
    for l in lista:
        for e in l.keys():
            turmas.append(e)
        for v in l.values():
            ids.append(v)
    ML_KEY = '-MLINE-' + sg.WRITE_ONLY_KEY
    layout = [
        [sg.Text('Escolha a turma, a quantidade de mensagens para exibir, em seguida clique em atualizar',
                 border_width=0)],
        [sg.Text('Escolha quantas mensagens exibir'),sg.OptionMenu([5,10,15,20])],
        [sg.Combo(turmas, key="curso", font='Noto 12',size=(70,1)), sg.Button('Atualizar',border_width=0,size=(10,1))],
        [sg.Multiline(size=(112,25),key=ML_KEY)],
        [sg.Text('Jeimeson R. França - 2020 - jeimesonrf@gmail.com',size=(112,1), justification='center')],
        [sg.StatusBar('Conectado',key='-SB-',size=(110,1),background_color='lightgray')]
    ]
    window = sg.Window(title, layout,element_justification='center',size=(800,585))
    cores = ['lightgrey','white']
    while True :
        event, values = window.read()
        print(event, values)
        page = values[0]

        if event == sg.WIN_CLOSED :  # always,  always give a way out!
            break

        if event == 'Atualizar':
            window[ML_KEY].update('')
            if values['curso'] == '' :
                window['-SB-'].update('Escolha uma turma')
                sg.popup('Você deve escolher uma turma',non_blocking=False,no_titlebar=True)
                window['-SB-'].update('')
                pass
            else:
                window['-SB-'].update('Conversando com os servidores do Google')
                sg.popup('Vamos aguardar o Google responder','Estamos buscando as informações no Google\nCarregando as mensagens do mural da turma selecionada',auto_close=True, auto_close_duration=7,non_blocking=True,no_titlebar=True)
                i = turmas.index(values['curso'])
                cId = ids[i]
                j = 0
                msgs = getAnnouncements(cId, page)
                mTemp=''
                for m in msgs:
                    l = j+1
                    updater = 'Mensagem '+str(l)+' carregada'
                    window['-SB-'].update(updater)
                    window[ML_KEY].update('\n'+m[0][0]+' '+m[0][1]+': ',text_color_for_value='darkred',
                                          background_color_for_value=cores[j%2], append=True)
                    if m[2] == mTemp:
                        pass
                    else:
                        name = getName(cId, m[2])
                        mTemp = name
                    window[ML_KEY].update(name+'\n\n', text_color_for_value='darkblue',background_color_for_value=cores[j%2], append=True)
                    window[ML_KEY].update(m[1]+'\n\n\n',background_color_for_value=cores[j%2], append=True)
                    j +=1



if __name__ == '__main__':
    janela('JMural by JeimesonRF')