import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib

import sys
from threading import Thread
from time import sleep


if sys.platform == "linux":
    video_src = "v4l2src"
elif sys.platform == "win32":
    video_src = "ksvideosrc"
elif sys.platform == "darwin":
    video_src = "autovideosrc"

Gst.init()

streamer = GLib.MainLoop()
thd = Thread(target=streamer.run)
thd.start()

pipeline = Gst.parse_launch("{video_src} ! decodebin ! videoconvert ! autovideosink".format(video_src=video_src))
pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    streamer.quit()

pipeline.set_state(Gst.State.NULL)
streamer.quit()
