# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"YouTube Downloader", pos = wx.DefaultPosition, size = wx.Size( 522,422 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer = wx.BoxSizer( wx.VERTICAL )


		bSizer.Add( ( 0, 18), 0, 0, 5 )

		gSizer1 = wx.GridSizer( 2, 1, 0, 0 )

		self.URLLabel = wx.StaticText( self, wx.ID_ANY, u"Content URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.URLLabel.Wrap( -1 )

		gSizer1.Add( self.URLLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.URL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer1.Add( self.URL, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer.Add( gSizer1, 0, wx.EXPAND, 5 )


		bSizer.Add( ( 0, 10), 0, 0, 5 )

		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )

		self.VideoCheck = wx.CheckBox( self, wx.ID_ANY, u"Video (MP4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VideoCheck.SetValue(True)
		gSizer4.Add( self.VideoCheck, 0, wx.ALL, 5 )

		self.AudioCheck = wx.CheckBox( self, wx.ID_ANY, u"Audio (MP3)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.AudioCheck, 0, wx.ALL, 5 )


		bSizer.Add( gSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 20 )

		gSizer2 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Output Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.OutputDir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRP_DEFAULT_STYLE )
		gSizer2.Add( self.OutputDir, 0, wx.ALL|wx.EXPAND, 10 )


		bSizer.Add( gSizer2, 0, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_button1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		gSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ProgressBar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.ProgressBar.SetValue( 0 )
		gSizer3.Add( self.ProgressBar, 0, wx.ALL|wx.EXPAND, 10 )


		bSizer.Add( gSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()
		self.OutputText = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.URL.Bind( wx.EVT_TEXT, self.set_url )
		self.OutputDir.Bind( wx.EVT_DIRPICKER_CHANGED, self.set_output_dir )
		self.m_button1.Bind( wx.EVT_BUTTON, self.on_submit_click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def set_url( self, event ):
		event.Skip()

	def set_output_dir( self, event ):
		event.Skip()

	def on_submit_click( self, event ):
		event.Skip()


