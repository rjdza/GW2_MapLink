import time
import mmap
import struct
import json

class clsGW2MumbleLinkData():
    UI_Version:str = ""
    GameTick:int = 0
    GameName:str = ""
    AvatarX:float = 0
    AvatarY:float = 0
    AvatarZ:float = 0
    CameraX:float = 0
    CameraY:float = 0
    CameraZ:float = 0
    AvatarName:str = ""
    AvatarProfession: str = 0
    AvatarProfessionID:int = 0
    AvatarRace:str = ""
    AvatarRaceID: str = ""
    MapName:str = ""
    MapID:int = 0
    WorldName:str = ""
    WorldID:int = 0
    TeamColourID:int = 0
    Commander:bool = False
    Map:int = 0
    FOV:float = 0
    UISize:int = 0

    def Update(self):
        shmem = mmap.mmap(0, (4*2 + 4*3 + 4*3 + 4*3 + 512 + 4*3 + 4*3 + 4*3 + 512 + 4 + 256 + 4096), "MumbleLink", mmap.ACCESS_READ)
        self.UI_Version, self.GameTick = struct.unpack("IL", shmem[:8])
        self.GameName = struct.unpack("512s", shmem[44:44 + 512])[0].decode('ascii')  # 556

        GW2CoOrdsAvatar = struct.unpack("3f3f3f", shmem[8:8 + 36])  # 44
        self.AvatarX = GW2CoOrdsAvatar[2]
        self.AvatarY = GW2CoOrdsAvatar[0]
        self.AvatarZ = GW2CoOrdsAvatar[1]

        GW2CoOrdsCam = struct.unpack("3f3f3f", shmem[556:556 + 36])  # 592
        self.CameraX = GW2CoOrdsCam[2]
        self.CameraY = GW2CoOrdsCam[0]
        self.CameraZ = GW2CoOrdsCam[1]

        GW2Ident = struct.unpack("512s", shmem[592:592 + 512])[0].decode('ascii')  # 1104
        GW2IdentDict = json.loads(GW2Ident)
        print(GW2IdentDict)

        shmem.close()


