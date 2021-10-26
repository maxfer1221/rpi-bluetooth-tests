import bluetooth

bd_addr = "c0:b8:83:f2:37:43"

port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")
sock.close()

