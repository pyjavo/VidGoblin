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
    video_url = "https://youtu.be/123456789"
    download_youtube_video(video_url)
