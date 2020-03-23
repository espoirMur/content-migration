import shutil
import os
from pytube import Playlist, YouTube
from zipfile import ZipFile


def download_videos_from_playlist(playlist_link, output_path='./videos'):
    """
    Download a youtube playlist and save video to a given path
    Args:
        path (string): the path to the youtube video
        output_path (str, optional): output path. Defaults to './videos'.
    """
    absolute_output_path = os.path.abspath(output_path)
    playlist = Playlist(playlist_link)
    playlist_title = playlist.title
    final_path = os.path.join(absolute_output_path, playlist_title)
    os.mkdir(final_path)
    for url in playlist:
        video = YouTube(url)
        video.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution')[-1].download(final_path)
    
    return final_path


def move_files_to_folder(path):
    """
    this loops trought a directories find all files
    for each file create a folder with the same name 
    and then move the file to the given folder
    
    Args:
        path ([type]): [description]
    """
    
    for dirname, subdirs, files in os.walk(path):
        for filename in files:
            folder_name = filename.split(".")[0]
            folder_name = folder_name.replace(' ', '_')
            print(folder_name)
            source_file = os.path.join(dirname, filename)
            destination_folder = os.path.join(dirname, folder_name)
            os.mkdir(destination_folder)
            shutil.move(source_file, destination_folder)
    

def zip_content_of_folder(path,):
    """
    Zip the content of a folder at the given path
    Args:
        path ([type]): [description]
    Return: the path to the zip file
    """
    print(path)
    file_basename = os.path.basename(path)
    with ZipFile('{}.zip'.format(file_basename), "w") as zip_file:
        for dirname, subdirs, files in os.walk(path):
            zip_file.write(dirname)
            for filename in files:
                folder_name = filename.split(".")[0]
                folder_name = folder_name.replace(' ', '_')
                print(folder_name)
                os.mkdir(os.path.join(dirname, folder_name))
                zip_file.write(os.path.join(dirname, folder_name, filename))


if __name__ == "__main__":
    path = os.path.join('videos', '1584537484.023008')
    file_basename = os.path.basename(path)
    shutil.make_archive(file_basename, 'zip', path)
