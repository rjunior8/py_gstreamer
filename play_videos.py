import gi
gi.require_version("Gst", "1.0")
from gi.repository import GObject, Gst

import os


Gst.init()
mainloop = GObject.MainLoop()

vids_path = os.path.abspath("vids/")

for vid in os.listdir(vids_path):
    
    player = Gst.ElementFactory.make("playbin", "player")
    
    full_path = "file://{vids_path}/{vid}".format(vids_path=vids_path, vid=vid)
    player.set_property("uri", full_path)
    
    player.set_state(Gst.State.PLAYING)

mainloop.run()
