#  DATA_ANALYSIS_04
#   This Program is designed to analyse the data from the loan1.csv
#   ... and a bar chart graph is plotted to show the Loan count in terms of grade of each month in 2018 of LC
#   The data been analyzed is gotten from LendingClub Statistics through kaggle.com

# importing the libraries the would be used
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import operator
import csv
from itertools import zip_longest

#   preset styling of the graph
plt.style.use('fivethirtyeight')

def main():
    loan_sheet = pd.read_csv('loan1.csv')
    id_grade = loan_sheet['grade']

    grade_count = Counter()

    for grade_c in id_grade:
        grade_count.update(grade_c.split(','))

    s_grade_count = sorted(grade_count.items(), key=operator.itemgetter(0))
#   creating an empty list to which the values of the graph would be plotted in
#       x-axis for grade_key; y-axis for the grade_value

    grade_key = []
    grade_value_count = []

#   assigning items from the dict to the empty list created above
    for item in s_grade_count:
        grade_key.append(item[0])
        grade_value_count.append(item[1])

#   plotting the graph
    plt.bar(grade_key, grade_value_count)

    plt.xlabel("Grade")
    plt.ylabel("")
    plt.title("LOAN GRADE COUNT")

    plt.tight_layout()

#   Writing the data extracted (grade_key & grade_value_count) in another csv file
#       This would be used to design the charts in the Dashboard
    d = [grade_key, grade_value_count]
    export_data = zip_longest(*d, fillvalue='')
    with open('grade_count.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("grade_key", "grade_value_count"))
        wr.writerows(export_data)
    myfile.close()
    # --------- end of written doc. -------------

    plt.show()


main()