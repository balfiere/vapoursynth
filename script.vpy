import vapoursynth as vs
core = vs.core
# import havsfunc as haf
# import muvsfunc as muvs
# import mvsfunc as mvs
#import descale as descale
#import finescale as fun
import resamplehq as rhq

# core.max_cache_size = 20000 #Use this command to limit the RAM usage (1000 is equivalent to 1GB of RAM)

# import the video
video = core.bs.VideoSource(source='/home/balfiere/Videos/vapoursynth/cut.mkv')

# convert to 4:4:4
video = core.fmtc.resample(video, css="444")
video = core.resize.Bicubic(video, format=vs.YUV444PS)  # convert to float32

############## Whatever you copied from the resizer goes here

video = core.descale.Debicubic(video, 630,354)

video = core.knlm.KNLMeansCL(video, 0, 6, 4, 1.2, channels="YUV")

video = core.cas.CAS(video, 0.5)

video = core.std.CropRel(video, left=142, top=3, right=220, bottom=1)

##############

#Trim returns a clip with only the frames between the arguments first and last, or a clip of length frames, starting at first. a = first frame, b = last frame
video = core.std.Trim(video, 43, 446)

video = core.fmtc.bitdepth(video, bits=16)
video.set_output()
