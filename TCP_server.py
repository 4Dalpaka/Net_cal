import socket

# 서버 설정
host = "127.0.0.1"
port = 12345
# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

while True:
    try:
        print("waiting connection")
        client_socket, client_address = server_socket.accept()
        print(f"connection form {client_address}")
        data = client_socket.recv(1024).decode("utf-8")
        if data == 'EXIT':
            print("SEVER PROGRAM END")
            server_socket.close()
            break
        to_cal = data.split(' ')
        if len(to_cal) == 1:
            response = f'c {data}'
        else:
            nextcal = ''
            cal_ing = list()
            for i in to_cal:
                if i == '*' or i == '/':
                    nextcal = i
                else:
                    if nextcal == '*':
                        cal_ing[-1] = f'{eval(cal_ing[-1]) * eval(i)}'
                        nextcal = ''
                    elif nextcal == '/':
                        cal_ing[-1] = f'{eval(cal_ing[-1]) / eval(i)}'
                        nextcal = ''
                    else:
                        cal_ing.append(i)
            sum = 0
            nextcal = '+'
            for k in cal_ing:
                if k == '+':
                    nextcal = '+'
                elif k == '-':
                    nextcal = '-'
                else:
                    if nextcal == '+':
                        sum += eval(k)
                    else:
                        sum -= eval(k)
            response = f'c {sum}'
        # finished
        print("complete")
        client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"오류: {e}")
        print("error send")
        response = f'e {e}'
        client_socket.send(response.encode("utf-8"))