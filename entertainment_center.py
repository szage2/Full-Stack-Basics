#I've stored here all data of the films I want to display on the website:
#title, date of release, storyline, category, directors, writers and stars of the films plus the url of the poster picture and the trailer.
#This is the program where I've imported the fresh tomatoe.py and media.py to use their contents.
#When entertainment_center.py runs it print out a short documentation and display the website with the movie trailers and data.

import fresh_tomatoes
import media

zootopia = media.Movie("Zootopia",
                        "(2016)",
                        "A Judy bemcomes the first bunny of cops and she faces some stereotypes and fights against them.",
                        "Category: Animation, Action, Adventure",
                        "Directors:  Byron Howard, Rich Moore",
                        "Writers:  Byron Howard (story by), Rich Moore (story by)",
                        "Stars:  Ginnifer Goodwin, Jason Bateman, Idris Elba",
                        "http://www.finalreel.co.uk/wp-content/uploads/2015/12/Zootopia-Poster.jpg",
                        "https://www.youtube.com/watch?v=Y0c3nKWhlIA")

spy = media.Movie("Spy",
                    "(2015)",
                    "A desk-bound CIA analyst go undercover to infiltrate the world of a deadly arms dealer.",
                    "Category:  Action, Comedy, Crime",
                    "Director: Paul Feig",
                    "Writer: Paul Feig",
                    "Stars:  Melissa McCarthy, Rose Byrne, Jude Law",
                    "http://nerdist.com/wp-content/uploads/2015/03/Spy_VerC_GoldMelissaPoster_sRGB9.jpg",
                    "https://www.youtube.com/watch?v=YrY3v1eDmQY")

enders_game = media.Movie("Ender's Game",
                "(2013)",
                "Young Ender Wiggin is recruited to lead the fight against the Formics, a genocidal alien race.",
                "Category: Action, Sci-Fi",
                "Director: Gavin Hood",
                "Writers: Gavin Hood (screenplay), Orson Scott Card",
                "Stars: Harrison Ford, Asa Butterfield, Hailee Steinfeld ",
                "http://cdn.collider.com/wp-content/uploads/enders-game-final-poster.jpg",
                "https://www.youtube.com/watch?v=2SRizeR4MmU")

forrest_gump = media.Movie("Forrest Gump",
                            "(1994)",
                            "Forrest Gump, while not intelligent, has accidentally been present at many historic moments",
                            "Category: Drama, Romance",
                            "Director: Robert Zemeckis",
                            "Writers: Winston Groom (novel), Eric Roth (screenplay)",
                            "Stars: Tom Hanks, Robin Wright, Gary Sinise ",
                            "https://1001scribbles.files.wordpress.com/2012/04/forrest-gump-poster1.jpg",
                            "https://www.youtube.com/watch?v=eYSnxZKTZzU")
exam = media.Movie("Exam",
                    "(2009)",
                    "The final candidates for a desirable job are locked in a room and given a test with one question.",
                    "Category: Mystery, Thriller",
                    "Director: Stuart Hazeldine",
                    "Writers: Stuart Hazeldine, Simon Garrity (story)",
                    "Stars: Adar Beck, Gemma Chan, Nathalie Cox ",
                    "https://laishizhou.files.wordpress.com/2013/02/p1669120386.jpg",
                    "https://www.youtube.com/watch?v=bkdt2Sygew0")

intouchables = media.Movie("Intouchables",
                            "(2011)",
                            "After a man becomes quadriplegic from a paragliding accident, he hires a young man to be his caregiver.",
                            "Category: Biography, Comedy, Drama",
                            "Directors:  Olivier Nakache, Eric Toledano ",
                            "Writers:  Olivier Nakache, Eric Toledano ",
                            "Stars:  Francois Cluzet, Omar Sy, Anne Le Ny ",
                            "http://www.wearemoviegeeks.com/wp-content/uploads/Intouchables-poster.jpg",
                            "https://www.youtube.com/watch?v=34WIbmXkewU")

sissi = media.Movie("Sissi",
                    "(1955)",
                    "Elisabeth, the young vibrant princess catches the eye of her sister's fiance, Emperor Franz Josef.",
                    "Category: Comedy, Drama, History",
                    "Director: Ernst Marischka",
                    "Writer: Ernst Marischka ",
                    "Stars: Romy Schneider, Karlheinz Bohm, Magda Schneider",
                    "http://ia.media-imdb.com/images/M/MV5BMTUxNDQ1ODU4OF5BMl5BanBnXkFtZTcwNzYwNTEzMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=cSLGzpKLg8k")

lucy = media.Movie("Lucy",
                    "(2014)",
                    "Lucy, caught in a dark deal, she transfors into a merciless warrior evolved beyond human logic.",
                    "Category: Action, Sci-Fi, Thriller",
                    "Director: Luc Besson",
                    "Writer: Luc Besson",
                    "Stars: Scarlett Johansson, Morgan Freeman, Min-sik Choi ",
                    "http://screenrant.com/wp-content/uploads/lucy-scarlett-johansson-poster.jpg",
                    "https://www.youtube.com/watch?v=MVt32qoyhi0")

back_to_the_future = media.Movie("Back to the Future",
                                "(1985)",
                                "A young man is sent thirty years into the past in Dr. Emmett Brown's time-traveling DeLorean.",
                                "Category: Adventure, Comedy, Sci-Fi",
                                "Director:  Robert Zemeckis ",
                                "Writers: Robert Zemeckis, Bob Gale ",
                                "Stars: Michael J. Fox, Christopher Lloyd, Lea Thompson ",
                                "http://imgc.allpostersimages.com/images/P-473-488-90/15/1555/PN9DD00Z/posters/back-to-the-future.jpg",
                                "https://www.youtube.com/watch?v=qvsgGtivCgs")

movies = [zootopia, spy, enders_game, forrest_gump, exam, intouchables, sissi, lucy, back_to_the_future]
print media.Movie.__doc__
# I call function open_movies_page from fline fresh_tomatoes.py and added a list 'movies' as the argument.
fresh_tomatoes.open_movies_page(movies)
