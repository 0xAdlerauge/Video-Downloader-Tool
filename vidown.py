"""
Video Downloader CLI
Author: adlerauge
License: MIT
Description: A robust command-line interface for downloading videos and extracting audio using yt-dlp
"""

import os
import sys
import logging
import re
from typing import Any, Dict
import yt_dlp

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

__author__ = "adlerauge"
__version__ = "1.0.0"

class VideoDownloader:
    def __init__(self, output_dir: str = "Downloads"):
        self.output_dir = output_dir
        self._ensure_output_directory()

    def _ensure_output_directory(self) -> None:
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _progress_hook(self, d: Dict[str, Any]) -> None:
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            sys.stdout.write(f"\rDownloading... {percent} | Speed: {speed}")
            sys.stdout.flush()
        elif d['status'] == 'finished':
            sys.stdout.write("\nDownload complete. Merging formats if necessary...\n")

    def get_options(self, quality: str) -> Dict[str, Any]:
        out_path = os.path.join(self.output_dir, '%(title)s.%(ext)s')
        options = {
            'outtmpl': out_path,
            'quiet': True,
            'no_warnings': True,
            'progress_hooks': [self._progress_hook],
            'merge_output_format': 'mp4',
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }
        
        if quality == '1':
            options['format'] = 'bestvideo+bestaudio/best'
        elif quality == '2':
            options['format'] = 'bestvideo[height<=1080]+bestaudio/best'
        elif quality == '3':
            options['format'] = 'bestvideo[height<=720]+bestaudio/best'
        elif quality == '4':
            options['format'] = 'bestaudio/best'
            options['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        return options

    def is_valid_url(self, url: str) -> bool:
        regex = re.compile(
            r'^(?:http|ftp)s?://' 
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
            r'localhost|' 
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
            r'(?::\d+)?' 
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def download(self, url: str, quality: str) -> None:
        if not self.is_valid_url(url):
            logger.error("Error: The provided string is not a valid URL.")
            return

        logger.info("Starting download process...")
        options = self.get_options(quality)

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
            logger.info("Process finished successfully. Check the Downloads folder.")
        except yt_dlp.utils.DownloadError as e:
            logger.error(f"Download Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    downloader = VideoDownloader()
    
    while True:
        clear_screen()
        print("-" * 50)
        print(" " * 15 + "VIDEO DOWNLOADER CLI")
        print(" " * 18 + "by adlerauge")
        print("-" * 50)
        
        url = input("\nEnter the video URL (or 'q' to quit): ").strip()
        
        if url.lower() == 'q':
            break
        if not url:
            continue

        print("\nSelect quality:")
        print("  [1] Best available quality")
        print("  [2] Max 1080p")
        print("  [3] Max 720p")
        print("  [4] Audio only (MP3)")
        
        quality = input("\nSelect an option (1-4): ").strip()
        if quality not in ['1', '2', '3', '4']:
            print("Invalid option. Defaulting to Best available quality (1).")
            quality = '1'

        print("\n" + "-" * 50)
        downloader.download(url, quality)
        print("-" * 50)
        
        input("\nPress ENTER to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)