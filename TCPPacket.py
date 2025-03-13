class TCPPacket:
    def __init__(self, seqn: int, ackn: int, offset: int, ack: bool, rst: bool, syn: bool, fin: bool, window: int, checksum: int, data: bytes):
        self.seqn = seqn
        self.ackn = ackn
        self.offset = offset
        self.ack = ack
        self.rst = rst
        self.syn = syn
        self.fin = fin
        self.window = window
        self.checksum = checksum
        self.data = data

    def to_bytes(self) -> bytes:
        packet = bytearray()
        packet[0:3] = self.seqn
        packet[4:7] = self.ackn
        packet[8] = self.offset << 4
        packet[9] = (self.ack << 5) | (0 << 4) | (self.rst << 3) | (self.syn << 2) | (self.fin << 1)
        packet[10:11] = self.window
        packet[12:13] = self.checksum
        packet[14:15] = 0
        packet[16:19] = bytes(self.data)
        return bytes(packet)

