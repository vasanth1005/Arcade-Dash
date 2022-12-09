import user
import customtkinter as ctk
from Tetris import tetris
from Racer import main
from PIL import Image

class App(ctk.CTk):
    def __init__(self, CurrentUser: user.User):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("Arcade Dash - Games")

        tetrisImage = ctk.CTkImage(light_image=Image.open("Tetris/tetrisImage.jpg"),
                                  dark_image=Image.open("Tetris/tetrisImage.jpg"),
                                  size=(300,150))
        self.tetrisButton = ctk.CTkButton(self,image=tetrisImage, text="", 
                                            command=self.tetrisButton_callback, corner_radius=0)
        self.tetrisButton.grid(row=0, column=0, padx=30, pady=20)

        RacerImage = ctk.CTkImage(light_image=Image.open("Racer/racerImage.png"),
                                  dark_image=Image.open("Racer/racerImage.png"),
                                  size=(300,150))
        self.RacerButton = ctk.CTkButton(self,image=RacerImage, text="", 
                                            command=self.racerButton_callback, corner_radius=0)
        self.RacerButton.grid(row=0, column=1, padx=30, pady=20)

        self.CURRENT_USER = CurrentUser

    def tetrisButton_callback(self):
        self.destroy()
        tetris.Run(self.CURRENT_USER)
    
    def racerButton_callback(self):
        self.destroy()
        main.Run(self.CURRENT_USER)
            


def open(CurrentUser: user.User):
    app = App(CurrentUser=CurrentUser)
    app.mainloop()