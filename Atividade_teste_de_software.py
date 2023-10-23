from tkinter import *
from tkinter import messagebox

branco = '#FFFFFF'
azul = '#6959CD'
vermelho = '#FA8072'

def caixa_de_info():
    messagebox.showinfo('Caixa de Mensagem', 'Informações cadastradas com sucesso')

def caixa_de_erro():
    messagebox.showerror('Erro', 'Preencha os campos obrigatórios')

def salvar():
    entradas = [entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, entrada7, entrada8, entrada9, entrada10, entrada11]

    nome_razao_social = str(entrada1.get())
    cnpj_cpf = str(entrada2.get())
    data_nascimento = str(entrada3.get())
    celular = str(entrada10.get())

    if nome_razao_social == '':
        entrada1.config(bg=vermelho)
    if cnpj_cpf == '':
        entrada2.config(bg=vermelho)
    if data_nascimento == '':
        entrada3.config(bg=vermelho)
    if celular == '':
        entrada10.config(bg=vermelho)
    if (nome_razao_social == '') or (cnpj_cpf == '') or (data_nascimento == '') or (celular == ''):
        caixa_de_erro()

    if vermelho not in [entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, entrada7, entrada8, entrada9, entrada10, entrada11]:
        for entrada in entradas:
            entrada.delete(0, 'end')
            entrada.config(bg=branco)

        caixa_de_info()

def cancelar():
    entradas = [entrada1, entrada2, entrada3, entrada4, entrada5, entrada6, entrada7, entrada8, entrada9, entrada10, entrada11]

    for entrada in entradas:
        entrada.delete(0, 'end')
        entrada.config(bg=branco)


janela = Tk()
janela.title('Cadastro')
janela.geometry('650x400')
janela.resizable(width=False, height=False)

tituto = Label(janela, text='Novo Cliente', font=('Arial', 14, 'bold'))
tituto.place(x=35, y=40)

label1 = Label(janela, text='Nome / Razão Social*', font=('Arial', 10))
label1.place(x=35, y=100)
label2 = Label(janela, text='CNPJ / CPF*', font=('Arial', 10))
label2.place(x=325, y=100)
label3 = Label(janela, text='Data de Nascimento*', font=('Arial', 10))
label3.place(x=475, y=100)

entrada1 = Entry(janela, font=('Arial', 10), width=40, bg=branco)
entrada1.place(x=35, y=130)
entrada2 = Entry(janela, font=('Arial', 10), width=20, bg=branco)
entrada2.place(x=325, y=130)
entrada3 = Entry(janela, font=('Arial', 10), width=20, bg=branco)
entrada3.place(x=475, y=130)

label4 = Label(janela, text='Endereço', font=('Arial', 10))
label4.place(x=35, y=170)
label5 = Label(janela, text='Bairro', font=('Arial', 10))
label5.place(x=286, y=170)
label6 = Label(janela, text='CEP', font=('Arial', 10))
label6.place(x=397, y=170)
label7 = Label(janela, text='Data de Cadastro', font=('Arial', 10))
label7.place(x=508, y=170)

entrada4 = Entry(janela, font=('Arial', 10), width=35, bg=branco)
entrada4.place(x=35, y=200)
entrada5 = Entry(janela, font=('Arial', 10), width=15, bg=branco)
entrada5.place(x=286, y=200)
entrada6 = Entry(janela, font=('Arial', 10), width=15, bg=branco)
entrada6.place(x=397, y=200)
entrada7 = Entry(janela, font=('Arial', 10), width=15, bg=branco)
entrada7.place(x=508, y=200)

label8 = Label(janela, text='Município', font=('Arial', 10))
label8.place(x=35, y=240)
label9 = Label(janela, text='Telefone', font=('Arial', 10))
label9.place(x=181, y=240)
label10 = Label(janela, text='Celular*', font=('Arial', 10))
label10.place(x=271, y=240)
label11 = Label(janela, text='UF', font=('Arial', 10))
label11.place(x=361, y=240)

entrada8 = Entry(janela, font=('Arial', 10), width=20, bg=branco)
entrada8.place(x=35, y=270)
entrada9 = Entry(janela, font=('Arial', 10), width=12, bg=branco)
entrada9.place(x=181, y=270)
entrada10 = Entry(janela, font=('Arial', 10), width=12, bg=branco)
entrada10.place(x=271, y=270)
entrada11 = Entry(janela, font=('Arial', 10), width=4, bg=branco)
entrada11.place(x=361, y=270)

texto1 = Label(janela, text='Campos Obrigatórios*', font=('Arial', 10))
texto1.place(x=450, y=270)

botao_salvar = Button(janela, text='Salvar', font=('Arial', 12), bg=azul, fg=branco, width=7, command=salvar)
botao_salvar.place(x=35, y=310)
botao_cancelar = Button(janela, text='Cancelar', font=('Arial', 12), width=7, command=cancelar)
botao_cancelar.place(x=115, y=310)

janela.mainloop()