#import all libraries
import pandas as pd 
import json
from datetime import datetime
import s3fs 
# import snscrape.modules.twitter as sntwitter

from googleapiclient.discovery import build

def run_youtube_etl():
    # YouTube API key and channel IDs
    api_key = 'AIzaSyCsVEZGaWXHRG7zDQQmuQALuG2jC__ukIc'
    channel_ids = ['UCwp9GbPASoPs6BIxVWm_-2A', 'UCJOwq_trsKYpVWUpGuXeyAg'] #Fidelity Channel Id, ETrade Channel ID

    # Building the YouTube API client
    youtube = build('youtube', 'v3', developerKey = api_key)

    # Function to get channel statistics
    def get_channel_stats(youtube, channel_ids):
        all_data = []
        request = youtube.channels().list(part = 'snippet,contentDetails, statistics', id = ','.join(channel_ids))
        response = request.execute()
        for i in range(len(response['items'])):
            data = dict(
                Channel_name = response['items'][i]['snippet']['title'],
                Subscribers = response['items'][i]['statistics']['subscriberCount'],
                Views = response['items'][i]['statistics']['viewCount'],
                Total_videos = response['items'][i]['statistics']['videoCount'],
                playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
            )
            all_data.append(data)
        
        return all_data
        
        
    # Getting channel statistics and creating a DataFrame    
    channel_statistics = get_channel_stats(youtube, channel_ids)
    channel_data = pd.DataFrame(channel_statistics)

    # Extracting Fidelity's playlist ID
    playlist_id = channel_data.loc[channel_data['Channel_name'] == 'Fidelity Investments', 'playlist_id'].iloc[0]

    print(playlist_id)

    # Function to get video IDs from a playlist
    def get_video_ids(youtube, playlist_id):
        request = youtube.playlistItems().list(
                    part = 'contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50)
        response = request.execute()
        
        video_ids=[]
        
        for i in range(len(response['items'])):
            video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
        next_page_token = response.get('nextPageToken')
        more_pages = True
        
        while more_pages:
            if next_page_token is None:
                more_pages = False
            else:
                request = youtube.playlistItems().list(
                    part = 'contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50,
                    pageToken = next_page_token)
                    
                response = request.execute()
                
                for i in range(len(response['items'])):
                    video_ids.append(response['items'][i]['contentDetails']['videoId'])
                    
                next_page_token = response.get('nextPageToken')
                
        return video_ids
        
    # Getting all video IDs from the playlist
    video_ids = get_video_ids(youtube, playlist_id) #has 301 rows
    #print(len(video_ids))

    # Function to get video details
    def get_video_details(youtube, video_ids):
        all_video_stats = []
        for i in range(0, len(video_ids), 50):
            request = youtube.videos().list(
                part = 'snippet, statistics', 
                id = ','.join(video_ids[i:i+50]))
            response = request.execute()
        
            for video in response['items']:
                video_stats = dict(
                    Title = video['snippet']['title'],
                    Published_date = video['snippet']['publishedAt'],
                    Views = video['statistics']['viewCount'],
                    Likes = video['statistics']['likeCount']
                    #,
                    #Comments = video['statistics']['commentCount']
                )
                all_video_stats.append(video_stats)
            
        return all_video_stats
      
    # Getting video details and creating a DataFrame
    video_details = get_video_details(youtube, video_ids)
    video_data = pd.DataFrame(video_details)

    print(video_data)
    print(len(video_data)) #to verify all 301 videos got imported

    video_data.to_csv("s3://bucket_name/Fidelity_YT_Video_Data.csv", index = False)


    
    

    
