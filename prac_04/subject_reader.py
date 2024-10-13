"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILE_PATH = "subject_data.txt" 
def main():
    subject_details = load_subject_data()  
    display_subject_data(subject_details)  

def load_subject_data():
    subjects = []  
    with open(FILE_PATH, 'r') as file: 
        for line in file:
            clean_line = line.strip()  
            details = clean_line.split(',')
            details[2] = int(details[2])  
            subjects.append(details)
    return subjects

def display_subject_data(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students enrolled.")  

main()
