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
dload.download('C:/Users/Badhon Barman/Desktop/downloader')
print('done')




