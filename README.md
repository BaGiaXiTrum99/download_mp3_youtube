## 🎵 DownloadMP3 - YouTube to MP3 Cutter

A Python script to download audio from a YouTube video and convert it to MP3 format, with optional trimming between two timestamps.

---

### 📦 Requirements

* Python 3.7+

* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

* You also need `ffmpeg` installed and accessible in your system's PATH:

  * [Download FFmpeg](https://ffmpeg.org/download.html)

---

### 🚀 Features

* Download audio stream from YouTube
* Convert audio to MP3
* Trim by start and end times (in `mm:ss` format)

---

### 🧠 Usage

```python
from download_mp3 import DownloadMP3

downloader = DownloadMP3(
    url="https://www.youtube.com/watch?v=D164TFHeOcI",
    start_seconds="1:0",   # start at 1 minute 0 seconds
    end_seconds="2:0"      # end at 2 minutes 0 seconds
)

downloader.download_audio_file()
downloader.convert_to_mp3_file()
```

---

### 🔧 Class Parameters

| Parameter       | Type | Default | Description                          |
| --------------- | ---- | ------- | ------------------------------------ |
| `url`           | str  | —       | YouTube video URL                    |
| `raw_extension` | str  | `"m4a"` | Format of the downloaded audio       |
| `des_extension` | str  | `"mp3"` | Output format                        |
| `start_seconds` | str  | `"0:0"` | Start time in `mm:ss`                |
| `end_seconds`   | str  | `"0:0"` | End time in `mm:ss` (`"0:0"` = full) |

---

### 📁 Output

* Audio files are saved to a folder named like `m4a_files/`
* Final MP3 files will appear in the same directory with `.mp3` extension

---

### 📌 Notes

* Ensure `ffmpeg` is installed, or `pydub` won't be able to convert audio.
* This script uses `pytubefix` which is a patched version of `pytube`.

---

### 📜 License

MIT License. Free to use and modify.

---

Bạn có muốn mình tạo sẵn file `README.md` và cả file `.gitignore` nếu dùng git không?
