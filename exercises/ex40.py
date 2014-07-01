
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

home_on_the_range_lyrics = ["Home, home on the range",
                            "Where the deer and the antelope play",
                            "And seldom is heard a discouraging word",
                            "And the skies are not cloudy all day"]
home_on_the_range = Song(home_on_the_range_lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

home_on_the_range.sing_me_a_song()

print home_on_the_range.lyrics
