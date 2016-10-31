from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
import struct

def byteswap(byte16):
    h = byte16 / 256
    l = byte16 % 256
    return l * 256 + h


def charswap(str2byte):
    return str2byte[1] + str2byte[0]


client = ModbusClient(method='rtu', port='COM1', baudrate=9600, parity='N', stopbits=1, timeout=1.5, databits=8, unit=1)
client.connect()

endian=client.read_holding_registers(49991,4,unit=1)
#endian.registers[0] = byteswap(endian.registers[0])
#endian.registers[1] = byteswap(endian.registers[1])
#endian.registers[2] = byteswap(endian.registers[2])
#endian.registers[3] = byteswap(endian.registers[3])
decoder=BinaryPayloadDecoder.fromRegisters(endian.registers,endian=Endian.Big)
decoded={
    'val':hex(decoder.decode_32bit_uint()),
    'v100':decoder.decode_32bit_float()
}

print decoded

encoder = BinaryPayloadBuilder(endian=Endian.Big)
encoder.add_16bit_uint(0x1234)
buf = encoder.build()
#buf[0] = charswap(buf[0])
client.write_registers(51234, buf, unit=1, skip_encode=True)

encoder = BinaryPayloadBuilder(endian=Endian.Big)
encoder.add_32bit_float(1.0114)
encoder.add_32bit_float(-6)
buf = encoder.build()
#buf[0] = charswap(buf[0])
#buf[1] = charswap(buf[1])
#buf[2] = charswap(buf[2])
#buf[3] = charswap(buf[3])
client.write_registers(50000 + 8 * 5, buf, unit=1, skip_encode=True)

while True:
    result = client.read_input_registers(100, 6, unit=1)
    if result:
        #result.registers[0] = byteswap(result.registers[0])
        #result.registers[1] = byteswap(result.registers[1])
        #result.registers[2] = byteswap(result.registers[2])
        #result.registers[3] = byteswap(result.registers[3])
        #result.registers[4] = byteswap(result.registers[4])
        #result.registers[5] = byteswap(result.registers[5])
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
        decoded = {
            'voltage': decoder.decode_32bit_float(),
            'pt100': decoder.decode_32bit_float(),
            'freq': decoder.decode_32bit_float()
        }
        print decoded
    client.write_coils(100, (1, 1, 1, 1, 1, 1), unit=1)
    result = client.read_discrete_inputs(100, 4, unit=1)

    print result.bits
    encoder = BinaryPayloadBuilder(endian=Endian.Big)
    encoder.add_32bit_float(20)
    encoder.add_32bit_float(80)
    buf = encoder.build()
    #buf[0] = charswap(buf[0])
    #buf[1] = charswap(buf[1])
    #buf[2] = charswap(buf[2])
    #buf[3] = charswap(buf[3])
    client.write_registers(100, buf, unit=1, skip_encode=True)
    #break
