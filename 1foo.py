# python3 - 3.10.12 Mar24 installed

# sudo apt install python3-pip -y

# pip install --upgrade pip

# sudo -H pip install -U pipenv

# pipenv upddate

import yt_dlp

def download_youtube_video(video_url, output_path):
    # Define the options for downloading the video
    ydl_opts = {
        'format': 'best',  # Select the best quality format
        'outtmpl': output_path,  # Output file path template
        'postprocessors': [{  # Convert video to audio if needed
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Change format if required (e.g., mp4, mkv)
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    # Replace this with the URL of the YouTube video you want to download
    # video_url = 'https://www.youtube.com/watch?v=your_video_id'
    video_url = 'https://www.youtube.com/watch?v=zU9y354XAgM'

    # Replace this with the desired output file path
    # output_path = '/path/to/your/downloaded_video.mp4'
    output_path = '/home/dave/code/yt-test/downloaded_video.mp4'

    download_youtube_video(video_url, output_path)


