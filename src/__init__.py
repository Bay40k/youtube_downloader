import threading
import time
from pathlib import Path
import sys, os

import MainForm
import wx

import downloader


class App(wx.App):
    def __init__(self, redirect=False, **kwds):
        try:
            from ctypes import OleDLL

            # Turn on high-DPI awareness to make sure rendering is sharp on big
            # monitors with font scaling enabled.
            OleDLL("shcore").SetProcessDpiAwareness(1)

        except AttributeError:
            # We're on a non-Windows box.
            pass

        except (OSError, ImportError):
            # exc.winerror is often E_ACCESSDENIED (-2147024891/0x80070005).
            # This occurs after the first run, when the parameter is reset in the
            # executable's manifest and then subsequent calls raise this exception
            # See last paragraph of Remarks at
            # [https://msdn.microsoft.com/en-us/library/dn302122(v=vs.85).aspx](https://msdn.microsoft.com/en-us/library/dn302122(v=vs.85).aspx)
            pass

        super().__init__(**kwds)


class MainFrame(MainForm.MainFrame):
    def __init__(self, parent):
        self.url_selected = False
        self.output_dir_selected = False
        MainForm.MainFrame.__init__(self, parent)
        self.SetClientSize(self.FromDIP(wx.Size(508, 270)))
        self.Show()
        self.default_output_text = self.OutputText.GetLabelText()
        application_path = os.path.dirname(sys.argv[0])
        self.OutputDir.SetPath(str(Path(application_path) / Path("output")))
        self.set_output_dir(None)

    def set_output_dir(self, event):
        print("Directory selected")
        self.output_dir_selected = True

    def set_url(self, event):
        print("URL entered")
        self.url_selected = True

    def on_submit_click(self, event):
        print("Submit button clicked")
        if not self.url_selected:
            self.OutputText.SetLabel("Please enter a URL")
        elif not self.output_dir_selected:
            self.OutputText.SetLabel("Please select an output directory")
        else:
            self.OutputText.SetLabel(self.default_output_text)
        self.OutputText.Show()
        if self.default_output_text == self.OutputText.GetLabelText():
            self.run_download()

    def on_download_hook(self, event):
        print("Download hook called")
        try:
            total_bytes = event["total_bytes"]
        except KeyError:
            total_bytes = event["total_bytes_estimate"]

        self.ProgressBar.SetValue(event["downloaded_bytes"] / total_bytes * 100)

    def run_download(self):
        self.ProgressBar.SetValue(0)
        self.OutputText.SetLabel("Downloading...")
        print("Running download")
        if self.VideoCheck.IsChecked():
            self.download_video()

        if self.AudioCheck.IsChecked():
            self.download_audio()

        print("Done")
        self.OutputText.SetLabel("Done")
        self.ProgressBar.SetValue(100)

    def download_video(self):
        url = self.URL.GetValue()
        output_dir = self.OutputDir.GetPath()
        video_download = threading.Thread(
            target=downloader.download_video,
            args=(url, output_dir, self.on_download_hook),
        )
        video_download.start()
        while video_download.is_alive():
            time.sleep(0.1)
            wx.Yield()

    def download_audio(self):
        url = self.URL.GetValue()
        output_dir = self.OutputDir.GetPath()
        audio_download = threading.Thread(
            target=downloader.download_video_as_mp3,
            args=(url, output_dir, self.on_download_hook),
        )
        audio_download.start()
        while audio_download.is_alive():
            time.sleep(0.1)
            wx.Yield()


app = App(False)
frame = MainFrame(None)
app.MainLoop()
