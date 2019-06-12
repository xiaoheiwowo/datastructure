
POL = 0x31 | 0x0100
INIT = 0xFF
XOR = 0x00

def printb(*args):
    print([bin(i)[2:].rjust(10, '0') for i in args])

def crc8_byte(byte_data):
    ret = byte_data
    for i in range(8):
        
        ret <<= 1
        ret += 0
        printb(ret)
        if (ret >> 8) == 1:
            ret ^= POL
    return ret ^ XOR


def cal_crc8(data):
    ret = 0
    for byte in data:
        ret = crc8_byte(ret ^ byte)
    
    return ret

if __name__ == "__main__":
    print(hex(crc8_byte(0x33)))
    # print(hex(cal_crc8([0xBE, 0xEF])))