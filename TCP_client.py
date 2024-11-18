import tkinter
import tkinter.messagebox as mess
import tkinter.font as fon
import socket

# cal window
cal=tkinter.Tk()
cal.title("Calculator")
cal.geometry("360x570+100+100")
cal.resizable(False, False)
# set server
server_address = "127.0.0.1"
server_port = 12345
# proccess
wassym = True
to_solve = ''
procc = tkinter.Label(cal, text=to_solve, font=fon.Font(size=15))
procc.place(x=0, y=0)
# result
new_cal = False
aft_cal = tkinter.Label(cal, text='', font=fon.Font(size=25))
aft_cal.place(x=0, y=180)
###
def add(input):
    global to_solve
    global wassym
    global new_cal
    aft_cal.config(text='')
    if input == '+' or input == '-' or input == 'x' or input == '÷':
        if wassym:
            pass
        else:
            new_cal = False
            to_solve+=f' {input} '
            wassym = True
    else:
        if new_cal:
            to_solve = ''
            new_cal = False
        to_solve+=input
        wassym = False
    procc.config(text=to_solve)
def delt():
    global to_solve
    global wassym
    global new_cal
    new_cal = False
    aft_cal.config(text='')
    if len(to_solve) != 0:
        if to_solve[-1] == ' ':
            to_solve = to_solve[:len(to_solve)-3]
            wassym = False
        else:
            to_solve = to_solve[:len(to_solve)-1]
            if len(to_solve) != 0:
                if to_solve[-1] == ' ':
                    wassym = True
            else:
                wassym = True
    procc.config(text=to_solve)
def cle():
    global to_solve
    global wassym
    global new_cal
    new_cal = False
    aft_cal.config(text='')
    wassym = True
    to_solve = ''
    procc.config(text=to_solve)
# cal button
bsx = 0
bsy = 220
bwidth = 90
bheight = 70
button_font = tkinter.font.Font(family = "맑은 고딕", size=23)
plus_button = tkinter.Button(cal, text = "+", overrelief="raised", font = button_font, command=lambda: add('+'), repeatdelay=500)
mi_button = tkinter.Button(cal, text = "-", overrelief="raised", font = button_font, command=lambda: add('-'), repeatdelay=500)
mul_button = tkinter.Button(cal, text = "x", overrelief="raised", font = button_font, command=lambda: add('x'), repeatdelay=500)
div_button = tkinter.Button(cal, text = "÷", overrelief="raised", font = button_font, command=lambda: add('÷'), repeatdelay=500)
clear_button = tkinter.Button(cal, text = "C", overrelief="raised", font = button_font, command=cle, repeatdelay=500)
del_button = tkinter.Button(cal, text = "←", overrelief="raised", font = button_font, command=delt, repeatdelay=500)
plus_button.place(x=bsx+bwidth*3, y=bsy, width=bwidth, height=bheight)
mi_button.place(x=bsx+bwidth*3, y=bsy+bheight, width=bwidth, height=bheight)
mul_button.place(x=bsx+bwidth*3, y=bsy+bheight*2, width=bwidth, height=bheight)
div_button.place(x=bsx+bwidth*3, y=bsy+bheight*3, width=bwidth, height=bheight)
# number button of calculator
zero_button = tkinter.Button(cal, text = "0", overrelief="raised", font = button_font, command=lambda: add("0"), repeatdelay=500)
one_button = tkinter.Button(cal, text = "1", overrelief="raised", font = button_font, command=lambda: add("1"), repeatdelay=500)
two_button = tkinter.Button(cal, text = "2", overrelief="raised", font = button_font, command=lambda: add("2"), repeatdelay=500)
three_button = tkinter.Button(cal, text = "3", overrelief="raised", font = button_font, command=lambda: add("3"), repeatdelay=500)
four_button = tkinter.Button(cal, text = "4", overrelief="raised", font = button_font, command=lambda: add("4"), repeatdelay=500)
five_button = tkinter.Button(cal, text = "5", overrelief="raised", font = button_font, command=lambda: add("5"), repeatdelay=500)
six_button = tkinter.Button(cal, text = "6", overrelief="raised", font = button_font, command=lambda: add("6"), repeatdelay=500)
seven_button = tkinter.Button(cal, text = "7", overrelief="raised", font = button_font, command=lambda: add("7"), repeatdelay=500)
eight_button = tkinter.Button(cal, text = "8", overrelief="raised", font = button_font, command=lambda: add("8"), repeatdelay=500)
nine_button = tkinter.Button(cal, text = "9", overrelief="raised", font = button_font, command=lambda: add("9"), repeatdelay=500)
clear_button.place(x=bsx, y=bsy+bheight*3, width=bwidth, height=bheight)
zero_button.place(x=bsx+bwidth, y=bsy+bheight*3, width=bwidth, height=bheight)
del_button.place(x=bsx+bwidth*2, y=bsy+bheight*3, width=bwidth, height=bheight)
one_button.place(x=bsx, y=bsy+bheight*2, width=bwidth, height=bheight)
two_button.place(x=bsx+bwidth, y=bsy+bheight*2, width=bwidth, height=bheight)
three_button.place(x=bsx+bwidth*2, y=bsy+bheight*2, width=bwidth, height=bheight)
four_button.place(x=bsx, y=bsy+bheight, width=bwidth, height=bheight)
five_button.place(x=bsx+bwidth, y=bsy+bheight, width=bwidth, height=bheight)
six_button.place(x=bsx+bwidth*2, y=bsy+bheight, width=bwidth, height=bheight)
seven_button.place(x=bsx, y=bsy, width=bwidth, height=bheight)
eight_button.place(x=bsx+bwidth, y=bsy, width=bwidth, height=bheight)
nine_button.place(x=bsx+bwidth*2, y=bsy, width=bwidth, height=bheight)
def get_ans():
    global server_address
    global server_port
    global wassym
    global to_solve
    global new_cal
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_address, server_port))
        print(client_socket)
        # 전송 준비
        to_change = list(to_solve)
        if to_change[-1] == ' ':
            to_change = to_change[0:-3]
        procc.config(text=''.join(to_change))
        for k in range(len(to_change)):
            if to_change[k] == 'x':
                to_change[k] = '*'
            elif to_change[k] == '÷':
                to_change[k] = '/'
        request = ''.join(to_change)
        # 서버로 전송
        client_socket.send(request.encode("utf-8"))
        # 서버로부터 수신
        response = client_socket.recv(1024).decode("utf-8")
        # cal 출력
        to_solve = response
        new_cal = True
        wassym = False
        aft_cal.config(text=f'= {response}')
    except Exception as e:
        mess.showinfo("error", e)
# get answer
go_button = tkinter.Button(cal, text = "=", overrelief="raised", font = button_font, command=get_ans)
go_button.place(x=bsx, y=bsy+bheight*4, width=360, height=bheight)
# 창 닫히면 서버 프로그램도 종료
def atclose():
    global server_address
    global server_port
    try:
        #
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        client_socket.connect((server_address, server_port))
        request = 'EXIT'
        client_socket.send(request.encode("utf-8"))
        cal.destroy()
    except:
        cal.destroy()
cal.protocol('WM_DELETE_WINDOW', atclose)
cal.mainloop()