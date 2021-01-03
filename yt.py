# import pytube

# url = 'https://www.youtube.com/watch?v=UqLDoWIzork'

# video = pytube.YouTube(url)

# dload = video.streams.get_by_itag(298)
# dload.download('C:/Users/Badhon Barman/Desktop/downloader')
# print('done')

# ----------------------------------------------------------------

import pytube

url = 'https://www.youtube.com/watch?v=UqLDoWIzork'

video = pytube.YouTube(url)

dload = video.streams.get_by_itag(298)

#the reason for using 298 here 

# _________________________________

# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
# <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
# <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d4016" progressive="False" type="video">
# <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="298" mime_type="video/mp4" res="720p" fps="60fps" vcodec="avc1.4d4020" progressive="False" type="video">
# <Stream: itag="302" mime_type="video/webm" res="720p" fps="60fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d4014" progressive="False" type="video">
# <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">
# <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">
# <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400b" progressive="False" type="video">
# <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
# <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">

# _________________________________

dload.download('C:/Users/Badhon Barman/Desktop/downloader')
print('done')




