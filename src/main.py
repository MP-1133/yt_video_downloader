from pytube import *


# pytube needs to be install if not exists.
# to install run the command\> pip install pytube
# sample test URL : https://www.youtube.com/watch?v=BDLxHeADLr8&list=PLfE2YiZ8J_yj2UZcscXbEkk3xuYwC5H7N
# Test save path  : D:\YouTube Video Downloader\ECS Coding videos


def get_required_resolution(playlist):
    videos = playlist.videos[playlist.length - 1:playlist.length]
    for video in videos:
        print("Supported Resolutions as below :- ")
        stream = video.streams
        for s in stream:
            if s.is_progressive and s.subtype == "mp4":
                print(f'{s.resolution} ==> {s}')
    video_resolution = input("\nEnter Your Resolution type from given lines as correct-(case-sensitive) : ")
    return video_resolution


def get_playlist_index(length):
    start_index = int(
        input(f"Enter Index from you want to start download video (Minimum 1 and Maximum {length}) : "))
    end_index = int(input(f"Enter Index up to you want to start download video : (Maximum {length}) : "))
    print(start_index, end_index)
    start_index = start_index - 1
    return start_index, end_index


def download_video(video, save_path, video_resolution):
    print(
        f"#################################################################################\nGetting Video Details...")
    required_stream = video.streams.get_by_resolution(video_resolution)
    print(f"Video title :- {required_stream.title}")
    print("File Size(MB) : ", (required_stream.filesize / 1048576), " MB")
    print(
        '#################################################################################\nVideo Downloading........')
    try:
        required_stream.download(save_path)
        return True
    except:
        return False


def download_playlist(playlist_url, save_path):
    playlist = Playlist(playlist_url)
    print("Total videos in the given Playlist : ", playlist.length)
    while True:
        answer = input("Do you want download videos in Index order ? ANS(Y/N/C) : ")
        if answer.capitalize() == 'C':
            print("Canceling the Process!!!!!!!!!!")
            return
        elif answer.capitalize() == 'Y' or answer.capitalize() == 'N':
            break
        else:
            print('Ohh!!  Invalid selection.. try again..')

    video_resolution = get_required_resolution(playlist)
    count = 0
    if answer.capitalize() == 'Y':
        start_index, end_index = get_playlist_index(playlist.length)
        for video in playlist.videos[start_index: end_index]:
            count = count + 1
            if download_video(video, save_path, video_resolution):
                print(
                    f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   Video Downloaded {count}/{end_index - start_index}  '
                    f'Successfully!!    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            else:
                print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   {count} position Video Downloading Failed!!   "
                      f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ")

    elif answer.capitalize() == 'N':
        confirm = input('Do you want ALL videos from the given Playlist ANS(Y/N) ? : ')
        if confirm.capitalize() == 'Y':
            for video in playlist.videos:
                count = count + 1
                if download_video(video, save_path, video_resolution):
                    print(
                        f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   Video Downloaded {count}/{playlist.length} '
                        f'Successfully!!    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                else:
                    print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   {count} position Video Downloading Failed!!   "
                          f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ")

        if confirm.capitalize() == 'N':
            print("Okay as your wish!!! {coProcess is ending.....")
            return


if __name__ == '__main__':
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& YouTube Playlist/Video Downloader Started.. &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print("\nChoices\n1. Single Video\n2. Whole Playlist\n\nEnter number only as you want..")
    # try:
    choice = int(input("Enter your choice : "))
    if choice == 1:
        url = input("Enter Video URL : ")
        path = input("Enter path for Video save : ")
        print("Supported resolution 360p, 480p, 720p")
        resolution = input("Enter supported Resolution : ")
        download_video(url, path, resolution)
    elif choice == 2:
        # url = 'https://www.youtube.com/watch?v=RWG1DVdgVXA&list=PLfE2YiZ8J_yigmCDlnVc-ZhovuufwB8QZ'
        # path = 'D:\YouTube Video Downloader\ECS Coding videos'
        url = input("Enter Video URL : ")
        path = input("Enter path for Video save : ")
        download_playlist(url, path)

    # except:
    # print('Some error occurred...')
