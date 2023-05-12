class Movies:

    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('Movie Name',self.title)
        print('Hero Name ' ,self.hero)
        print('Heroine Name ' , self.heroine)

movieLists = []

while True:
    title = input('Enter the Movie Name ')
    hero = input('Enter Hero Name')
    heroine = input('Enter the Heroine Name')
    m = Movies(title,hero,heroine)
    movieLists.append(m)
    print('Movie Inserted Successfully')
    option = input('Do you want insert more Movie [Yes/No]')
    if option.lower() == 'no':
        break
print('All Movies Informations : ')

for movie in movieLists:
    movie.info()
    print()

