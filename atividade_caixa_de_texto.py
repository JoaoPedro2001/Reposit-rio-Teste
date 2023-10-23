from tkinter import*
from tkinter import ttk
from tkinter import messagebox

ciano = '#00FFFF'
preto = '#000000'
branco = '#FFFFFF'

janela1 = Tk()
janela1.title('Atividade Caixa de Seleção')
janela1['bg'] = ciano
janela1.geometry('400x400+540+150')
janela1.resizable(width=False, height=False)

def janela_secundaria():
    ciano_escuro = '#008B8B'
    preto = '#000000'
    branco = '#FFFFFF'

    janela2 = Toplevel()
    janela2['bg'] = ciano_escuro
    janela2.geometry('600x450+540+150')
    janela2.resizable(width=False, height=False)
    janela1.withdraw()

    def dados_enviados():
        nome = str(cadastro_nome.get())

        if var_genero.get() == 1:
            genero = 'Masculino'
        elif var_genero.get() == 2:
            genero = 'Feminino'
        elif var_genero.get() == 3:
            genero = 'Outro'
        else:
            genero = ''

        estado_civil = str(caixa_selecao.get())
        if estado_civil == 'Escolha a opção':
            estado_civil = ''

        if (var_python.get() == 1) and (var_java.get() == 0) and (var_c_sharp.get() == 0):
            cursos = 'Python'
        elif (var_python.get() == 0) and (var_java.get() == 1) and (var_c_sharp.get() == 0):
            cursos = 'Java'
        elif (var_python.get() == 0) and (var_java.get() == 0) and (var_c_sharp.get() == 1):
            cursos = 'C#'
        elif (var_python.get() == 1) and (var_java.get() == 1) and (var_c_sharp.get() == 0):
            cursos = 'Python, Java'
        elif (var_python.get() == 1) and (var_java.get() == 0) and (var_c_sharp.get() == 1):
            cursos = 'Python, C#'
        elif (var_python.get() == 0) and (var_java.get() == 1) and (var_c_sharp.get() == 1):
            cursos = 'Java, C#'
        elif (var_python.get() == 1) and (var_java.get() == 1) and (var_c_sharp.get() == 1):
            cursos = 'Python, Java, C#'
        else:
            cursos = ''

        status_nome['text'] = f'Nome: {nome}'
        status_genero['text'] = f'Genero: {genero}'
        status_estado_civil['text'] = f'Estado Cívil: {estado_civil}'
        status_cursos['text'] = f'Cursos: {cursos}'

    texto_bem_vindo = Label(janela2, text='Bem-vindo ao cadastro de interesse', font=('Arial', 12, 'bold'),
                            bg=ciano_escuro, fg=branco)
    texto_bem_vindo.place(x=170, y=10)
    texto_nome = Label(janela2, text='Nome:', font=('Arial', 12, 'bold'), bg=ciano_escuro, fg=preto)
    texto_nome.place(x=10, y=40)
    cadastro_nome = Entry(janela2, font=('Arial', 12))
    cadastro_nome.place(x=70, y=40)

    texto_genero = Label(janela2, text='Genero:', font=('Arial', 12, 'bold'), bg=ciano_escuro, fg=preto)
    texto_genero.place(x=10, y=70)

    var_genero = IntVar()

    opcao_masculino = Radiobutton(janela2, text='Masculino', font=('Arial', 12), bg=ciano_escuro, variable=var_genero,
                                  value=1, width=10)
    opcao_masculino.place(x=0, y=100)
    opcao_feminino = Radiobutton(janela2, text='Feminino', font=('Arial', 12), bg=ciano_escuro, variable=var_genero,
                                 value=2, width=10)
    opcao_feminino.place(x=110, y=100)
    opcao_outro = Radiobutton(janela2, text='Outro', font=('Arial', 12), bg=ciano_escuro, variable=var_genero, value=3,
                              width=10)
    opcao_outro.place(x=220, y=100)

    texto_estado_civil = Label(janela2, text='Estado Cívil:', font=('Arial', 12, 'bold'), bg=ciano_escuro, fg=preto)
    texto_estado_civil.place(x=10, y=130)
    caixa_selecao = ttk.Combobox(janela2, font=('Arial', 12),
                                 values=['Escolha a opção', 'Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viuvo(a)'])
    caixa_selecao.current(0)
    caixa_selecao.place(x=115, y=130)

    var_python = IntVar()
    var_java = IntVar()
    var_c_sharp = IntVar()

    texto_curso = Label(janela2, text='Selecione o Curso de Interesse:', font=('Arial', 12, 'bold'), bg=ciano_escuro,
                        fg=preto)
    texto_curso.place(x=10, y=160)
    opcao_python = Checkbutton(janela2, text='python', font=('Arial', 12), variable=var_python, bg=ciano_escuro)
    opcao_python.place(x=10, y=190)
    opcao_java = Checkbutton(janela2, text='java', font=('Arial', 12), variable=var_java, bg=ciano_escuro)
    opcao_java.place(x=140, y=190)
    opcao_c_sharp = Checkbutton(janela2, text='C#', font=('Arial', 12), variable=var_c_sharp, bg=ciano_escuro)
    opcao_c_sharp.place(x=250, y=190)

    botao_enviar = Button(janela2, text='Enviar', font=('Arial', 12), width=20, command=dados_enviados)
    botao_enviar.place(x=210, y=220)

    def voltar_janela_principal():
        janela2.destroy()
        janela1.deiconify()

    botao_sair = Button(janela2, text='Sair', font=('Arial', 12), width=20, command=voltar_janela_principal)
    botao_sair.place(x=210, y=405)

    frame = Frame(janela2, bg=branco, width=400, height=135)
    frame.place(x=100, y=260)

    status_nome = Label(janela2, text='', font=('Arial', 12), bg=branco)
    status_nome.place(x=110, y=270)
    status_genero = Label(janela2, text='', font=('Arial', 12), bg=branco)
    status_genero.place(x=110, y=300)
    status_estado_civil = Label(janela2, text='', font=('Arial', 12), bg=branco)
    status_estado_civil.place(x=110, y=330)
    status_cursos = Label(janela2, text='', font=('Arial', 12), bg=branco)
    status_cursos.place(x=110, y=360)

