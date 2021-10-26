import bluetooth
server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#server_sock = bluetooth.BluetoothSocket( bluetooth.L2CAP )

# port = bluetooth.get_available_port( bluetooth.RFCOMM )
port = 1
server_sock.bind(("", port))
server_sock.listen(1)

uuid = "f2066963-c794-4899-b3b3-9c09ee11d963"
bluetooth.advertise_service( server_sock, "RBP Receiver", uuid )


client_sock,address = server_sock.accept()

print("Accepted connection from ", address)

client_sock.close()
server_sock.close()
