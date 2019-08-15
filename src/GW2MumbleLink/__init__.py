import time
import mmap
import struct
import json

import MyGW2API as gw2api

class clsGW2MumbleLinkData():
    UIVersion:int = 0
    GameTick:int = 0
    GameName:str = ""
    AvatarX:float = 0
    AvatarY:float = 0
    AvatarZ:float = 0
    CameraX:float = 0
    CameraY:float = 0
    CameraZ:float = 0
    AvatarName:str = ""
    AvatarProfession: str = ""
    AvatarProfessionID:str = ""
    AvatarRace:str = ""
    AvatarRaceID: str = ""
    MapName:str = ""
    MapID:str = ""
    MapName:str = ""
    RegionID:str = ""
    RegionName:str = ""
    ContinentID:str = ""
    ContinentName:str = ""
    WorldName:str = ""
    WorldID:int = 0
    TeamColourID:int = 0
    Commander:bool = False
    Map:int = 0
    FOV:float = 0
    UISize:int = 0

    def RefreshData(self):
        self.GameTick = 0
        shmem = mmap.mmap(0, (4*2 + 4*3 + 4*3 + 4*3 + 512 + 4*3 + 4*3 + 4*3 + 512 + 4 + 256 + 4096), "MumbleLink", mmap.ACCESS_READ)
        self.UIVersion, self.GameTick = struct.unpack("IL", shmem[:8])
        # print("SELF TEST: ", self.UIVersion, self.GameTick )

        if self.UIVersion == 2:

            self.GameName:str = struct.unpack("512s", shmem[44:44 + 512])[0].decode('utf-16').strip(chr(0))  # 556

            GW2CoOrdsAvatar = struct.unpack("3f3f3f", shmem[8:8 + 36])  # 44
            self.AvatarX = GW2CoOrdsAvatar[2]
            self.AvatarY = GW2CoOrdsAvatar[0]
            self.AvatarZ = GW2CoOrdsAvatar[1]

            GW2CoOrdsCam = struct.unpack("3f3f3f", shmem[556:556 + 36])  # 592
            self.CameraX = GW2CoOrdsCam[2]
            self.CameraY = GW2CoOrdsCam[0]
            self.CameraZ = GW2CoOrdsCam[1]

            GW2Ident:str = struct.unpack("512s", shmem[592:592 + 512])[0].decode('utf-16').strip(chr(0))  # 1104
            GW2Ident = GW2Ident[:GW2Ident.find(chr(0))]
            print(f"GW2 Ident: >{GW2Ident}< : Len: {len(GW2Ident)}")
            GW2IdentDict = json.loads(GW2Ident)
            # print(GW2IdentDict)
            self.AvatarName = GW2IdentDict["name"]
            self.SetProfession(GW2IdentDict["profession"])
            self.SetRace(GW2IdentDict["race"])
            self.SetMapID(GW2IdentDict["map_id"])
            self.WorldID = GW2IdentDict["world_id"]
            self.TeamColourID = GW2IdentDict["team_color_id"]
            self.Commander = GW2IdentDict["commander"]
            self.Map = GW2IdentDict["map"]
            self.FOV = GW2IdentDict["fov"]
            self.UISize = GW2IdentDict["uisz"]

        else:
            self.GameName: str = "No game running"
            self.AvatarName = "Not Logged In"
            self.GameTick = 0

        shmem.close()

    def SetRace(self, RaceID):
        if self.AvatarRaceID != RaceID:
            self.AvatarRaceID = RaceID
            self.AvatarRace = ""
        if self.AvatarRace == "":
            self.AvatarRace = gw2api.GW2_Races[RaceID]

    def SetProfession(self, ProfessionID):
        if self.AvatarProfessionID != ProfessionID:
            self.AvatarProfessionID = ProfessionID
            self.AvatarProfession = ""
        if self.AvatarProfession == "":
            self.AvatarProfession = gw2api.GW2_Professions[ProfessionID]

    def SetMapID(self, MapID):
        self.MapID = MapID
        # print(gw2api.GW2_Maps)
        print(f"MapID: {MapID}")
        # print(gw2api.GW2_Maps["53"])
        print(gw2api.GW2_Maps[str(MapID)])
        self.MapName: str = gw2api.GW2_Maps[str(MapID)]["map_name"]
        self.RegionID: str = gw2api.GW2_Maps[str(MapID)]["region_id"]
        self.RegionName: str = gw2api.GW2_Maps[str(MapID)]["region_name"]
        self.ContinentID: str = gw2api.GW2_Maps[str(MapID)]["continent_id"]
        self.ContinentName: str = gw2api.GW2_Maps[str(MapID)]["continent_name"]







