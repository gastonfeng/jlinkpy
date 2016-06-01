
from jlink import jlink
from jlink.jlink import JLinkException

filename = 'd:/project/NEWXUNXIAN2830/build/NEWXUNXIAN2830.hex'

try:
    jlink = jlink.JLink()
    # jlink.ExecCommand("si 0\n")
    # jlink.ConfigJTAG()
    print jlink.CORE_Select(50331903)
    print jlink.ExecCommand("unlock kinetis")
    print jlink.ExecCommand("monitor erase")
    print jlink.ExecCommand("device=STM32F103ZE (allow opt. bytes)")
    print jlink.ExecCommand("SupplyPower=1")
    print jlink.ConfigJTAG(0, 0)
    print  jlink.SetEndian(0)
    print jlink.GetFirmwareString()
    print jlink.SetMaxSpeed()
    print jlink.GetSpeed()
    print jlink.SetResetType(0)
    print jlink.SetResetDelay(1000)
    print jlink.ResetPullsRESET(1)
    print jlink.reset()
    print jlink.halt()
    print jlink.SetMaxSpeed()
    print jlink.GetSpeed()
    print jlink.GetDeviceFamily()
    print jlink.GetIdData()
    print hex(jlink.GetDeviceID(-1))
    print jlink.GoIntDis()
    while not jlink.IsHalted():
        pass
    # jlink.ExecCommand("map ram 0x20000000 - 0x2000FFFF")
    # jlink.reset()
    # jlink.ExecCommand("unlock Kinetis")
    # jlink.ExecCommand("r")
    # jlink.ExecCommand("exit")
    print jlink.ExecCommand('loadbin ' + filename + ',0x00000000')
    print jlink.ExecCommand("r")
    print jlink.ExecCommand("exit")
    print hex(jlink.GetSelDevice())
    print hex(jlink.GetId())
    print jlink.GetIRLen()
    # print jlink.GetHWInfo()
    print jlink.GetHardwareVersion()
    # print jlink.DEVICE_GetInfo()
    # print jlink.DEVICE_GetSelected()
    # print jlink.DEVICE_Select()
    print jlink.GetDeviceFamily()

    jlink.erase_all()
    jlink.auto_program(filename)

    print jlink.go()
    jlink.close()
except JLinkException, ex:
    print ex.message

