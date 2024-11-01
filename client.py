import tkinter
import socket


cal=tkinter.Tk()
cal.title("Calculator")
cal.geometry("450x500+100+100")
cal.resizable(False, False)


button = tkinter.Button(cal, overrelief="raised", width=15, height=10)
button.pack()


# 서버 설정
server_address = "127.0.0.1"
server_port = 1234

# 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

cal.mainloop()