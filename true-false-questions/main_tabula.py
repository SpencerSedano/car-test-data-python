""" from PyPDF2 import PdfReader

reader = PdfReader(
    "C:/Users/spenc/OneDrive/Desktop/python-car-test-data/true-false-questions/file.pdf"
)
count = 0
number_of_pages = len(reader.pages)
print(f"This is the number of PAGES: {number_of_pages}")
for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)
    count += 1

print(f"The loop went: {count} times")

 """

import tabula

""" df = tabula.read_pdf(
    "C:/Users/spenc/OneDrive/Desktop/python-car-test-data/true-false-questions/file.pdf",
    pages="all",
) """

tabula.convert_into(
    "C:/Users/spenc/OneDrive/Desktop/python-car-test-data/true-false-questions/file.pdf",
    "output3_all_pages.csv",
    output_format="csv",
    pages="all",
    lattice=True,  # It does not counts each new line as a new question, if it is False, it does not work as expected
)
