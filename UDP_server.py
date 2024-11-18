import socket

# 서버 설정
host = "127.0.0.1"
port = 12345
# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

try:
    while True:
        print("waiting connection")
        data, client_address = server_socket.recvfrom(1024)
        print(f"connection form {client_address}")
        data = data.decode("utf-8")
        if data == 'EXIT':
            break
        to_cal = data.split(' ')
        if len(to_cal) == 0:
            response = 'no input'
        elif len(to_cal) == 1:
            response = data
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
            response = f'{sum}'
        # finished
        print("complete")
        server_socket.sendto(response.encode("utf-8"), client_address)
except Exception as e:
    print(f"오류: {e}")
finally:
    print("SEVER PROGRAM END")
    server_socket.close()