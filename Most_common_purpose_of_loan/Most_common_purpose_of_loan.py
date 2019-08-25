#  DATA_ANALYSIS_05
#   This Program is designed to analyse the data from the loan1.csv
#   ... and a chart is plotted to to show the Most common purpose of collection the loan in 2018
#   The data been analyzed is gotten from LendingClub Statistics through kaggle.com

# importing the libraries the would be used
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import csv
from itertools import zip_longest

def main():
    loan_sheet = pd.read_csv('loan1.csv')
    id_purpose = loan_sheet['purpose']

    purpose_count = Counter()

    for purpose in id_purpose:
        purpose_count.update(purpose.split(','))

    purpose_key = []
    popularity =[]

    for item in purpose_count.most_common():
        purpose_key.append(item[0])
        popularity.append(item[1])

#   plotting the graph
    purpose_key.reverse()
    popularity.reverse()

    plt.barh(purpose_key, popularity )

    matplotlib.rc('xtick', labelsize=8)
    matplotlib.rc('ytick', labelsize=8)
    matplotlib.rc('axes', titlesize=8)


    plt.xlabel("Total count of loan", size =10)
    plt.ylabel("Purpose")
    plt.title(" TOTAL COUNTS FOR PURPOSE OF LOAN IN 2018", size=12)
    plt.tight_layout()

    #   Writing the data extracted (purpose_key & popularity) in another csv file
    #       This would be used to design the charts in the Dashboard
    d = [purpose_key, popularity]
    export_data = zip_longest(*d, fillvalue='')
    with open('purpose_count.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("purpose_key", "popularity"))
        wr.writerows(export_data)
    myfile.close()
    # ---------end of written doc. -------------

    plt.show()


main()