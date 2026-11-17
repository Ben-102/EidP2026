# Aufgabe 08-05
#  TODO: Ihre Lösung hier
class Post:
    def __init__(self, autor, inhalt):
        self.autor = autor
        self.inhalt = inhalt

    def anzeigen(self):
        print()


class BildPost:
    def __init__(self, autor, inhalt, bild_datei):
        super().__init__(autor, inhalt)
        self.bild_datei = bild_datei


class VideoPost:
    def __init__(self, autor, inhalt, video_datei):
        super().__init__(autor, inhalt)
