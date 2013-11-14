

#output.icecast(%ogg(%flac(samplerate=44100, channels=2,compression=0, bits_per_sample=16)),id="icecast_xxxxx",
#               fallible=true,mount="my_radio.ogg", 
#               host="node06.daj.anorg.net", port=8000, password="dasource",
#               s)

#output.icecast(%external(channels=2,samplerate=44100,header=true,
#          restart_on_crash=false,
#          restart_after_delay=5,
#          process="flac"), format="audio/mpeg", name="external", s)


output.icecast(%gstreamer(channels=2,
           audio="lame",
           has_video=false,
           muxer="mpegtsmux",
           metadata="metadata",
           log=5,
           pipeline=""), format="audio/mpeg", name="external", s)
