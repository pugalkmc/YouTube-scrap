import os
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Set up the YouTube API client
credentials, project_id = google.auth.default()
if credentials is None:
    credentials = Credentials.from_authorized_user_file(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

youtube = build('youtube', 'v3', credentials=credentials)

# Define the hashtag to search for
hashtag = 'your_hashtag_here'

# Search for videos that contain the hashtag
search_response = youtube.search().list(
    q=hashtag,
    type='video',
    part='id,snippet',
    fields='items(id(videoId),snippet(channelId,title,description,publishedAt))',
    maxResults=100000
).execute()

# Collect the video links from the search results
video_links = []
for search_result in search_response.get('items', []):
    video_id = search_result['id']['videoId']
    channel_id = search_result['snippet']['channelId']
    video_link = f'https://www.youtube.com/watch?v={video_id}&feature=youtu.be'
    video_links.append(video_link)

# Print the collected video links

print (video_links)
