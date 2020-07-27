import PySimpleGUI as sg
from list import coursesList
from lerMural import getAnnouncements
from teachers import getName
from mural import publicar

turmas = []
ids = []

def enviar(values):
    mensagem = values['msgML']
    print(mensagem)
    i = turmas.index(values['curso'])
    cId = ids[i]
    return publicar(cId, mensagem)

def jmural():
    sg.theme('Reddit')
    sg.SetOptions(element_padding=(2, 5))
    sg.PopupAnimated(
        'professor.png',
        message='JClass - Ajudando professores\nIcons made by photo3idea_studio\nhttps://www.flaticon.com/authors/photo3idea-studio',
        font='Noto 12'
    )
    sg.time.sleep(7)
    sg.PopupAnimated(None)
    lista = coursesList()
    for l in lista:
        for e in l.keys():
            turmas.append(e)
        for v in l.values():
            ids.append(v)
    #print(nomes)
    #print(ids)
    ML_KEY = '-MLINE-' + sg.WRITE_ONLY_KEY

    enviar_layout = [
        [sg.Text(text='Compartilhe algo com sua turma: ', font='Noto 14', background_color='white')],
        [sg.Multiline(default_text="", size=(80, 10), background_color='white', border_width=1, key='msgML',
                      font='Noto 12')],
        [sg.Button('Enviar', border_width=0, font='Noto 12'), sg.Text('', key='result', size=(15, 1), font='Noto 12',
                                                                      text_color='Red')]
    ]

    consultar_layout = [
        [sg.Text('Escolha a turma, a quantidade de mensagens para exibir, em seguida clique em atualizar',
                 border_width=0,font='Noto 14')],
        [sg.Text('Escolha quantas mensagens exibir',font='Noto 14'),
         sg.OptionMenu([5,10,15,20]),
         sg.Button('Atualizar',border_width=0,size=(10,1),font='Noto 12')],
        [sg.Multiline(size=(80,20),key=ML_KEY,background_color='white', border_width=1, font='Noto 12')]
    ]
    layout_final = [
        [sg.Text('Turma:',font='Noto 14'),sg.Combo(turmas, key="curso", font='Noto 12', size=(50, 1))],
        [sg.TabGroup([[sg.Tab('Consulta', consultar_layout), sg.Tab('Envio', enviar_layout)]])],
        [sg.Text('Jeimeson R. França - 2020 - jeimesonrf@gmail.com', size=(80, 1), justification='center')],
        [sg.Text('https://sites.google.com/view/jclass/', size=(80, 1),
                justification='center')],
        [sg.StatusBar('', size=(93, 1), key='-SB-')]
    ]

    window = sg.Window('JMural', layout_final,element_justification='center')
    cores = ['lightgrey', 'white']
    while True:
        event, values = window.read()
        #print(event, values)

        if event == sg.WIN_CLOSED:  # always,  always give a way out!
            break
        if event == 'Atualizar':
            window[ML_KEY].update('')
            if values['curso'] == '' :
                window['-SB-'].update('Escolha uma turma')
                sg.popup('Você deve escolher uma turma',
                         non_blocking=False,
                         no_titlebar=True,
                         background_color='lightgray',
                         font='Noto 11')
                window['-SB-'].update('')
                pass
            else:
                window['-SB-'].update('Conversando com os servidores do Google')
                sg.popup(
                    'Vamos aguardar o Google responder',
                    'Estamos buscando as informações no Google\n'+
                    'Carregando o mural da turma selecionada!\n'+
                    'Esta mensagem fechará automaticamente!',
                    auto_close=True,
                    auto_close_duration=7,
                    non_blocking=True,
                    no_titlebar=True,
                    background_color='lightgray',
                    font='Noto 11')
                i = turmas.index(values['curso'])
                cId = ids[i]
                j = 0
                page = values[0]
                msgs = getAnnouncements(cId, page)
                mTemp=''
                for m in msgs:
                    l = j+1
                    #print(m[0][0],m[0][1],' ',m[3][0],m[3][1])
                    updater = 'Mensagem '+str(l)+' carregada'
                    window['-SB-'].update(updater)
                    window[ML_KEY].update('\n'+m[0][0]+' '+m[0][1]+': ',text_color_for_value='darkred',
                                          background_color_for_value=cores[j%2], append=True)
                    if (m[0][0] != m[3][0]) and (m[0][1] != m[3][1]):
                        window[ML_KEY].update('atualizado: '+ m[3][0] + ' ' + m[3][1] + ': ', text_color_for_value='darkred',
                                              background_color_for_value=cores[j % 2], append=True)
                    if m[2] == mTemp:
                        pass
                    else:
                        name = getName(cId, m[2])
                        mTemp = m[2]
                    window[ML_KEY].update(name+'\n\n', text_color_for_value='darkblue',background_color_for_value=cores[j%2], append=True)
                    window[ML_KEY].update(m[1]+'\n\n\n',background_color_for_value=cores[j%2], append=True)

                    j +=1
        if event == 'Enviar':
            #print(values['msg'])
            if values['curso'] =='':
                window['-SB-'].update('Escolha uma turma')
                sg.popup('Você deve escolher uma turma',
                         no_titlebar=True,
                         non_blocking=False,
                         background_color='lightgray',
                         font='Noto 11')
                window['-SB-'].update('')
            elif (values['msgML'] == '') or (values['msgML'] == '\n'):
                window['-SB-'].update('Digite uma mensagem')
                sg.popup('Você deve digitar uma mensagem',
                         no_titlebar=True,
                         non_blocking=False,
                         background_color='lightgray',
                         font='Noto 11')
                window['-SB-'].update('')
            else:
                print(values['msgML'])
                window['-SB-'].update('Conversando com o Google para enviar a mensagem')
                sg.popup('Vamos aguardar o Google responder',
                         'Estamos negociando o envio com o Google',
                         auto_close=True,
                         auto_close_duration=7,
                         non_blocking=True,
                         no_titlebar=True,
                         background_color='lightgray',
                         font='Noto 11')
                msg_enviar = enviar(values)
                if msg_enviar == 'Publicado':
                    window['-SB-'].update('Mensagem enviada ao mural da turma '+values['curso'])
                else:
                    sg.popup('Algo deu errado')
                    window['-SB-'].update(msg_enviar)

if __name__ == '__main__':
    jmural()