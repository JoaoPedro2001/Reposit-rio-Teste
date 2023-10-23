from tkinter import*
import customtkinter

def tela_principal():
    #Configurando a tela principal
    def limpar_nome():
        login.delete(0, END)

    def limpar_senha():
        senha.delete(0, END)

    def conf():
        if login.get() == '' and senha.get() == '':
            mensagem['text'] = ''
        elif login.get() != 'usuario' and senha.get() != '12345':
            mensagem['text'] = 'Usuário e senha incorretos!'
            limpar_nome()
            limpar_senha()
        elif login.get() != 'usuario':
            mensagem['text'] = 'Nome de usuário inválido!'
            limpar_nome()
        elif senha.get() != '12345':
            mensagem['text'] = 'Senha incorreta!'
            limpar_senha()
        else:
            janela.withdraw()
            janela1 = Toplevel()
            janela1.title('Bem vindo')
            janela1.geometry('1200x500+100+50')
            janela1.iconbitmap('icone.ico')
            janela1.resizable(width=False, height=False)

            janela1.mainloop()

    janela = customtkinter.CTk()
    janela.title('Sistema de Login')
    janela._set_appearance_mode('dark')
    janela.geometry('1030x500+100+50')
    janela.iconbitmap('user_ico.ico')
    janela.resizable(width=False, height=False)

    imagem = PhotoImage(file='foto1.png')
    label_imagem = Label(janela, image=imagem)
    label_imagem.pack()

    titulo_principal = customtkinter.CTkLabel(janela,
                                              text='Faça login ou se cadastre',
                                              fg_color='#7F39FB',
                                              font=('Arial',25))
    titulo_principal.place(x=150, y=10)

    frame_login = customtkinter.CTkFrame(janela, width=500, height=380, fg_color='lightgrey')
    frame_login.place(x=522, y=80)

    label_titulo = customtkinter.CTkLabel(frame_login,
                                          text='Faça seu login',
                                          font=('Arial',20))
    label_titulo.place(x=190, y=10)

    login = customtkinter.CTkEntry(frame_login, width=300,
                                   placeholder_text='Seu nome',
                                   corner_radius=25)
    login.place(x=100, y=40)

    label_senha = customtkinter.CTkLabel(frame_login,
                                         text='Entre com a senha',
                                         font=('Arial', 20))
    label_senha.place(x=170, y=80)

    senha = customtkinter.CTkEntry(frame_login, width=300,
                                   placeholder_text='Sua senha',
                                   corner_radius=25, show='*')
    senha.place(x=100, y=120)

    botao = customtkinter.CTkButton(frame_login, text='Entrar'.upper(), corner_radius=25, hover_color='black', command=conf)
    botao.place(x=180, y=200)

    mensagem = Label(frame_login, text='', font=('Arial, 15'), fg='black', bg='lightgrey')
    mensagem.place(x=130, y=300)

    janela.mainloop()

tela_principal()