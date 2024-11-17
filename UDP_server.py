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
        response = f'{eval(data)}'
        # finished
        print("complete")
        server_socket.sendto(response.encode("utf-8"), client_address)
except Exception as e:
    print(f"오류: {e}")
finally:
    print("SEVER PROGRAM END")
    server_socket.close()