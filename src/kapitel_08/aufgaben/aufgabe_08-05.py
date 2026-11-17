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
        return super().anzeigen()
        print("ffdf")


class VideoPost(Post):
    def __init__(self, autor, inhalt, video_datei):
        super().__init__(autor, inhalt)
        self.video_datei = video_datei


text_post = Post("user123", "Das ist ein einfacher Text-Post.")
text_post.anzeigen()

bild_post = BildPost("insta_star", "Urlaubsfoto! #sommer", "sonnenuntergang.jpg")