def caixa_de_mensagem():
    messagebox.showinfo('Caixa de Mensagem', 'Preencha os campos obrigatórios')

def caixa_de_erro():
    messagebox.showerror('Erro', 'E-mail ou senha incorretos')

def comparar_info():
    login_digitado = str(entrada_login.get())
    senha_digitada = str(entrada_senha.get())

    LOGIN = 'usuario@gmail.com'
    SENHA = '12345'

    if (login_digitado == LOGIN) and (senha_digitada == SENHA):
        janela_secundaria()
    elif (login_digitado == '') or (senha_digitada == ''):
        caixa_de_mensagem()
    else:
        caixa_de_erro()

texto_login = Label(janela1, text='Login *', font=('Arial', 12, 'bold'), bg=ciano, fg=preto)
texto_login.grid(column=0, row=0, padx=(50,0), pady=(10,0))
texto_senha = Label(janela1, text='Senha *', font=('Arial', 12, 'bold'), bg=ciano,fg=preto)
texto_senha.grid(column=0, row=1, padx=(50,0), pady=(10,0))
entrada_login = Entry(janela1, font=('Arial', 12))
entrada_login.grid(column=1, row=0)
entrada_senha = Entry(janela1, font=('Arial', 12))
entrada_senha.grid(column=1, row=1)
botao_entrar = Button(janela1, text='Entrar', font=('Arial', 12, 'bold'), fg=preto, command=comparar_info)
botao_entrar.grid(column=1, row=2, padx=(0,20),pady=(10,0))

janela1.mainloop()