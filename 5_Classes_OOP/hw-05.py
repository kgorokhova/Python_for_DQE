"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Private ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.

Each new record should be added to the end of file
"""

from datetime import datetime, date  # Import module datetime for dates and time use
from random import randint  # Import random module for numbers generation

FILE_NAME = 'newsfeed.txt'  # Declare text file global variable as constant for usage in each class


class News:
    """Generates news for news feed"""
    def __init__(self, news_text: str, news_city: str):
        """Accepts parameters for news - text and city"""
        self.news_text = news_text
        self.news_city = news_city

    @classmethod
    def create_news_from_user_input(cls) -> 'News':
        """Reads user input and creates instance of current class and returns it"""
        news_text = input('Add news text: ')
        news_city = input('Add city: ')
        return cls(news_text, news_city)

    def save_news_to_file(self):
        """Adds posting datetime and saves current object to file"""
        datetime_now = datetime.now()  # get current datetime
        with open(FILE_NAME, 'a') as newsfeed:  # append new item to text file
            newsfeed.write(f'News -------------------------\n'
                           f'{self.news_text}\n'
                           f'{self.news_city}, {datetime_now.strftime("%Y-%m-%d %X")}\n'
                           f'------------------------------\n\n\n')


class Advertising:
    """Generates private ad for news feed"""
    def __init__(self, ad_text: str, ad_date: date):
        """Accepts parameters for private ad - text and expiration date"""
        self.ad_text = ad_text
        self.ad_date = ad_date

    @classmethod
    def create_ad_from_user_input(cls) -> 'Advertising':
        """Reads user input and creates instance of current class and returns it"""
        ad_text = input('Add ad text: ')
        # Generate expiration date and validate its format
        while True:
            try:
                year = int(input('Add expiration date, input year: '))
                month = int(input('Input month: '))
                day = int(input('Input day: '))
                ad_date = date(year, month, day)
                if ad_date < date.today():
                    print('Incorrect input, no past dates allowed')
                    continue
                return cls(ad_text, ad_date)
            except ValueError:
                print('Incorrect input, please enter integers for valid date')

    def save_ad_to_file(self):
        """Calculates remaining days and saves current object to file"""
        delta = self.ad_date - date.today()  # Find how much days left before advertisement ends
        with open(FILE_NAME, 'a') as newsfeed:  # append new item to text file
            newsfeed.write(f'Private Ad -------------------\n'
                           f'{self.ad_text}\n'
                           f'Actual until: {self.ad_date}, {delta.days} days left\n'
                           f'------------------------------\n\n\n')


class Recipes:
    """Generates cooking recipes for news feed"""
    def __init__(self, recipe_text: str, cooking_time: int):
        """Accepts parameters for recipes - text and cooking time"""
        self.recipe_text = recipe_text
        self.cooking_time = cooking_time

    @classmethod
    def create_recipe_from_user_input(cls) -> 'Recipes':
        """Reads user input and creates instance of current class and returns it"""
        recipe_text = input('Add recipe text: ')
        # Validate cooking time input
        while True:
            try:
                cooking_time = int(input('Add cooking time in minutes: '))
                if cooking_time < 1:
                    print('Incorrect input, cooking time cannot be less than 1 minute')
                    continue
                return cls(recipe_text, cooking_time)
            except ValueError:
                print('Incorrect input, please enter integer')

    def save_recipe_to_file(self):
        """Generates recipe difficulty rate and saves current object to file"""
        if self.cooking_time > 120:  # Get difficulty rate
            difficulty = randint(7, 10)
        else:
            difficulty = randint(1, 6)
        with open(FILE_NAME, 'a') as newsfeed:  # append new item to text file
            newsfeed.write(f'Recipe -----------------------\n'
                           f'{self.recipe_text}\n'
                           f'Cooking time: {self.cooking_time} min, difficulty rate: {difficulty}/10\n'
                           f'------------------------------\n\n\n')


def main():
    """Initiates news generation"""
    while True:  # Choose topic or exit program
        topic = input("""Choose topic:
        a - News
        b - Private ad
        c - Recipes
        d - Exit news feed generator\n""")

        # Initiate news generation depending on chosen topic
        if topic == 'a':
            news = News.create_news_from_user_input()
            news.save_news_to_file()
            print('---News added---')
        elif topic == 'b':
            ad = Advertising.create_ad_from_user_input()
            ad.save_ad_to_file()
            print('---New advertising added---')
        elif topic == 'c':
            recipe = Recipes.create_recipe_from_user_input()
            recipe.save_recipe_to_file()
            print('---New recipe added---')
        elif topic == 'd':
            print('Exiting news feed generator...')
            break
        else:
            print('Incorrect input, please enter one of the provided options')


# This code will execute only if current file was run directly, and not imported
if __name__ == '__main__':
    main()
