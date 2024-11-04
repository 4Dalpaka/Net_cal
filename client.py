import tkinter
import tkinter.font
import socket

# cal window
cal=tkinter.Tk()
cal.title("Calculator")
cal.geometry("400x500+100+100")
cal.resizable(False, False)
# cal button
bsx = 0
bsy = 220
bwidth = 100
bheigh = 70
button_font = tkinter.font.Font(family = "맑은 고딕", size=25)
plus_button = tkinter.Button(cal, text = "+", overrelief="raised", font = button_font)
mi_button = tkinter.Button(cal, text = "-", overrelief="raised", font = button_font)
mul_button = tkinter.Button(cal, text = "x", overrelief="raised", font = button_font)
div_button = tkinter.Button(cal, text = "÷", overrelief="raised", font = button_font)
clear_button = tkinter.Button(cal, text = "C", overrelief="raised", font = button_font)
del_button = tkinter.Button(cal, text = "←", overrelief="raised", font = button_font)
plus_button.place(x=bsx, y=bsy, width=bwidth, heigh=bheigh)
mi_button.place(x=bsx + bwidth, y=bsy, width=bwidth, heigh=bheigh)
mul_button.place(x=bsx + bwidth * 2, y=bsy, width=bwidth, heigh=bheigh)
div_button.place(x=bsx + bwidth * 3, y=bsy, width=bwidth, heigh=bheigh)
# cal number button
zero_button = tkinter.Button(cal, text = "0", overrelief="raised", font = button_font)
one_button = tkinter.Button(cal, text = "1", overrelief="raised", font = button_font)
two_button = tkinter.Button(cal, text = "2", overrelief="raised", font = button_font)
three_button = tkinter.Button(cal, text = "3", overrelief="raised", font = button_font)
four_button = tkinter.Button(cal, text = "4", overrelief="raised", font = button_font)
five_button = tkinter.Button(cal, text = "5", overrelief="raised", font = button_font)
six_button = tkinter.Button(cal, text = "6", overrelief="raised", font = button_font)
seven_button = tkinter.Button(cal, text = "7", overrelief="raised", font = button_font)
eight_button = tkinter.Button(cal, text = "8", overrelief="raised", font = button_font)
nine_button = tkinter.Button(cal, text = "9", overrelief="raised", font = button_font)
clear_button.place(x=bsx, y=bsy + bheigh * 3, width=bwidth, heigh=bheigh)
zero_button.place(x=bsx + bwidth, y=bsy + bheigh * 3, width=bwidth, heigh=bheigh)
one_button.place(x=bsx + bwidth * 2, y=bsy + bheigh * 3, width=bwidth, heigh=bheigh)
del_button.place(x=bsx + bwidth * 3, y=bsy + bheigh * 3, width=bwidth, heigh=bheigh)
two_button.place(x=bsx, y=bsy + bheigh * 2, width=bwidth, heigh=bheigh)
three_button.place(x=bsx + bwidth, y=bsy + bheigh * 2, width=bwidth, heigh=bheigh)
four_button.place(x=bsx + bwidth * 2, y=bsy + bheigh * 2, width=bwidth, heigh=bheigh)
five_button.place(x=bsx + bwidth * 3, y=bsy + bheigh * 2, width=bwidth, heigh=bheigh)
six_button.place(x=bsx, y=bsy + bheigh, width=bwidth, heigh=bheigh)
seven_button.place(x=bsx + bwidth, y=bsy + bheigh, width=bwidth, heigh=bheigh)
eight_button.place(x=bsx + bwidth * 2, y=bsy + bheigh, width=bwidth, heigh=bheigh)
nine_button.place(x=bsx + bwidth * 3, y=bsy + bheigh, width=bwidth, heigh=bheigh)

# # 서버 설정
# server_address = "127.0.0.1"
# server_port = 12345

# # 서버에 연결
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((server_address, server_port))

# request = "12+13"
# client_socket.send(request.encode("utf-8"))

# response = client_socket.recv(1024).decode("utf-8")
# print(response)

cal.mainloop()