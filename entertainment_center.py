import media
import fresh_tomatoes

## Create the movie objects
toy_story = media.Movie('Toy Story', 'A story of a boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

#print toy_story.storyline

avatar = media.Movie('Avatar',
                     'A marine on another planet',
                     'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=-9ceBgWV8io')
#avatar.show_trailer()

avengers = media.Movie('The Avengers',
                       'Superheroes team up',
                       'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg',
                       'https://www.youtube.com/watch?v=eOrNdBpGMv8')

matrix = media.Movie('The Matrix',
                    'A man questions reality and becomes the hero of a new reality',
                    'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
                    'https://www.youtube.com/watch?v=vKQi3bBA1y8')
#matrix.show_trailer()

pulp_fiction = media.Movie('Pulp Fiction',
                           'Some badass stories',
                           'https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg',
                           'https://www.youtube.com/watch?v=s7EdQ4FqbhY')

school_of_rock = media.Movie('School of Rock',
                             'Using rock music to learn',
                             'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie('Ratatouille',
                          'A rat is a chef in Paris',
                          'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                          'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie('Midnight In Paris',
                                'Going back in time to meet authors',
                                'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                'https://www.youtube.com/watch?v=FAfR8omt-CY')

hunger_games = media.Movie('Hunger Games',
                           'A really real reality show',
                           'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')

## Create the list of movies to show
movies = [matrix, pulp_fiction, avengers, toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

## Create the website page and display it
fresh_tomatoes.open_movies_page(movies)
