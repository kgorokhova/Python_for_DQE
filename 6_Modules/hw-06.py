"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:

1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
4.Apply case normalization functionality form Homework 3/4
"""

from datetime import datetime, date  # Import module datetime for dates and time use
from random import randint  # Import random module for numbers generation
from hw_04 import splitting_sentences, normalize_text  # import text splitting and normalization functions
import os  # import module os for file system use

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


class TextFile:
    """Generates news items from text file"""
    def __init__(self, file_path: str):
        """Accepts parameter for finding text file - file path"""
        self.file_path = file_path

    @classmethod
    def get_file_path(cls) -> 'TextFile':
        """Reads user input and saves it as file path"""
        while True:
            file_path = input('Enter file path (keep empty input for default path): ')
            if file_path == '':  # If user left empty input - used default path
                file_path = f'{os.getcwd()}\\source_text.txt'
            # Validate file existence
            file_exists = os.path.isfile(file_path)
            if file_exists:
                print('File successfully found')
            else:
                print('File not found, please try again')
                continue
            return cls(file_path)

    def read_and_save_file_to_newsfeed(self):
        """Reads file, normalize news items and saves it to newsfeed file"""
        with open(self.file_path, 'r') as file:
            text_from_file = splitting_sentences(file.read())
            fixed_text = normalize_text(text_from_file)

        for news in splitting_sentences(fixed_text):  # append all news items to text file
            with open(FILE_NAME, 'a') as newsfeed:
                newsfeed.write(f'News form file ---------------\n'
                               f'{news}\n'
                               f'------------------------------\n\n\n')
        os.remove(self.file_path)  # Delete source file after all items was added


def main():
    """Initiates news generation"""
    while True:  # Choose action or exit program
        action = input("""Choose action:
        a - Add News
        b - Add Private ad
        c - Add Recipes
        d - Add text from file
        e - Exit news feed generator\n""")

        # Initiate news generation depending on chosen action
        if action == 'a':
            news = News.create_news_from_user_input()
            news.save_news_to_file()
            print('---News added---')
        elif action == 'b':
            ad = Advertising.create_ad_from_user_input()
            ad.save_ad_to_file()
            print('---New advertising added---')
        elif action == 'c':
            recipe = Recipes.create_recipe_from_user_input()
            recipe.save_recipe_to_file()
            print('---New recipe added---')
        elif action == 'd':
            from_file = TextFile.get_file_path()
            from_file.read_and_save_file_to_newsfeed()
            print('---All entries added---')
        elif action == 'e':
            print('Exiting news feed generator...')
            break
        else:
            print('Incorrect input, please enter one of the provided options')


# This code will execute only if current file was run directly, and not imported
if __name__ == '__main__':
    main()
