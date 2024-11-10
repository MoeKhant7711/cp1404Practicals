import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    with open('languages.csv', 'r') as in_file:
        # Skip the header
        in_file.readline()

        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[3] == "Yes"

            # Create ProgrammingLanguage object
            language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic, int(parts[4]))
            languages.append(language)

    for language in languages:
        print(language)


def using_csv():
    """Read and print data using csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Skip header
        reader = csv.reader(in_file)

        for row in reader:
            print(row)


def using_namedtuple():
    """Read and print data using namedtuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Skip header
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)

        Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
        reader = csv.reader(in_file)

        for row in reader:
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Read and print data using both csv and namedtuple."""
    Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')

    with open('languages.csv', 'r') as in_file:
        in_file.readline()  # Skip header
        for language in map(Language._make, csv.reader(in_file)):
            print(language.name, 'was released in', language.year)
            print(repr(language))


if __name__ == "__main__":
    main()
   
