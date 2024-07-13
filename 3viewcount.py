import yt_dlp

def get_video_info(video_url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,  # We don't need to download the video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
    
    return info_dict

def download_youtube_video(video_url, output_path):
    # Define the options for downloading the video
    ydl_opts = {
        'format': 'best',  # Select the best quality format
        'outtmpl': output_path,  # Output file path template
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    # Replace this with the URL of the YouTube video you want to download
    video_url = 'https://www.youtube.com/watch?v=zU9y354XAgM'

    # Get video info to retrieve view count
    video_info = get_video_info(video_url)
    view_count = video_info.get('view_count', 'N/A')
    comment_count = video_info.get('comment_count', "N/A")
    like_count = video_info.get('like_count', "N/A")

    # Print the view count
    print(f"View count: {view_count}")
    print(f"Comment count: {comment_count}")
    print(f"Like count: {like_count}")

    # Replace this with the desired output file path
    # output_path = '/home/dave/code/yt-test/downloaded_video.mp4'

    # Download the video
    # download_youtube_video(video_url, output_path)
