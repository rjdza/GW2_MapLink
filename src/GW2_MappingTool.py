import DebugTools.dprint as d
from DebugTools.dprint import logCRITICAL as cprint
# import GW2_MumbleLinkApi

d.termPretty = d.clsTermPictures
cprint("App Started")

import time
import mmap
import struct

# test="1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
test_pack=struct.pack("II3f3f3fs3f3f3fsIcs", 1, 2, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 5.1, 5.2, 5.3, b"6", 7.1, 7.2, 7.3, 8.1, 8.2, 8.3, 9.1, 9.2, 9.3, b"10", 11, b"C", b"13")
print(f"Pack Length: {len(test_pack)} - {test_pack}")

# import gw2lib.common as gw2com
# import gw2lib.mumble as gw2mum

import ctypes
# class Link(ctypes.Structure):
#     _fields_ = [
#         ("uiVersion",       ctypes.c_uint32),
#         ("uiTick",          ctypes.c_ulong),
#         ("fAvatarPosition", ctypes.c_float * 3),
#         ("fAvatarFront",    ctypes.c_float * 3),
#         ("fAvatarTop",      ctypes.c_float * 3),
#         ("name",            ctypes.c_wchar * 256),
#         ("fCameraPosition", ctypes.c_float * 3),
#         ("fCameraFront",    ctypes.c_float * 3),
#         ("fCameraTop",      ctypes.c_float * 3),
#         ("identity",        ctypes.c_wchar * 256),
#         ("context_len",     ctypes.c_uint32),
#         ("context",         ctypes.c_uint32 * (256/4)), # is actually 256 bytes of whatever
#         ("description",     ctypes.c_wchar * 2048)
#
#     ]



lastAvatarPos=[]
lastCamPos=[]
while True:

    # shmem = mmap.mmap(0, 20, "MumbleLink", mmap.ACCESS_READ)
    # coord=struct.unpack("IL3f", shmem)[2:5]

    # coord = struct.unpack("ILLLf", shmem)[2:5]

    # gw2data = struct.unpack("II", shmem)
    # iUIVer, iTick =
    # fY, fZ, fX,  = struct.unpack("f3", shmem[3:5])
    # coord = struct.unpack("f3", shmem[3:5])
    # coord=[0,0,0]

    # shmem = mmap.mmap(0, 20, "MumbleLink", mmap.ACCESS_READ)
    # coord = struct.unpack("IL3f", shmem)[:5]

    # I = 4 : 1 = b'\x01\x00\x00\x00'
    # L = 4 : 1 = b'\x01\x00\x00\x00'
    # f = 4 : 1 = b'\x00\x00\x80?' (So really 3 + 1)

    # shmem = mmap.mmap(0, 94, "MumbleLink", mmap.ACCESS_READ)
    shmem = mmap.mmap(0, (4 *2 + 4 *3 + 4*3 + 4*3 + 512 + 4*3 + 4*3 + 4*3 + 512 + 4 + 256 + 4096), "MumbleLink", mmap.ACCESS_READ)
    # GW2PackedData = struct.unpack("II3f3f3fs3f3f3fsIcs", shmem)
    # GW2PackedData = struct.unpack("II3f3f3f256s", shmem)
    # coord = struct.unpack("IL3f", shmem[:20])
    # iVersion, iTick = GW2PackedData[0:2]

    iVersion, iTick = struct.unpack("IL", shmem[:8])
    GW2CoOrdsAvatar = struct.unpack("3f3f3f", shmem[8:8 + 36]) # 44
    # GW2Name = struct.unpack("256s", shmem[44:300])[0].decode('ascii')
    GW2Name = struct.unpack("512s", shmem[44:44 + 512])[0].decode('ascii') # 556
    # GW2CoOrdsCam = struct.unpack("3f3f3f", shmem[300:336])
    GW2CoOrdsCam = struct.unpack("3f3f3f", shmem[556:556 + 36]) # 592
    GW2Ident =  struct.unpack("512s", shmem[592:592 + 512])[0].decode('ascii')  # 1104
    GW2Context1 = struct.unpack("I", shmem[1104:1104 + 4])  # 1108
    GW2Context2 = struct.unpack("256c", shmem[1108:1108 + 256])[0].decode('ascii')  # 1364
    GW2Desc = struct.unpack("4096s", shmem[1364:1364 + 4096])[0].decode('ascii')  # 5460

    fCoOrd_AvatarPos = GW2CoOrdsAvatar[0:3]
    fCoOrd_AvatarFront = GW2CoOrdsAvatar[3:6]
    fCoOrd_AvatarTop = GW2CoOrdsAvatar[6:9]

    fCoOrd_CamPos = GW2CoOrdsCam[0:3]
    fCoOrd_CamFront = GW2CoOrdsCam[3:6]
    fCoOrd_CamTop = GW2CoOrdsCam[6:9]

    shmem.close()

    if lastAvatarPos!=fCoOrd_AvatarPos:
        lastAvatarPos = fCoOrd_AvatarPos
        print("-------------------------------------------------------------------------------")
        print(f"Ver: {iVersion}, Tick: {iTick}")
        # print(f"Packed Data: {GW2PackedData[2:]}")
        print(f"CoOrds: {GW2CoOrdsAvatar}")
        print(f"Decoded Name: {GW2Name}")
        print(f"Avatar Pos: {fCoOrd_AvatarPos}")
        print(f"Avatar Front: {fCoOrd_AvatarFront}")
        print(f"Avatar Top: {fCoOrd_AvatarTop}")
        print(f"Identity: {GW2Ident}")
        print(GW2Context1)
        print(GW2Context2)
        print(GW2Desc)
        # X = coord[2]
        # Y = coord[0]
        # Z = coord[1]

    if lastCamPos != fCoOrd_CamPos:
        lastCamPos = fCoOrd_CamPos
        print(f"Camera Pos: {fCoOrd_CamPos}")
        print(f"Camera Front: {fCoOrd_CamFront}")
        print(f"Camera Top: {fCoOrd_CamTop}")

    # shmem = mmap.mmap(0, 20, "MumbleLink", mmap.ACCESS_READ)
    # coord=struct.unpack("IL3f", shmem)[2:5]
    #
    # shmem.close()
    # if last!=coord:
    #     print(coord)
    #     last = coord
    #     X = coord[2]
    #     Y = coord[0]
    #     Z = coord[1]
    #
    # mumdat = gw2mum.GW2MumbleData
    # print(mumdat)

    time.sleep(0.3)



# import gw2lib