def make_album(artist, album, num_songs=None):
    cd = {'artist': artist, 'album': album}
    if num_songs:
        cd['num_songs'] = num_songs
    return cd

another = 'yes'
album_list={}
count = 0;

while another == 'yes':

    count += 1
    print("Describe your favourite album")
    artist_name = input("Artist name: ")
    album_name = input('Album name: ')
    album_list[count] = make_album(artist_name, album_name)
    another = input("repeat for another album?")

print("\nLIST OF FAVOURITE ALBUMS:")
print(album_list)