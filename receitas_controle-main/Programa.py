
import customtkinter as ctk
import database
from tkinter import messagebox

class Application:
    #função de inicio
    def __init__(self):
        self.janela = ctk.CTk()
        self.database = database  
        self.user_entry = None  
        self.password_entry = None  
        self.tela()
        self.tela_login()
        self.janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.geometry("700x400")
        self.janela.title("Login")

        self.janela.resizable(False, False)



    #tela principal
    def create_success_window(self, nome_usuario):
        print(nome_usuario)
        #funçao de mostrar a informaçao na tela
        def mostrar():
            txt_1 = ctk.CTkFrame(master=success_window, width=900, height=680)
            txt_1.place(x=380, y=20)

            if txt_1:
                for widget in txt_1.winfo_children():
                    widget.destroy()

            
            txt_1 = ctk.CTkFrame(master=success_window, width=900, height=680)
            txt_1.place(x=380, y=20)
            slct = database.read(nome_usuario)
            print(slct)
            row = 0  
            for i in slct:
                texto = ctk.CTkLabel(master=txt_1, text=f'ID: {i[0]}, Valor: {i[1]}, Data: {i[2]}, Nome Cliente: {i[3]}, Nome Produto: {i[4]}', pady=20, font=("Roboto", 14))
                texto.grid(row=row, column=0, sticky="w")
                row += 1  
            atls()

        def atls():
            valor = self.database.soma(nome_usuario)
            valor = str(valor)
            label_2.configure(text=valor)



        #comandos do botao
        def bEvent():
            val = val_entry.get()
            desc = desc_entry.get()
            self.database.insert(val, nome_usuario, desc)
            mostrar()
        
        def bEvent2():
            id = id_entry.get()
            self.database.delete(id, nome_usuario)
            mostrar()



        #declaração da tela
        self.janela.destroy()
        success_window = ctk.CTk()
        success_window.geometry("1366x720")
        success_window.title("Logado com Sucesso!")

        txt_1 = ctk.CTkFrame(master=success_window, width=900, height=680)
        txt_1.place(x=380, y=20)

        frame_1 = ctk.CTkFrame(master=success_window, width=300, height=768, bg_color="#191919")
        frame_1.pack(side=ctk.LEFT)

        txt_2 = ctk.CTkFrame(master=success_window, width=300, height=50, fg_color="black")
        txt_2.place(x=0, y=90)

        label_2 = ctk.CTkLabel(master=txt_2, width=300, height=50, bg_color="white", text="teste")
        label_2.place(x=0, y=0)  

        label_1 = ctk.CTkLabel(master=frame_1, width=300, height=300, bg_color="#202020", text="")
        label_1.place(x=0, y=468)

        mostrar()  
        id_entry = ctk.CTkEntry(master=frame_1, placeholder_text='ID para excluir', width=300, font=('Robot', 14))
        id_entry.place(x=0, y=200)
        self.id_entry = id_entry
        button_2 = ctk.CTkButton(master=frame_1, text='Excluir', command=bEvent2, hover_color="#FF6600", fg_color="#E07B28", width=300, height=30, font=("Roboto", 14))
        button_2.place(x=0, y=250)

        val_entry = ctk.CTkEntry(master=frame_1, placeholder_text="Valor", width=300, font=("Roboto", 14))
        val_entry.place(x=0, y=530)
        self.val_entry = val_entry
        desc_entry = ctk.CTkEntry(master=frame_1, placeholder_text="Descrição", width=300, font=("Roboto", 14))
        desc_entry.place(x=0, y=580)
        self.desc_entry = desc_entry
        
        button_1 = ctk.CTkButton(master=frame_1, text="Adicionar", command=bEvent, hover_color="#FF6600", fg_color="#E07B28", width=300, height=30, font=("Roboto", 14))
        button_1.place(x=0, y=650)     

        success_window.mainloop()


    #tela de login
    def tela_login(self):
        login_frame = ctk.CTkFrame(master=self.janela, width=350, height=396)
        login_frame.pack(side=ctk.RIGHT)

        ctk.CTkLabel(master=login_frame, text="Login de usuário", text_color="#E07B28", font=("Roboto", 30)).place(x=65, y=40)

        user_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Digite seu nome de usuário", width=300, font=("Roboto", 14))
        user_entry.place(x=25, y=105)
        self.user_entry = user_entry  

        ctk.CTkLabel(master=login_frame, text_color="#E07B28", text="Nome de usuário é obrigatório.", font=("Roboto", 10)).place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Digite sua senha", width=300, font=("Roboto", 14), show="*")
        password_entry.place(x=25, y=175)
        self.password_entry = password_entry  

        ctk.CTkLabel(master=login_frame, text_color="#E07B28", text="Uso de senha é obrigatório.", font=("Roboto", 10)).place(x=25, y=205)

        ctk.CTkCheckBox(master=login_frame, text="Lembrar de mim", font=("Roboto", 10)).place(x=25, y=245)


        #funçao do login
        def login():
            nome_usuario = self.user_entry.get()
            senha_usuario = self.password_entry.get()
            if nome_usuario and senha_usuario:
                success = self.database.verificar_login(nome_usuario, senha_usuario)

                if success:
                    messagebox.showinfo("Login", "Login efetuado com sucesso!")
                    self.create_success_window(nome_usuario)  

                if not success:
                    messagebox.showwarning("Login", "Falha ao efetuar login. Verifique os dados e tente novamente.")

        ctk.CTkButton(master=login_frame, text="Login", hover_color="#FF6600", fg_color="#E07B28",
                      width=300, height=30, font=("Roboto", 14), command=login).place(x=25, y=285)

        ctk.CTkLabel(master=login_frame, text="Não tem uma conta?", font=("Roboto", 15)).place(x=25, y=325)



        #tela de registro
        def tela_registro():
            login_frame.pack_forget()

            rg_frame = ctk.CTkFrame(master=self.janela, width=350, height=396)
            rg_frame.pack(side=ctk.RIGHT)

            ctk.CTkLabel(master=rg_frame, text="Cadastro de usuário", text_color="#E07B28", font=("Roboto", 30)).place(x=40, y=40)

            user_entry_reg = ctk.CTkEntry(master=rg_frame, placeholder_text="Digite o nome de usuário", width=300, font=("Roboto", 14))
            user_entry_reg.place(x=25, y=105)
            self.user_entry_reg = user_entry_reg  

            password_entry_reg = ctk.CTkEntry(master=rg_frame, placeholder_text="Digite sua senha", width=300, font=("Roboto", 14), show="*")
            password_entry_reg.place(x=25, y=150)
            self.password_entry_reg = password_entry_reg  

            cpassword_entry_reg = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirme sua senha", width=300, font=("Roboto", 14), show="*")
            cpassword_entry_reg.place(x=25, y=195)
            self.cpassword_entry_reg = cpassword_entry_reg  

            ctk.CTkCheckBox(master=rg_frame, text="Aceito os termos e políticas.", font=("Roboto", 10)).place(x=25, y=245)



            def back():
                rg_frame.pack_forget()
                login_frame.pack(side=ctk.RIGHT)

            ctk.CTkButton(master=rg_frame, text="VOLTAR", hover_color="#191919", fg_color="gray", width=145,
                          height=30, font=("Roboto", 14), command=back).place(x=25, y=290)



            def save_user():
                nome_usuario = self.user_entry_reg.get()  
                senha_usuario = self.password_entry_reg.get()  
                csenha_usuario = self.cpassword_entry_reg.get()  
                if nome_usuario and senha_usuario:
                    if senha_usuario == csenha_usuario:
                        success = self.database.cadastrar_usuario(nome_usuario, senha_usuario)
                        if success:
                            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
                        else:
                            messagebox.showwarning("Cadastro", "Falha ao cadastrar usuário. Verifique os dados e tente novamente.")
                    else:
                        messagebox.showwarning("Cadastro", "Senhas não coincidem. Tente novamente.")

            ctk.CTkButton(master=rg_frame, text="CADASTRAR", hover_color="#FF6600", fg_color="#E07B28", width=145,
                          height=30, font=("Roboto", 14), command=save_user).place(x=180, y=290)

        ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, hover_color="#FF6600", fg_color="#E07B28",
                      font=("Roboto", 14), command=tela_registro).place(x=175, y=325)


if __name__ == "__main__":
    Application()
