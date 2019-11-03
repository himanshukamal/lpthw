class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

seedhe_maut = Song(["Utho bano bada padho likho dil ho na ho",
                    "Bolo jo wo bole",
                    " Jo na maane pito beta lao la danda",
                    "Kya baat hai (*2)"

                    "Pao chuo chalo kya baat hai",
                    "Gaye kahan sankar tere",
                    "jeeta galat faimi me tu shoche ghoome aage",
                    "peeche sansaar tere?",
                    "Pehle dhan chaap bete",
                    "Unne Ghanta khed hai",
                    "Hoti light ni uss sheher me jaha pankha fail hai",
                    "bol dhappa",
                    "Poore din gadi phone mai nazar",
                    "Laadsab ki laalsa bhi Gum chal jag ja"])
bulls_on_parade = Song(["They rally around tha family"])

seedhe_maut.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
