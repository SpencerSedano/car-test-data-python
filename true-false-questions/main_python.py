import random
import csv


def main():
    # The main will
    # Read the dictionary
    data = csv_to_dict(
        "C:/Users/spenc/OneDrive/Desktop/python-car-test-data/python-car-test-data/true-false-questions/output/output3_all_pages.csv"
    )
    random_question(
        "C:/Users/spenc/OneDrive/Desktop/python-car-test-data/python-car-test-data/true-false-questions/output/output3_all_pages.csv"
    )


def csv_to_dict(file):
    with open(
        file,
        "r",
        # UTF-8 covers the Unicode characters which are a TON of languages and special characters
        encoding="utf8",  # utf8 or latin1 encoding works
    ) as file:
        dict_reader = csv.DictReader(file)
        data = [row for row in dict_reader]
        # There are about 654 indexes
        return data


def random_question(file):
    data = csv_to_dict(file)
    random_number_range = random.randrange(0, 654)
    print(random_number_range)
    question_number = data[random_number_range]["Number"]
    question_answer = data[random_number_range]["Answer"]
    print(question_answer)

    print(f"Question number: {question_number}")
    print(data[random_number_range]["Question"])
    user_answer = input("Choose O or X: ")

    if user_answer == question_answer:
        print(f"Congratulations!\nAnswer is: {question_answer}")
    else:
        print(f"Try again :(\nAnswer is: {question_answer}")


if __name__ == "__main__":
    main()
