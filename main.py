# Author:        F4lnes
# Created        22.05.2020
from tkinter import *
from tkinter import messagebox
from gtts import gTTS

LARGE_FONT = ("Avenir", 14)


class TextConvert(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, File_Convert, Single_Convert):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="Help", underline=0, menu=fileMenu)
        fileMenu.add_command(label='Information', underline=1,
                             command=lambda: messagebox.showinfo('Help', 'Thanks for using Text To Speech Translator!\n'
                                                                         'This tool can be used to convert whole .txt '
                                                                         'files or single lines to speech, '
                                                                         'either .mp3 or .wav.'))
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Text To Speech Translator", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = Button(self, text="Convert whole files",
                        command=lambda: controller.show_frame(File_Convert))
        button.pack()

        button2 = Button(self, text="Single Line Convert",
                         command=lambda: controller.show_frame(Single_Convert))
        button2.pack()


class File_Convert(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Single Convert", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(StartPage))
        button1.pack()

        self.file_to_convert = StringVar()
        self.file_ext = StringVar(None, 'wav')

        self.lbl_convert = Label(self, text='File to convert to sound')
        self.lbl_convert.pack(side="top")

        self.file_to_convert.set('script.txt')
        self.entry_convert = Entry(self, textvariable=self.file_to_convert)

        self.entry_convert.pack(side='top')
        self.file_ext.set('wav')
        Radiobutton(self, text="wav", variable=self.file_ext, value='wav').pack(anchor=W)
        Radiobutton(self, text="mp3", variable=self.file_ext, value='mp3').pack(anchor=W)

        self.convert = Button(self, text="CONVERT",
                              command=lambda: self.file_to_sound(self.file_to_convert, self.file_ext))
        self.convert.pack(side="bottom")

        self.lbl_convert = Label(self, text='File to convert to sound')
        self.lbl_convert.pack(side="top")

    def file_to_sound(self, c_file=None, extension=None):
        o_file = c_file.get()
        o_extension = extension.get()

        f = open(o_file)

        for x in f:
            b = x.strip()
            tts = gTTS(b)
            tts.save(f'{b}.{o_extension}')


class Single_Convert(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Single Convert", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.file_to_convert = StringVar()
        self.file_ext = StringVar(None, 'wav')

        self.lbl_convert = Label(self, text='Line to convert to sound')
        self.lbl_convert.pack(side="top")

        self.entry_convert = Entry(self, textvariable=self.file_to_convert)

        self.entry_convert.pack(side='top')
        self.file_ext.set('wav')
        Radiobutton(self, text="wav", variable=self.file_ext, value='wav').pack(anchor=W)
        Radiobutton(self, text="mp3", variable=self.file_ext, value='mp3').pack(anchor=W)

        self.convert = Button(self, text="CONVERT",
                              command=lambda: self.single_line(self.file_to_convert, self.file_ext))
        self.convert.pack(side="bottom")

        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(StartPage))
        button1.pack()

    def single_line(self, line, extension):
        o_line = line.get()
        o_extension = extension.get()

        b = o_line.strip()
        tts = gTTS(b)
        tts.save(f'{b}.{o_extension}')


if __name__ == '__main__':
    app = TextConvert()
    app.mainloop()
