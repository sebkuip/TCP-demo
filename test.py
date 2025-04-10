from TCPPacket import TCPPacket

packet = TCPPacket(5, 4, 0, False, False, True, False, 5, 0, "Hello World").to_bytes()
print(packet.to_bytes(packet.bit_length(), byteorder='little').hex().replace('\\x', ''))
