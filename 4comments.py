import yt_dlp
import json

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

def download_comments(video_url, output_path):
    # Define the options for downloading the comments
    ydl_opts = {
        'writecomments': True,  # Enable comment downloading
        'outtmpl': output_path.replace('.mp4', '.comments.json'),  # Output file path for comments
        'writeinfojson': True,  # Ensure metadata is written
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    # Replace this with the URL of the YouTube video you want to download
    video_url = 'https://www.youtube.com/watch?v=zU9y354XAgM'

    # Get video info to retrieve view count
    video_info = get_video_info(video_url)
    view_count = video_info.get('view_count', 'N/A')

    # Print the view count
    print(f"View count: {view_count}")

    # Replace this with the desired output file path
    output_path = '/home/dave/code/yt-test/downloaded_video.mp4'

    # Download the video
    download_youtube_video(video_url, output_path)

    # Download the comments
    download_comments(video_url, output_path)

    # Load and print comments from the downloaded JSON file
    comments_file_path = output_path.replace('.mp4', '.comments.json')
    try:
        with open(comments_file_path, 'r') as f:
            comments_data = json.load(f)
            print(f"Comments downloaded to {comments_file_path}")
            print("Sample comments:")
            for comment in comments_data['comments'][:5]:  # Print first 5 comments as a sample
                print(comment['text'])
    except FileNotFoundError:
        print(f"Comments file not found at {comments_file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {comments_file_path}")


# TODO try this library instead?
# https://github.com/egbertbouman/youtube-comment-downloader
