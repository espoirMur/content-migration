import os
from requests import get
from requests.exceptions import RequestException
from urllib.parse import urlencode
from contextlib import closing
from settings import YOUTUBE_API_KEY

CHANNEL_URL = 'https://www.googleapis.com/youtube/v3/channels'
PLAYLIST_URL = 'https://www.googleapis.com/youtube/v3/playlists'


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers.get('Content-Type').lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('json') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything, like using a logger
    """
    print(e)


def get_youtube_channel_id_from_username(username, URL=CHANNEL_URL):
    """
    Attempt to get geo coordinates
    """
    params = {
        'key': YOUTUBE_API_KEY,
        'part': "id",
        'contentDetails': 'statistics',
        'forUsername': username
        }
    try:
        with closing(get(url=URL, params=params)) as resp:
            if is_good_response(resp):
                return resp.json().get('items')[0].get('id')
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to API : {1}'.format(str(e)))
        return None


def get_playlists_from_channel_id(channel_id: str) -> list:
    """
    given the channel id  return all playlist
    """
    params = {
        'key': YOUTUBE_API_KEY,
        'part': "snippet",
        'channelId': channel_id,
        }
    try:
        with closing(get(url=PLAYLIST_URL, params=params)) as resp:
            if is_good_response(resp):
                return [item.get('id') for item in resp.json().get('items')]
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to API : {1}'.format(str(e)))
        return None


if __name__ == "__main__":
    channel_id = get_youtube_channel_id_from_username("KhanAcademyBangla")
    print(get_playlists_from_channel_id(channel_id))



