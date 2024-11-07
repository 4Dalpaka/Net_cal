import socket

# 서버 설정
host = "127.0.0.1"
port = 12345
# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

try:
    while True:
        print("waiting connection")
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024).decode("utf-8")
        if data == 'EXIT':
            break
        response = f'{eval(data)}'
        # finished
        print("complete")
        client_socket.send(response.encode("utf-8"))
except Exception as e:
    print(f"오류: {e}")
finally:
    print("END")
    client_socket.close()