# ------------------------------------------------------------------------------
#        Name: Julia Lee  and Zhengfei Xia
#    Filename: playlist.py
#        Date: 10/17/2018
# Description: This is a  youtube playlist!                                            
# ------------------------------------------------------------------------------
def store():
    songs = {}
    Answer = input("Do you want to enter a  song ? (Type DONE to end):")
    song_info=[]
    while Answer.upper().strip() != 'DONE':
        i  = 0
        if Answer.upper() != 'DONE':
            Title = input("Song Title:")
            Url = input("Url:")
            duration = input("Video Duration (mm:ss)")
            songs[Title] = [Url , duration]
            for s in songs:
                    i += 1
                    print(str(i)+".",s)
            print(songs)
            Answer = input("Do you want to enter another song ? (Type DONE to end):")
    return songs
#play:
def play (songs):
    import webbrowser
    from time import sleep
    song = input("What song do you want to play?:")
    #info is a list
    info = songs[song] 
    print("Now playing", song)
    sleep(2)
    webbrowser.open(info[0])
    time = info[1].split(":")
    seconds = int(time[0])*60 + int(time[1])
    sleep(seconds)
    print("Song is over!")

def main():
    songs = store()
    play(songs)
if (__name__ == "__main__"):
    main()
