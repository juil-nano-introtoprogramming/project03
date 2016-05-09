#!python
# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

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

school_of_rock = media.Movie("School of Rock",
                            "Rock musician becomes high school music teacher.",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.yotuube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A screenwriter confronts his relationship by travelling back in time at midnight.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

ratatouille = media.Movie("Ratatouille",
                            "A rat who can cook makes an alliance with a young kitchen worker.",
                            "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
                            "A girl must survive the oppressive regime's death games.",
                            "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# Anime
cowboy_bebop = media.Movie("Cowboy Bebop",
                            "A ragtag team of bounty hunters travelling through space.",
                            "http://cdn.myanimelist.net/images/anime/4/19644.jpg",
                            "https://youtu.be/qig4KOK2R2g")

mononoke_hime = media.Movie("Mononoke Hime",
                            "When an Emishi village is attacked by a fierce demon boar, the young prince Ashitaka puts his life at stake to defend his tribe. With its dying breath, the beast curses the prince's arm, granting him demonic powers while gradually siphoning his life away. Instructed by the village elders to travel westward for a cure, Ashitaka arrives at Tatara, the Iron Town, where he finds himself embroiled in a fierce conflict: Lady Eboshi of Tatara, promoting constant deforestation, stands against Princess San and the sacred spirits of the forest, who are furious at the destruction brought by the humans. As the opposing forces of nature and mankind begin to clash in a desperate struggle for survival, Ashitaka attempts to seek harmony between the two, all the while battling the latent demon inside of him. Princess Mononoke is a tale depicting the connection of technology and nature, while showing the path to harmony that could be achieved by mutual acceptance. [Written by MAL Rewrite]",
                            "http://cdn.myanimelist.net/images/anime/7/75919.jpg",
                            "https://youtu.be/4OiMOHRDs14")

full_metal_panic_fumoffu = media.Movie("Full Metal Panic? Fumoffu",
                                        "Its back-to-school mayhem with Kaname Chidori and her war-freak classmate Sousuke Sagara as they encounter more misadventures in and out of Jindai High School.",
                                        "http://cdn.myanimelist.net/images/anime/4/75260.jpg",
                                        "https://youtu.be/UaZEknOT0HA")

ergo_proxy = media.Movie("Ergo Proxy",
                        "The world is bigger than you think... After the explosion of the methane hydrate layer, the remaining members of mankind are forced to live in isolated domed cities scattered across the arid and inhospitable planet. They live in a controlled society and are assisted in daily life by autonomous robots called AutoReivs. In one of these cities, Romdo, Inspector Re-l Mayer, granddaughter of the regent, leads an investigation concerning AutoReivs that have gone mad after being infected by the Cogito virus. In the process, she comes in contact with a monster called Proxy. Elsewhere in the city, immigrant Vincent Law is on the run after being framed for involvement in several Cogito cases. Together, along with the adorable child-AutoReiv Pino, they set out on a journey to the dome city Mosk in order to unravel the mystery of the Proxies.",
                        "http://cdn.myanimelist.net/images/anime/11/6259.jpg",
                        "https://youtu.be/WjTPHVz6OOg")

ghost_in_the_shell_sac = media.Movie("Ghost in the Shell: Stand Alone Complex",
                                    "In the not so distant future, mankind has advanced to a state where complete body transplants from flesh to machine is possible. This allows for great increases in both physical and cybernetic prowess and blurring the lines between the two worlds. However, criminals can also make full use of such technology, leading to new and sometimes, very dangerous crimes. In response to such innovative new methods, the Japanese Government has established Section 9, an independently operating police unit which deals with such highly sensitive crimes. Led by Daisuke Aramaki and Motoko Kusanagi, Section 9 deals with such crimes over the entire social spectrum, usually with success. However, when faced with a new A level hacker nicknamed 'The Laughing Man,' the team is thrown into a dangerous cat and mouse game, following the hacker's trail as it leaves its mark on Japan. [Written by MAL Rewrite]",
                                    "http://cdn.myanimelist.net/images/anime/11/50857.jpg",
                                    "https://youtu.be/SY6PNTzQb1A")

nichijou = media.Movie("Nichijou",
                        "Nichijou primarily focuses on the daily antics of a trio of childhood friends—high school girls Mio Naganohara, Yuuko Aioi and Mai Minakami—whose stories soon intertwine with the young genius Hakase Shinonome, her robot caretaker Nano, and their talking cat Sakamoto.",
                        "http://cdn.myanimelist.net/images/anime/3/75617.jpg",
                        "https://youtu.be/CD6VdVDVDXI")

if __name__ == '__main__':
    movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, spirited_away]
    anime = [spirited_away, nichijou, ghost_in_the_shell_sac, ergo_proxy, full_metal_panic_fumoffu, mononoke_hime, cowboy_bebop]
    fresh_tomatoes.open_movies_page(anime)
