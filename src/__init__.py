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

        try:
            downloaded_bytes = event["downloaded_bytes"]
            self.ProgressBar.SetValue(int(downloaded_bytes / total_bytes * 100))
        except KeyError:
            self.ProgressBar.Pulse()

    def run_download(self):
        self.ProgressBar.SetValue(0)
        print("Running download")
        if self.VideoCheck.IsChecked():
            self.OutputText.SetLabel("Downloading video...")
            self.download_video()

        if self.AudioCheck.IsChecked():
            self.OutputText.SetLabel("Downloading audio...")
            self.download_audio()

        print("Done")
        self.OutputText.SetLabel("Done")
        self.ProgressBar.SetValue(100)

    def download(self, type: str):
        if type.lower() not in ["video", "audio"]:
            print("Invalid download type")
            return
        if type.lower() == "video":
            download_function = downloader.download_video
        else:
            download_function = downloader.download_video_as_mp3
        url = self.URL.GetValue()
        output_dir = self.OutputDir.GetPath()
        download = threading.Thread(
            target=download_function,
            args=(url, output_dir, self.on_download_hook),
        )
        download.start()
        while download.is_alive():
            time.sleep(0.1)
            wx.Yield()

    def download_video(self):
        self.download("video")

    def download_audio(self):
        self.download("audio")


app = App(False)
frame = MainFrame(None)
app.MainLoop()
