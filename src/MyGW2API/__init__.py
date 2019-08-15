import requests
import DebugTools.dprint as d
from DebugTools.dprint import logDEBUG as dprint
from DebugTools.dprint import logCRITICAL as cprint
d.termPretty = d.clsTermPictures

GW2_API_Base = "https://api.guildwars2.com/"

def GetMaps():
    dprint("Getting map info.")
    retVal = requests.get(GW2_API_Base + "/v1/maps.json")
    return retVal.json()["maps"]

def GetProfessions():
    dprint("Getting profession info.")
    retVal = requests.get(GW2_API_Base + "/v2/professions.json")
    return retVal.json()

def GetRaces():
    dprint("Getting race info.")
    retVal = requests.get(GW2_API_Base + "/v2/races.json")
    return retVal.json()

GW2_Maps = GetMaps()
GW2_Professions = GetProfessions()
GW2_Races = GetRaces()