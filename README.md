# Download-Yt

A tool to easily download YouTube videos using a browser extension and a local backend server.

## Overview

This project consists of two main components:
1. A JavaScript script (`script.js`) that runs as a custom script in the Enhancer for YouTube browser extension
2. A Python backend server (`backend.py`) that processes download requests and saves videos to your local machine

## Requirements

- Python 3.6+
- Flask
- yt-dlp
- Enhancer for YouTube browser extension

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Download-Yt.git
   cd Download-Yt
   ```

2. Install Python dependencies:
   ```
   pip install flask yt-dlp
   ```

3. Set up the Enhancer for YouTube extension:
   - Install [Enhancer for YouTube](https://chrome.google.com/webstore/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle) from the Chrome Web Store
   - Open extension settings
   - Navigate to "Scripts" section
   - Add a new custom script
   - Copy and paste the content of `script.js` into the custom script field
   - Save the script

## Configuration

By default, videos will be downloaded to:
```
C:\Users\Desktop\OneDrive\Vídeos\YoutubeMaterials\
```

To change the download folder, edit the `DOWNLOAD_FOLDER` variable in `backend.py`.

## Usage

1. Start the backend server:
   ```
   python backend.py
   ```

2. Navigate to any YouTube video page
3. The script will automatically activate when you're on a YouTube video page
4. A new tab will open with the download request being processed
5. The video will be downloaded to your configured folder
6. The tab will automatically close after the download completes

## Alternative Usage

You can also use the backend directly by opening http://localhost:5000 in your browser and pasting a YouTube URL.

## Notes

- The server must be running for downloads to work
- The script copies the video URL to your clipboard as a backup method
- Videos are downloaded in the best available quality

## License

See the LICENSE file for details.