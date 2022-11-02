"""
Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:

1.Define your input format (one or many records)
2.Default folder or user provided file path
3.Remove file if it was successfully processed
"""

import xml.etree.ElementTree
from datetime import datetime, date  # Import module datetime for dates and time use
from random import randint  # Import random module for numbers generation
from hw_04 import splitting_sentences, normalize_text  # Import text splitting and normalization functions
import os  # Import module os for file system use
import re  # Import module re for regular expressions use
import csv  # Import csv module for csv parsing
import json  # Import json module for reading and writing JSONs
import xml.etree.ElementTree as ET  # Import xml module for XML parsing

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
    default_file_name = 'source_text.txt'

    def __init__(self, file_path: str):
        """Accepts parameter for finding text file - file path"""
        self.file_path = file_path

    @classmethod
    def get_file_path(cls) -> 'TextFile':
        """Reads user input and saves it as file path"""
        while True:
            file_path = input('Enter file path (keep empty input for default path): ')
            if file_path == '':  # If user left empty input - used default path
                file_path = f'{os.getcwd()}\\{cls.default_file_name}'
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


class JsonFile(TextFile):
    """Generates news items from JSON file"""
    default_file_name = 'source.json'

    def __init__(self, file_path: str):
        """Inherits file path approach from TextFile class"""
        super().__init__(file_path)

    def read_and_save_json_to_newsfeed(self):
        """Reads JSON file and applies writing logic from previous classes"""
        with open(self.file_path, 'r') as file:
            json_list = json.load(file)

        try:
            for json_object in json_list:
                if json_object['type'] == 'news':  # applies logic from News class
                    news = News(json_object["text"], json_object["city"])
                    news.save_news_to_file()
                elif json_object['type'] == 'ad':  # applies logic from Advertising class
                    ad_date = datetime.strptime(json_object['due_date'], "%Y-%m-%d")
                    ad = Advertising(json_object["text"], ad_date.date())
                    ad.save_ad_to_file()
                elif json_object['type'] == 'recipe':  # applies logic from Recipes class
                    recipe = Recipes(json_object["text"], int(json_object["time"]))
                    recipe.save_recipe_to_file()
                elif json_object is None:  # if JSON file is empty rise exception
                    raise KeyError
                else:
                    raise KeyError
            os.remove(self.file_path)  # Delete source file after successful run
        except KeyError:
            print('Incorrect JSON format or news type, please try different file')


class Xml(TextFile):
    """Generates news items from XML file"""
    default_file_name = 'source.xml'

    def __init__(self, file_path: str):
        """Inherits file path approach from TextFile class"""
        super().__init__(file_path)

    def read_and_save_xml_to_newsfeed(self):
        """Reads XML file and applies writing logic from previous classes"""
        try:
            # parse XML file
            tree = ET.parse(self.file_path)
            root = tree.getroot()

            # iterate over child items and get data for each news type
            for child in root.findall('item'):
                if child.attrib['type'] == 'news':
                    news_text = child.find('news_text').text  # get news text
                    city = child.find('city').text  # get city
                    news = News(news_text, city)  # applies logic from News class
                    news.save_news_to_file()
                elif child.attrib['type'] == 'ad':
                    ad_text = child.find('ad_text').text  # get ad text
                    due_date = child.find('due_date').text  # get exp date
                    ad_date = datetime.strptime(due_date, "%Y-%m-%d")  # change date format for delta calc
                    ad = Advertising(ad_text, ad_date.date())  # applies logic from Advertising class
                    ad.save_ad_to_file()
                elif child.attrib['type'] == 'recipe':
                    recipe_text = child.find('recipe_text').text  # get recipe text
                    time = child.find('time').text  # get cooking time
                    recipe = Recipes(recipe_text, int(time))  # applies logic from Recipes class
                    recipe.save_recipe_to_file()
            os.remove(self.file_path)  # Delete source file after successful run
        except xml.etree.ElementTree.ParseError:  # handle exception, if XML file is empty or incorrect
            print('Incorrect XML format, please try different file')


def count_words_and_save_to_csv():
    """Counts each word occurrence in the newsfeed file and saves it to csv"""
    with open(FILE_NAME, 'r') as newsfeed:
        content = newsfeed.read()
        content = content.lower()  # all words are preprocessed in lowercase
        words = re.findall(r"[a-z']+", content)  # get list of all words
        words_storage = {}

        # count word occurrence
        for word in words:
            if word in words_storage:
                words_storage[word] = words_storage[word] + 1
            else:
                words_storage[word] = 1

    # Write words and counts with '-' delimiter to csv
    with open('words_count.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='-')
        writer.writerows(words_storage.items())


def count_letters_and_save_to_csv():
    """Counts letters, uppercase letters, percentage and writes it to csv"""
    with open(FILE_NAME, 'r') as newsfeed:
        content = newsfeed.read()
        all_letters = re.findall(r"([a-zA-Z])", content)  # get list of all letters
        csv_output = []
        letter_data = {}
        total_letter_count = len(all_letters)  # get total count of all letters

        # calculations for letters (total and uppercase) count
        for letter in all_letters:
            letter_uppercase = letter.upper()
            is_uppercase = letter == letter_uppercase  # define if letter is in uppercase or not
            # get count of uppercase letters
            count_uppercase = 0
            if is_uppercase:
                count_uppercase += 1
            # define initial data in dict
            if letter_uppercase not in letter_data:
                letter_data[letter_uppercase] = {
                    'letter': letter.upper(),
                    'count_all': 1,
                    'count_uppercase': count_uppercase,
                    'percentage': 0
                }
            else:
                letter_data[letter_uppercase]['count_all'] += 1  # calc letter count
                letter_data[letter_uppercase]['count_uppercase'] += count_uppercase  # calc uppercase letter count

        # calc letter percentage and create final list of dicts
        for count_percentage in letter_data.values():
            count_percentage['percentage'] = round((count_percentage['count_all'] / total_letter_count) * 100, 1)
            csv_output.append(count_percentage)

        # Write letters with all calculations and header to csv
        with open('letters_count.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, ['letter', 'count_all', 'count_uppercase', 'percentage'])
            writer.writeheader()
            writer.writerows(csv_output)


def main():
    """Initiates news generation"""
    while True:  # Choose action or exit program
        action = input("""Choose action:
        a - Add News from user input
        b - Add Private ad from user input
        c - Add Recipes from user input
        d - Add items from text file
        e - Add items from JSON
        f - Add items from XML
        j - Exit news feed generator\n""")

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
            from_json = JsonFile.get_file_path()
            from_json.read_and_save_json_to_newsfeed()
            print('---All valid entries added---')
        elif action == 'f':
            from_xml = Xml.get_file_path()
            from_xml.read_and_save_xml_to_newsfeed()
            print('---All valid entries added---')
        elif action == 'j':
            print('Exiting news feed generator...')
            break
        else:
            print('Incorrect input, please enter one of the provided options')

    # Data for csv files recalculates each time after user exit
    count_words_and_save_to_csv()
    count_letters_and_save_to_csv()


# This code will execute only if current file was run directly, and not imported
if __name__ == '__main__':
    main()
