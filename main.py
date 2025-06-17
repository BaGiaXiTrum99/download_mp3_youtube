
from pytubefix import YouTube
from pydub import AudioSegment

class DownloadMP3:
    def __init__(self,url , raw_extension = "m4a", des_extension = "mp3", start_seconds = "0:0", end_seconds   = "0:0"):
        self.url = url
        self.raw_extension = raw_extension
        self.des_extension = des_extension
        self.start_seconds = start_seconds
        self.end_seconds   = end_seconds
        self.m4a_path      = None
        
    def download_audio_file(self):
        yt = YouTube(self.url)
        stream = yt.streams.filter(only_audio=True).first()
        try:
            m4a_path = stream.download(output_path=self.raw_extension+"_files")
            m4a_path=m4a_path.rsplit('\\',2)[-2]+"\\"+m4a_path.rsplit('\\',2)[-1]
            print("Downloaded file",m4a_path)
            self.m4a_path = m4a_path
        except Exception as e:
            print(e)
            self.m4p_path = None

    def convert_to_mp3_file(self):
        try:
            raw_file = AudioSegment.from_file(self.m4a_path,format=self.raw_extension)

            self.start_seconds = int(self.start_seconds.split(':')[0])*60*1000 + int(self.start_seconds.split(':')[1])
            if self.end_seconds == "0:0":
                self.end_seconds = raw_file.__len__()
            else:
                self.end_seconds = int(self.end_seconds.split(':')[0])*60*1000 + int(self.end_seconds.split(':')[1])
            raw_file=raw_file[self.start_seconds:self.end_seconds]
            
            new_path = self.m4a_path.replace(self.raw_extension,self.des_extension)
            mp3_path = raw_file.export(new_path,format=self.des_extension)
            print("Converted to file",mp3_path.name)
            mp3_path = AudioSegment.from_mp3(mp3_path)[self.start_seconds:self.end_seconds]
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    download_file = DownloadMP3("https://www.youtube.com/watch?v=D164TFHeOcI",start_seconds="1:0",end_seconds="2:0")
    download_file.download_audio_file()
    download_file.convert_to_mp3_file()




