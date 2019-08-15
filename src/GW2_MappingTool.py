import DebugTools.dprint as d
from DebugTools.dprint import logDEBUG as dprint
from DebugTools.dprint import logCRITICAL as cprint
import wx.xrc
from FormBuilder import GW2_MapLink

import GW2MumbleLink as ML
# import MyGW2API as gw2api

d.termPretty = d.clsTermPictures
cprint("App Started")

mlData = ML.clsGW2MumbleLinkData()
mlData.RefreshData()

class clsWinMain(GW2_MapLink.frmMain):
    """Subclassed Frame"""
    EVENT=wx.NewEventType()
    EVENT2 = wx.PyEventBinder

    def __init__(self,parent):
        GW2_MapLink.frmMain.__init__(self, parent)

    def RunUpdate( self, event ):
        global mlData
        mlData.RefreshData()
        self.lblAvatarName.SetLabel(mlData.AvatarName)
        self.lblProfession.SetLabel(mlData.AvatarProfession)
        self.lblRace.SetLabel(mlData.AvatarRace)
        self.lblMapInfo.SetLabel(f"{mlData.MapName}, {mlData.RegionName}, {mlData.ContinentName}")
        dprint(f"Game Tick: {mlData.GameTick} / UI Version: {mlData.UIVersion}")

def main():

    wxApp = wx.App(False)

    winMain = clsWinMain(None)
    # iconWinMain = wx.EmptyIcon()
    iconWinMain = wx.Icon()
    iconWinMain.CopyFromBitmap(wx.Bitmap("assets\\gw2_icon.ico", wx.BITMAP_TYPE_ANY))
    winMain.SetIcon(iconWinMain)
    winMain.Show()

    wxApp.MainLoop()

if __name__ == "__main__":
    main()
