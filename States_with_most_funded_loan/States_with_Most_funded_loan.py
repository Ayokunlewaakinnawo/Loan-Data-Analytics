#  DATA_ANALYSIS_03
#   This Program is designed to analyse the data from the loan1.csv
#   ... and a chart is plotted to to show the Counts of loan disbursed in each states in the US for 2018
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
    id_state = loan_sheet['addr_state']

    addr_state_count = Counter()

    for state in id_state:
        addr_state_count.update(state.split(','))

    state_key = []
    population =[]

    for item in addr_state_count.most_common():
        state_key.append(item[0])
        population.append(item[1])

#   plotting the graph
    state_key.reverse()
    population.reverse()

    plt.barh(state_key, population, )

    matplotlib.rc('xtick', labelsize=5)
    matplotlib.rc('ytick', labelsize=8)
    matplotlib.rc('axes', titlesize=8)


    plt.xlabel("Total count of loan disbursed", size =10)
    plt.ylabel("States in th United State of America")
    plt.title(" TOTAL COUNTS OF LOAN DISBURSED IN EACH STATES IN 2018", size=12)
    plt.tight_layout()

#   Writing the data extracted (state_key", "population) in another csv file
#       This would be used to design the charts in the Dashboard
    d = [state_key, population]
    export_data = zip_longest(*d, fillvalue='')
    with open('state_count.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("state_key", "population"))
        wr.writerows(export_data)
    myfile.close()
    # ---------end of written doc. -------------

    plt.show()

main()