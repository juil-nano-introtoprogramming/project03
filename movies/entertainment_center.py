#!python
import media

toy_story = media.Movie("Toy Story",
                        "In a world where toys pretend to be lifeless in the presence of humans, Woody, a pullstring cowboy doll, is the leader of a group of toys that are owned by a boy named Andy Davis.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=Fq00mCqBMY8cRdxXPV9GNQ")

spirited_away = media.Movie("Spirited Away",
                            "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
                            "http://ia.media-imdb.com/images/M/MV5BMjYxMDcyMzIzNl5BMl5BanBnXkFtZTYwNDg2MDU3._V1_UY268_CR4,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

if __name__ == '__main__':
    spirited_away.show_trailer()
