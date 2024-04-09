import csv
from quiz.models import Question


CSV_PATH = "test.csv"


Question.objects.all().delete()


with open(CSV_PATH, encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    print("loading...")
    for row in reader:
        Question.objects.create(
            question_number=row[0],
            question_answer=row[1],
            question_text=row[2],
        )
        print(row)
