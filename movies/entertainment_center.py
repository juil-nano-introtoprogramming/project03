#!python
# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

from operator import add

toy_story = media.Movie("Toy Story",
                        "In a world where toys pretend to be lifeless in the presence of humans, Woody, a pullstring cowboy doll, is the leader of a group of toys that are owned by a boy named Andy Davis.",
                        81,
                        ['Animation', 'Adventure', 'Comedy'],
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "http://www.imdb.com/title/tt0114709/")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    162,
                    ['Action', 'Adventure', 'Fantasy'],
                    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=Fq00mCqBMY8",
                    "http://www.imdb.com/title/tt0499549/")

spirited_away = media.Movie("Spirited Away",
                            "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
                            125,
                            ['Anime', 'Animation', 'Adventure', 'Family'],
                            "http://ia.media-imdb.com/images/M/MV5BMjYxMDcyMzIzNl5BMl5BanBnXkFtZTYwNDg2MDU3._V1_UY268_CR4,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk",
                            "http://www.imdb.com/title/tt0245429/?")

school_of_rock = media.Movie("School of Rock",
                            "Rock musician becomes high school music teacher.",
                            108,
                            ['Comedy','Music'],
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.yotuube.com/watch?v=3PsUJFEBC74",
                            "http://www.imdb.com/title/tt0332379/?")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A screenwriter confronts his relationship by travelling back in time at midnight.",
                                94,
                                ['Comedy', 'Fantasy', 'Romance'],
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "http://www.imdb.com/title/tt1605783/")

