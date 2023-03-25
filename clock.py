import ctypes
import datetime
import threading
import time
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk


class Application:
    def __init__(self):
        self.window()

    def window(self):
        def info(title, content):
            tkinter.messagebox.showinfo(title, content)

            return None

        def close(event):
            root.destroy()

        def update():
            while True:
                time_now = datetime.datetime.now()
                tkstr_time.set(time_now.strftime("%H:%M:%S"))
                date_now = datetime.datetime.now()
                tkstr_date.set(date_now.strftime("%Y/%m/%d %a"))
                time.sleep(1)

        root = tkinter.Tk()
        root.title("Clock")
        root.geometry("+10+10")
        root.resizable(False, False)
        root.attributes("-topmost", True)
        # root.overrideredirect(True)

        icondata = """iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAABGdBTUEAALGPC/xh
BQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAA
OpgAABdwnLpRPAAAAb9QTFRFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////abHWxQAAAJN0Uk5TAAEO
MU98lZihoJZ9TgIYU5nG7PrHmhcth9H50CsmjeT+4o4kDGza2GgLJ6n989XAtqfW
+KUjQeFhOxkJBgOkyz3g/G0lBM3eTVDl229wQvsqLqo8z/B6Ex8eD/HKkWXtZmTZ
fobjLNx2VTLfo3lbk6gHt5RqwRow66woi1JMzsx7L66Cg9Ru8u+fIj44d0vdOimM
/wWCJQAAAAFiS0dElH9nShUAAAAJcEhZcwABOvYAATr2ATqxVzoAAAODSURBVFjD
7Vf5QxJBFJ5FSVBR8b4QPEoUUVEKXFxIcZUKQ0hRUVNT0zzKo8QjrdSszMriH86Z
WXB3mT3k1/p+2++9982bmTezbwD4DyVQVMaRmqxs7Z0cnT4nNy8/S2O4ZXRBYZGx
uCTBoaS4tKywXH0uhorKquqECNU1lbUq0zDVmS0JAiz1DY0qwpvu3iOGI4lma4tS
fKstlXybvb2j0+Ho7OiytyW5bud9+fgHNclol87dQ3t6GabXQ/e4vfVJDd9Dufjs
PuzV7/MPsHwD2+of7Me2oYB0/KPH2OdJsCDdSA8PYatZUuEpHj/kHCGaqXAkhHN4
JrF+o8g8FtWkqPGJycmJ8dRnTDuFXKYHiPtnQ8ZiN5OiDDNml8s8c1M/7PNZ5ORt
Igj40f6NuXnlZvAibz4zN4bKcp4wgRdo/lEGyAkAZgGtQ7MpbYUaUG5ODZAXABo8
00Xx0Qovof17CZQEQHgZkkthkUAlKr8gUBYAK+is5AlJGpXwdIEaAdoH2SpaQL5C
W+AHagTACtqIbAFXBrk+kzoBE6rYBsHSGiGlY9QJsBFIG/kbtgoLzOIG6gSAH9Kz
qzwmG96f9h61Aj12eNPyF2EBOrbTZAEna0iCqx66HfJWnmcuJDo8ZIE1p5fDOpej
pwPyGzzPIkh09pIFbtD2GvO9nfDrzY0jpYOEg1ErwGzCLz2VuYBNJABybjeFrW34
taO8iNRbh5eP1CK+Ey+iFhJdadsIKIMQXNK7XeJtDJALSQq4kPi3e3yPWMpSCMIE
9uI8Bh+mdVZdPLufdphwJbkO1AkcuKD3oYB7T7xQJLCB/tNHAq78GJIfdtXE7yLf
43Ihu4gKZViNwEeLuAogatG8hj4px2etofUaEdFUHSpWW0wpPnaCHE/TDI2oukJa
Rj6ePUN9xmdCp2PthpapOdlejjn/graAVHMt+OjNzsnkwJ5/RU7fiM1aow83GAsa
qfjYGRo/Ybwg27/jJigUqSB3tfET3OIsX0qNEDBzjdgPUpMVXeOarJ/ScwxwPv2D
K+I2b2OUa/N+ycRfn3Rf8vbqi/ivUKO55aGvgvuuZKNZeglkMeAUtrqbtm1Bq6u/
AApomm9OSMHS7lZstmESi0vkdt91qjg8hqFWW5P24Og+jv5W/+6hCvL/lPKePHvG
w6NbPHmwxvWjyxrd0et3NqyBuCbzx1vGkf8Q/gJf8QMsQfk1swAAACV0RVh0ZGF0
ZTpjcmVhdGUAMjAxOC0wOS0yNlQxNzozNDowOCswMjowMHNHuogAAAAldEVYdGRh
dGU6bW9kaWZ5ADIwMTgtMDktMjZUMTc6MzQ6MDgrMDI6MDACGgI0AAAARnRFWHRz
b2Z0d2FyZQBJbWFnZU1hZ2ljayA2LjcuOC05IDIwMTYtMDYtMTYgUTE2IGh0dHA6
Ly93d3cuaW1hZ2VtYWdpY2sub3Jn5r80tgAAABh0RVh0VGh1bWI6OkRvY3VtZW50
OjpQYWdlcwAxp/+7LwAAABh0RVh0VGh1bWI6OkltYWdlOjpoZWlnaHQANTEywNBQ
UQAAABd0RVh0VGh1bWI6OkltYWdlOjpXaWR0aAA1MTIcfAPcAAAAGXRFWHRUaHVt
Yjo6TWltZXR5cGUAaW1hZ2UvcG5nP7JWTgAAABd0RVh0VGh1bWI6Ok1UaW1lADE1
Mzc5NzYwNDiqWeX5AAAAE3RFWHRUaHVtYjo6U2l6ZQAxMi4zS0JCzRDEXAAAAGt0
RVh0VGh1bWI6OlVSSQBmaWxlOi8vLi91cGxvYWRzLzU2L1dMaDJNS0EvMTU3MC8z
NTA3NzY3LWFsYXJtLWNsb2NrLWljb25vdGVrYS1sYXRlci10aW1lLXRpbWVyLXdh
dGNoXzEwNzY4MS5wbmfrd0PCAAAAAElFTkSuQmCC
"""

        root.tk.call(
            "wm", "iconphoto", root._w, tkinter.PhotoImage(data=icondata)
        )

        inner = ttk.Frame(root)
        inner.grid(column=0, row=0, ipadx=0, ipady=0, padx=20, pady=(10, 20))

        tkstr_time = tkinter.StringVar()
        time_display = ttk.Label(
            inner,
            textvariable=tkstr_time,
            font=("", 30, "bold"),
            anchor=tkinter.CENTER,
        )
        time_display.grid(
            column=0,
            row=0,
            columnspan=1,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=4,
        )
        time_now = datetime.datetime.now()
        tkstr_time.set(time_now.strftime("%H:%M:%S"))

        tkstr_date = tkinter.StringVar()
        date_display = ttk.Label(
            inner,
            textvariable=tkstr_date,
            font=("", 20, "bold"),
            anchor=tkinter.CENTER,
        )
        date_display.grid(
            column=0,
            row=1,
            columnspan=1,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=4,
        )
        date_now = datetime.datetime.now()
        tkstr_date.set(date_now.strftime("%Y/%m/%d %a"))

        root.bind("<Escape>", close)

        updater = threading.Thread(target=update)
        updater.start()

        root.mainloop()


if __name__ == "__main__":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass

    Application()
