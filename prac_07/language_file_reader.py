import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, and display them."""
    languages = load_languages("languages.csv")
    # Display all the languages using their __str__ method
    for language in languages:
        print(language)


def load_languages(filename):
    """Load languages from a CSV file and return a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip the header line
        
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"  # Convert "Yes"/"No" to Boolean
            pointer_arithmetic = parts[3] == "Yes"  # Convert "Yes"/"No" to Boolean
            # Create a ProgrammingLanguage object
            language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic, int(parts[4]))
            languages.append(language)
    return languages


def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in reader:
            print(row)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)
        # Create a namedtuple class called 'Language'
        Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
        reader = csv.reader(in_file)

        for row in reader:
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    with open("languages.csv", "r", newline='') as in_file:
        next(in_file)  # Skip the header
        # Create a namedtuple class called 'Language'
        Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
        for language in map(Language._make, csv.reader(in_file)):
            print(f"{language.name} was released in {language.year}")
            print(repr(language))

main()
    
