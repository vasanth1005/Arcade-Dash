import user
import GamesWindow
import customtkinter as ctk

class EntryFrame(ctk.CTkFrame):
    def __init__(self, *args, width: int = 100, height: int = 32, headerStr: str = "", placeholder:str = "", show:str="", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.label = ctk.CTkLabel(master=self, text=headerStr, height=height)
        self.label.grid(row=0, column=0, padx=10)
        self.entry = ctk.CTkEntry(master=self, placeholder_text=placeholder, show=show, width=width, height=height)
        self.entry.grid(row=1, column=0, columnspan=2)

    def GetText(self)-> str:
        return self.entry.get()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark") 

        self.geometry("500x300")
        self.title("Arcade Dash - Login")
        self.resizable(False,False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.userTextbox = EntryFrame(self,headerStr="Username:", placeholder="Enter username", width=460)
        self.userTextbox.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        
        self.passwordTextbox = EntryFrame(self,show='*', placeholder="Enter password", headerStr="Password:", width=460)
        self.passwordTextbox.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
        
        self.loginButton = ctk.CTkButton(self,text="Login",command=self.button_callback)
        self.loginButton.grid(row=3, column=1, padx=30, pady=(10,20))

    def button_callback(self):
        CURRENT_USER = user.User()
        if (CURRENT_USER.login(self.userTextbox.GetText(),self.passwordTextbox.GetText())):
            self.destroy()
            GamesWindow.open(CurrentUser=CURRENT_USER)

if __name__ == "__main__":
    app = App()
    app.mainloop()
