# Aufgabe 08-05
#  TODO: Ihre Lösung hier
class Post:
    def __init__(self, autor, inhalt):
        self.autor = autor
        self.inhalt = inhalt

    def anzeigen(self):
        print(f"--- Post von {self.autor} ---\n{self.inhalt}\n---------------")


class BildPost(Post):
    def __init__(self, autor, inhalt, bild_datei):
        super().__init__(autor, inhalt)
        self.bild_datei = bild_datei

    def anzeigen(self):
        super().anzeigen()
        print(
            f"--- Bild-Post von {self.autor} ---\n{self.inhalt}\n[{self.bild_datei}]\n------------"
        )


class VideoPost(Post):
    def __init__(self, autor, inhalt, video_datei, dauer):
        super().__init__(autor, inhalt)
        self.video_datei = video_datei
        self.dauer = dauer

    def anzeigen(self):
        super().anzeigen()
        print(
            f"--- Video-Post von {self.autor} ---\n{self.inhalt}\n[{self.video_datei} ({self.dauer})]\n------------"
        )


text_post = Post("user123", "Das ist ein einfacher Text-Post.")
bild_post = BildPost("insta_star", "Urlaubsfoto! #sommer", "sonnenuntergang.jpg")
video_post = VideoPost(
    "youtuber", "Mein neues Tutorial ist online!", "anleitung.mp4", 65
)

text_post.anzeigen()
bild_post.anzeigen()
video_post.anzeigen()