ratatouille = media.Movie("Ratatouille",
                            "A rat who can cook makes an alliance with a young kitchen worker.",
                            111,
                            ['Animation', 'Comedy', 'Family'],
                            "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                            "http://www.imdb.com/title/tt0382932/")

hunger_games = media.Movie("Hunger Games",
                            "A girl must survive the oppressive regime's death games.",
                            142,
                            ['Adventure', 'Drama', 'Sci-Fi'],
                            "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=4S9a5V9ODuY",
                            "http://www.imdb.com/title/tt1392170/")

# Anime
cowboy_bebop = media.TVShow("Cowboy Bebop",
                            "A ragtag team of bounty hunters travelling through space.",
                            24,
                            ['Animation', 'Anime', 'Action', 'Adventure', 'Comedy', 'Drama', 'Sci-Fi', 'Space'],
                            "http://cdn.myanimelist.net/images/anime/4/19644.jpg",
                            "https://youtu.be/qig4KOK2R2g",
                            "http://myanimelist.net/anime/1/Cowboy_Bebop",
                            1, 26, False)

mononoke_hime = media.Movie("Mononoke Hime",
                            "When an Emishi village is attacked by a fierce demon boar, the young prince Ashitaka puts his life at stake to defend his tribe. With its dying breath, the beast curses the prince's arm, granting him demonic powers while gradually siphoning his life away. Instructed by the village elders to travel westward for a cure, Ashitaka arrives at Tatara, the Iron Town, where he finds himself embroiled in a fierce conflict: Lady Eboshi of Tatara, promoting constant deforestation, stands against Princess San and the sacred spirits of the forest, who are furious at the destruction brought by the humans. As the opposing forces of nature and mankind begin to clash in a desperate struggle for survival, Ashitaka attempts to seek harmony between the two, all the while battling the latent demon inside of him. Princess Mononoke is a tale depicting the connection of technology and nature, while showing the path to harmony that could be achieved by mutual acceptance. [Written by MAL Rewrite]",
                            130,
                            ['Anime', 'Animation', 'Action', 'Adventure', 'Fantasy'],
                            "http://cdn.myanimelist.net/images/anime/7/75919.jpg",
                            "https://youtu.be/4OiMOHRDs14",
                            "http://myanimelist.net/anime/164/Mononoke_Hime")

full_metal_panic_fumoffu = media.TVShow("Full Metal Panic? Fumoffu",
                                        "Its back-to-school mayhem with Kaname Chidori and her war-freak classmate Sousuke Sagara as they encounter more misadventures in and out of Jindai High School.",
                                        24,
                                        ['Animation', 'Anime', 'Action', 'Comedy', 'School'],
                                        "http://cdn.myanimelist.net/images/anime/4/75260.jpg",
                                        "https://youtu.be/UaZEknOT0HA",
                                        "http://myanimelist.net/anime/72/Full_Metal_Panic_Fumoffu",
                                        1, 12, False)

ergo_proxy = media.TVShow("Ergo Proxy",
                        "The world is bigger than you think... After the explosion of the methane hydrate layer, the remaining members of mankind are forced to live in isolated domed cities scattered across the arid and inhospitable planet. They live in a controlled society and are assisted in daily life by autonomous robots called AutoReivs. In one of these cities, Romdo, Inspector Re-l Mayer, granddaughter of the regent, leads an investigation concerning AutoReivs that have gone mad after being infected by the Cogito virus. In the process, she comes in contact with a monster called Proxy. Elsewhere in the city, immigrant Vincent Law is on the run after being framed for involvement in several Cogito cases. Together, along with the adorable child-AutoReiv Pino, they set out on a journey to the dome city Mosk in order to unravel the mystery of the Proxies.",
                        25,
                        ['Animation', 'Anime', 'Mystery', 'Psychological', 'Sci-Fi'],
                        "http://cdn.myanimelist.net/images/anime/11/6259.jpg",
                        "https://youtu.be/WjTPHVz6OOg",
                        "http://myanimelist.net/anime/790/Ergo_Proxy",
                        1, 23, False)

ghost_in_the_shell_sac = media.TVShow("Ghost in the Shell: Stand Alone Complex",
                                    "In the not so distant future, mankind has advanced to a state where complete body transplants from flesh to machine is possible. This allows for great increases in both physical and cybernetic prowess and blurring the lines between the two worlds. However, criminals can also make full use of such technology, leading to new and sometimes, very dangerous crimes. In response to such innovative new methods, the Japanese Government has established Section 9, an independently operating police unit which deals with such highly sensitive crimes. Led by Daisuke Aramaki and Motoko Kusanagi, Section 9 deals with such crimes over the entire social spectrum, usually with success. However, when faced with a new A level hacker nicknamed 'The Laughing Man,' the team is thrown into a dangerous cat and mouse game, following the hacker's trail as it leaves its mark on Japan. [Written by MAL Rewrite]",
                                    25,
                                    ['Animation', 'Anime', 'Action', 'Mecha', 'Military', 'Police', 'Sci-Fi', 'Seinen'],
                                    "http://cdn.myanimelist.net/images/anime/11/50857.jpg",
                                    "https://youtu.be/SY6PNTzQb1A",
                                    "http://myanimelist.net/anime/467/Ghost_in_the_Shell__Stand_Alone_Complex",
                                    1, 26, False)

nichijou = media.TVShow("Nichijou",
                        "Nichijou primarily focuses on the daily antics of a trio of childhood friends—high school girls Mio Naganohara, Yuuko Aioi and Mai Minakami—whose stories soon intertwine with the young genius Hakase Shinonome, her robot caretaker Nano, and their talking cat Sakamoto.",
                        23,
                        ['Animation', 'Anime', 'Comedy', 'School', 'Slice of Life'],
                        "http://cdn.myanimelist.net/images/anime/3/75617.jpg",
                        "https://youtu.be/CD6VdVDVDXI",
                        "http://myanimelist.net/anime/10165/Nichijou",
                        1, 26, False)

if __name__ == '__main__':
    """Generates an HTML page with all video instances and opens it in a browser.

    Also generates HTML pages for movies and tv shows separately."""
    mediums = [media.Movie, media.TVShow]
    all_video = reduce(add, map(list, (medium.get_instances() for medium in mediums)))

    fresh_tomatoes.open_movies_page(all_video)
    for medium in mediums:
        fresh_tomatoes.render_page(medium.__name__, list(medium.get_instances()))
