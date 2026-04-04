def make_album(artist, title, songs=None):
    if songs:
        return {"artist": artist.title(), "title": title.title(), "songs": songs}

    return {"artist": artist.title(), "title": title.title()}


print(make_album("Arabas", "Carabas_Albumb", 5))
print(make_album("Arabas", "Carabas_Albumb"))
