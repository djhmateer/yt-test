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
        # 'outtmpl': output_path,  # Output file path template
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',  # Output file path template
        #'postprocessors': [{  # Convert video to audio if needed
        #    'key': 'FFmpegVideoConvertor',
            # 'preferedformat': 'mp4',  # Change format if required (e.g., mp4, mkv)
            #'preferedformat': 'mkv',  # Change format if required (e.g., mp4, mkv)
        #}],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    # Replace this with the URL of the YouTube video you want to download
    # video_url = 'https://www.youtube.com/watch?v=your_video_id'
    # video_url = 'https://www.youtube.com/watch?v=zU9y354XAgM'

    # PL113 first amendment - 180MB.
    video_url = 'https://www.youtube.com/watch?v=LkPDz_MHIEY'

    # PL102 108 year old..  but 53:59 long
    # video_url = 'https://www.youtube.com/watch?v=zP7gmuOJtak'

    # Replace this with the desired output file path
    # output_path = '/path/to/your/downloaded_video.mp4'

    # output_path = '/home/dave/code/yt-test/downloaded_video.mp4'
    # output_path = '/mnt/c/dev/yt-test/downloaded_video.mp4'
    output_directory = '/mnt/c/dev/yt-test/'

    download_youtube_video(video_url, output_directory)


