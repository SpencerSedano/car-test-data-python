import random
import csv


def main():
    # The main function will call functions

    csv_path = "C:/Users/spenc/OneDrive/Desktop/python-car-test-data/python-car-test-data/true-false-questions/output/output3_all_pages.csv"

    random_question(csv_path)


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
    random_number_range = random.randrange(0, len(data))
    print(len(data))
    question_number = data[random_number_range]["Number"]
    question_answer = data[random_number_range]["Answer"]
    question_question = data[random_number_range]["Question"]
    """ print(
        data[636]
    )  """  # The original PDF file goes from 635 to 641, so it will be the same for the CSV
    print(question_answer)

    print(f"Question number: {question_number}")
    print(f"{question_question}")

    return data[636]

    """ user_input(question_answer) """


def user_input(question_answer):
    # Pytest are often not used with input, but if I want to test and have this input
    # I will need more complex knowleadge and I think I will need Mock module
    """answer = input("Choose O or X: ")"""
    answer = "X"

    if answer == question_answer:
        print(f"Congratulations!\nAnswer is: {question_answer}")
    else:
        print(f"Try again :(\nAnswer is: {question_answer}")

    return answer


if __name__ == "__main__":
    main()
