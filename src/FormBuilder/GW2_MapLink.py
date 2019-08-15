# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 13 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,374 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

        gsOutline = wx.GridSizer( 3, 3, 0, 0 )

        bsTL = wx.BoxSizer( wx.VERTICAL )

        self.lblAvatarName = wx.StaticText( self, wx.ID_ANY, u"No Avatar Logged In", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblAvatarName.Wrap( -1 )

        self.lblAvatarName.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

        bsTL.Add( self.lblAvatarName, 0, wx.ALL, 5 )

        self.lblProfession = wx.StaticText( self, wx.ID_ANY, u"Profession", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblProfession.Wrap( -1 )

        self.lblProfession.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

        bsTL.Add( self.lblProfession, 0, wx.ALL, 5 )

        self.lblRace = wx.StaticText( self, wx.ID_ANY, u"Race", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblRace.Wrap( -1 )

        self.lblRace.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

        bsTL.Add( self.lblRace, 0, wx.ALL, 5 )

        self.lblMapInfo = wx.StaticText( self, wx.ID_ANY, u"Map Info", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblMapInfo.Wrap( -1 )

        self.lblMapInfo.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

        bsTL.Add( self.lblMapInfo, 0, wx.ALL, 5 )

        self.lblWorldInfo = wx.StaticText( self, wx.ID_ANY, u"World Info", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblWorldInfo.Wrap( -1 )

        self.lblWorldInfo.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

        bsTL.Add( self.lblWorldInfo, 0, wx.ALL, 5 )


        gsOutline.Add( bsTL, 1, wx.EXPAND, 5 )

        bsTM = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bsTM.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        gsOutline.Add( bsTM, 1, wx.EXPAND, 5 )

        bsTR = wx.BoxSizer( wx.VERTICAL )


        gsOutline.Add( bsTR, 1, wx.EXPAND, 5 )


        self.SetSizer( gsOutline )
        self.Layout()
        self.tmrUpdate = wx.Timer()
        self.tmrUpdate.SetOwner( self, wx.ID_ANY )
        self.tmrUpdate.Start( 250 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_TIMER, self.RunUpdate, id=wx.ID_ANY )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def RunUpdate( self, event ):
        event.Skip()


