import yt_dlp

def download_youtube_video(url, output_path='downloads'):
    """
    Download a YouTube video as MP4
    
    Args:
        url: YouTube video URL
        output_path: Directory to save the video (default: 'downloads')
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        # Fix for 403 errors - use OAuth and avoid SABR streaming
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
                'player_skip': ['webpage', 'configs'],
            }
        },
        # Additional options to avoid blocks
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'geo_bypass': True,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=12345678912"
    download_youtube_video(video_url)
