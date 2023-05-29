class SportsNews:
    def sportsNews(self):
        print('Sports News')
        print('Sports News')
        print('Sports News')

class MoviesNews:
    def moviesNews(self):
        print('Movies News')
        print('Movies News')
        print('Movies News')

class PoliticsNews:
    def politicsNews(self):
        print('Politics News')
        print('Politics News')
        print('Politics News')

class MahbubNews:
    def __init__(self):
        self.sports = SportsNews()
        self.movies = MoviesNews()
        self.politics = PoliticsNews()
    def getTotalNews(self):
        print("All News")
        self.sports.sportsNews()
        self.movies.moviesNews()
        self.politics.politicsNews()

mnewsc = MahbubNews()
mnewsc.getTotalNews()