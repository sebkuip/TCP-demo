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

    def get_binary_data(self) -> int:
        binary_data = 0
        for letter in self.data:
            binary_data <<= 8
            binary_data |= ord(letter)
        return binary_data


    def to_bytes(self) -> bytes:
        packet = 0
        packet |= (self.seqn & 0xFFFFFFFF) << 32
        packet |= (self.ackn & 0xFFFFFFFF) << 32
        packet |= (self.offset & 0xF) << 4
        packet <<= 6 # Reserved bits
        packet |= (1 if self.ack else 0) << 1
        packet <<= 1
        packet |= (1 if self.rst else 0) << 1
        packet |= (1 if self.syn else 0) << 1
        packet |= (1 if self.fin else 0) << 1
        packet |= (self.window & 0xFFFF) << 16
        packet |= (self.checksum & 0xFFFF) << 16
        packet <<= 16
        padding = (32 - (len(self.data) % 32)) % 32
        packet |= self.get_binary_data() << padding
        print(packet)

        return packet
