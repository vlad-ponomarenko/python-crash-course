#
# BETTER
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album


albums = []

while True:
    artist = input("Artist (or 'quit' to exit): ")
    if artist == "quit":
        break

    title = input("Album title: ")
    if title == "quit":
        break

    songs = input("Number of songs (optional): ")

    if songs:
        album = make_album(artist, title, int(songs))
    else:
        album = make_album(artist, title)

    print(album)
    albums.append(album)
