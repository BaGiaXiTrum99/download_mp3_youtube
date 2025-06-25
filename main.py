
from pytubefix import YouTube
from pydub import AudioSegment
import os

class DownloadMP3:
    def __init__(self,url , 
                 raw_extension = "m4a", 
                 des_extension = "mp3", 
                 start_seconds = "0:0", 
                 end_seconds   = "0:0",
                 category = "Nhạc Việt"):
        self.url = url
        self.raw_extension = raw_extension
        self.des_extension = des_extension
        self.start_seconds = start_seconds
        self.end_seconds   = end_seconds
        self.m4a_path      = None
        self.category      = category
    
    def _time_to_ms(self, time_str):
            """Convert mm:ss to milliseconds."""
            minutes, seconds = map(int, time_str.split(":"))
            return (minutes * 60 + seconds) * 1000

    def download_audio_file(self):
        yt = YouTube(self.url)
        stream = yt.streams.filter(only_audio=True).first()
        try:
            m4a_path = stream.download(output_path=self.raw_extension+"_files\\"+self.category)
            # m4a_path=m4a_path.rsplit('\\',3)[-3]+"\\"+m4a_path.rsplit('\\',3)[-2]
            self.m4a_path= os.path.relpath(m4a_path,os.getcwd())
            print("Downloaded file",self.m4a_path)
        except Exception as e:
            print(e)
            self.m4a_path = None

    def convert_to_mp3_file(self):
        try:
            raw_file = AudioSegment.from_file(self.m4a_path,format=self.raw_extension)

            start_ms = self._time_to_ms(self.start_seconds)
            end_ms = self._time_to_ms(self.end_seconds) if self.end_seconds != "0:0" else raw_file.__len__()

            trimmed_audio=raw_file[start_ms:end_ms]
            os.makedirs(self.des_extension+"_files\\"+self.category,exist_ok=True)
            new_path = self.m4a_path.replace(self.raw_extension,self.des_extension).replace("'","")
            mp3_path = trimmed_audio.export(new_path,format=self.des_extension)
            print("Converted to file",mp3_path.name)

        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    download_file = DownloadMP3(
        url="https://www.youtube.com/watch?v=TGbwL8kSpEk",
        start_seconds="0:09",
        end_seconds="3:20",
        category="Nhạc Hàn"
    )
    download_file.download_audio_file()
    download_file.convert_to_mp3_file()



