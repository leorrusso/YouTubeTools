import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title(".mp3 downloader")
app.geometry("640x720")
app.grid_columnconfigure(0, weight=1)

lblUrl = customtkinter.CTkLabel(app, text="Paste the url below to download the .mp3")
lblUrl.grid(row=0,column=0, pady = 8, padx =16,sticky="ew")
txtUrl = customtkinter.CTkEntry(app)
txtUrl.grid(row=1,column=0, pady = 16, padx =16,sticky="ew")

conFrame = customtkinter.CTkFrame(app)
conFrame.grid(row=2,column=0, sticky="ew")
conFrame.columnconfigure(0, weight=1)
btnDownload = customtkinter.CTkButton(conFrame, text="Download", command=button_callback)
btnDownload.grid(row=2, column=0, padx=0, pady=4)
btnCancel = customtkinter.CTkButton(conFrame, text="Cancel", fg_color="transparent", command=button_callback)
btnCancel.grid(row=3, column=0, padx=0, pady=4)

app.mainloop()