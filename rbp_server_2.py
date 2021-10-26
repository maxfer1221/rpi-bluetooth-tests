import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

port = 0x1001
server_sock.bind(("",port))
server_sock.listen(1)
print("listening on port %d" % port)

uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
bluetooth.advertise_service(
        server_sock,
        "FooBar Service",   
        bluetooth.AV_REMOTE_CLASS)
        # bluetooth.AV_REMOTE_PROFILE )

client_sock,address = server_sock.accept()
print("Accepted connection from ",address)

data = client_sock.recv(1024)
print("received [%s]" % data)

client_sock.close()
server_sock.close()
