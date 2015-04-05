__author__ = 'ralph'

import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=_KFpws6qmuw")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)
print(toy_story.storyline)
print(avatar.storyline)
avatar.show_trailer()