import PySimpleGUI as sg
from mural import publicar
from list import coursesList

nomes = []
ids = []

def enviar(values):
    mensagem = values['msg']
    print(mensagem)
    i = nomes.index(values['curso'])
    cId = ids[i]
    return publicar(cId, mensagem)


def janela(title, course):
    sg.theme('Reddit')
    sg.SetOptions(element_padding=(2, 5))
    lista = coursesList()
    print(lista)
    for l in lista:
        for e in l.keys():
            nomes.append(e)
        for v in l.values():
            ids.append(v)
    print(nomes)
    print(ids)
    layout = [
        [sg.Text(text='Compartilhe algo com sua turma: '+course, font='Noto 14',background_color='white')],
        [sg.Combo(nomes,key="curso",font='Noto 12',size=(80,1))], #,sg.Button('Teste')],
        [sg.Multiline(default_text="",size=(80,10),background_color='white',border_width=1,key='msg',font='Noto 12')],
        [sg.Button('Enviar',border_width=0,font='Noto 12'),sg.Text('',key='result',size=(15,1),font='Noto 12',
                                                                   text_color='Red')],
        [sg.StatusBar('',size=(80,1),key='-SB-')]
    ]
    window = sg.Window(title, layout, default_element_size=(20, 1),size=(600,340))

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:  # always,  always give a way out!
            break

        if event == 'Enviar':
            #print(values['msg'])
            if values['curso'] =='':
                window['-SB-'].update('Escolha uma turma')
                sg.popup('Você deve escolher uma turma',no_titlebar=True,non_blocking=False,background_color='lightgray')
                window['-SB-'].update('')
            else:
                window['-SB-'].update('Conversando com o Google para enviar a mensagem')
                window['result'].update('Processando')
                msg = enviar(values)
                window['result'].update(msg)
                if msg == 'Publicado':
                    window['-SB-'].update('Mensagem enviada ao mural da turma '+values['curso'])
                else:
                    window['-SB-'].update('Algo deu errado: '+msg)

def main():
    janela("JClass.JPost", "")


if __name__ == '__main__':
    main()