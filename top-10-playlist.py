import os
from googleapiclient.discovery import build

# Get the values of the environment variables

yt_api_key = os.environ.get('YT_API_KEY')  # YouTube API Key (from the Google Developer Console)
playlist_id = os.environ.get('PLAYLIST_ID') # YouTube playlist ID

# Maximum number of results to retrieve (limited to 1000 by the API)
max_results = 50  # You can adjust this as needed

# Initialize the YouTube API
youtube = build('youtube', 'v3', developerKey=yt_api_key)

# Get the list of videos from the playlist
playlist_items = youtube.playlistItems().list(
    playlistId=playlist_id,
    part='snippet',
    maxResults=max_results
).execute()

# List to store details of the most viewed videos
videos_details = []

# Iterate through the items in the playlist
for item in playlist_items['items']:
    video_id = item['snippet']['resourceId']['videoId']

    # Get details of each video by its ID
    video_info = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    video_details = {
        'title': video_info['items'][0]['snippet']['title'],
        'views': int(video_info['items'][0]['statistics']['viewCount']),
        'video_id': video_id
    }

    videos_details.append(video_details)

# Sort the videos by number of views (most viewed first)
videos_details = sorted(videos_details, key=lambda x: x['views'], reverse=True)

# Limit the list to the top 10 most viewed videos
top_10_videos = videos_details[:10]

# Display the ranking of the top 10 most viewed videos with names and URLs
print("Ranking of the top 10 most viewed videos:")
for idx, video in enumerate(top_10_videos, start=1):
    video_url = f"https://www.youtube.com/watch?v={video['video_id']}"
    print(f"{idx}. {video['title']} - {video_url} - Views: {video['views']}")