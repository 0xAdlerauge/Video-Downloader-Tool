# Video Downloader CLI 

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

A robust, interactive Command Line Interface (CLI) application for downloading videos and extracting audio from thousands of websites, powered by `yt-dlp`.

Created by **adlerauge**

## ✨ Features

- **Multi-platform support**: Download from YouTube, Vimeo, X (Twitter), and thousands of other sites.
- **Interactive UI**: Clean terminal interface with quality selection menus.
- **Quality Control**: Choose between Best Quality, 1080p, 720p, or Audio-only (MP3).
- **Robust Error Handling**: Includes strict URL validation and bypasses common HTTP errors gracefully.
- **Progress Tracking**: Real-time download percentage and speed monitoring.

## 🛠️ Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html) (required for merging video/audio tracks and MP3 conversion)

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/0xAdlerauge/Video-Downloader-Tool.git
   cd Video-Downloader-Tool
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the script from your terminal:

```bash
python vidown.py
```

Paste your URL when prompted and select your desired output quality. Files will be saved automatically in the `Downloads` folder.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
