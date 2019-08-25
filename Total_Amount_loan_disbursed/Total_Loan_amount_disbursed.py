#  DATA_ANALYSIS_02
#   This Program is designed to analyse the data from the loan1.csv
#   ... and a bar chart is plotted to to show the Total Loan amount disbursed for each month in 2018 of LC
#   The data been analyzed is gotten from LendingClub Statistics through kaggle.com

# importing the libraries the would be used
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np
import csv
from itertools import zip_longest

#   preset styling of the graph
plt.style.use('fivethirtyeight')

def loan_amt(x, y):
#   opening the csv file i would be reading the data from

    loan_sheet = pd.read_csv('loan1.csv')
    issue_date = loan_sheet['issue_d']
    loan_term = loan_sheet['term']
#   adding up the total funded loan with the corresponding month
    t_funded_amnt = loan_sheet.loc[(issue_date == x) & (loan_term == y), 'funded_amnt'].sum()
    return t_funded_amnt

def main():
    loan_sheet = pd.read_csv('loan1.csv')
    id_issue_d = loan_sheet['issue_d']

    issue_d_count = Counter()

    for month in id_issue_d:
        issue_d_count.update(month.split(','))

    ini_months = []
    for key, value in issue_d_count.items():
        ini_months.append(key[3:9])
# Arranging the months in the right order
    ini_months.reverse()

    months = ini_months

#   evaluating the total sum of the funded loan under the short term of 36 months to its corresponding month
    funded_amnt_short = []

    total_funded_amnt = [loan_amt('18-Jan', ' 36 months'),
                         loan_amt('18-Feb', ' 36 months'),
                         loan_amt('18-Mar', ' 36 months'),
                         loan_amt('18-Apr', ' 36 months'),
                         loan_amt('18-May', ' 36 months'),
                         loan_amt('18-Jun', ' 36 months'),
                         loan_amt('18-Jul', ' 36 months'),
                         loan_amt('18-Aug', ' 36 months'),
                         loan_amt('18-Sep', ' 36 months'),
                         loan_amt('18-Oct', ' 36 months'),
                         loan_amt('18-Nov', ' 36 months'),
                         loan_amt('18-Dec', ' 36 months'),
                         ]
    for item in total_funded_amnt:
        funded_amnt_short.append(item)

    #   evaluating the total sum of the funded loan under the long term of 60 months to its corresponding month
    funded_amnt_long = []

    total_funded_amnt = [loan_amt('18-Jan', ' 60 mont60hs'),
                         loan_amt('18-Feb', ' 60 months'),
                         loan_amt('18-Mar', ' 60 months'),
                         loan_amt('18-Apr', ' 60 months'),
                         loan_amt('18-May', ' 60 months'),
                         loan_amt('18-Jun', ' 60 months'),
                         loan_amt('18-Jul', ' 60 months'),
                         loan_amt('18-Aug', ' 60 months'),
                         loan_amt('18-Sep', ' 60 months'),
                         loan_amt('18-Oct', ' 60 months'),
                         loan_amt('18-Nov', ' 60 months'),
                         loan_amt('18-Dec', ' 60 months'),
                         ]
    for item in total_funded_amnt:
        funded_amnt_long.append(item)

    #   plotting the graph
    months_index = np.arange(len(months))
    width = .25

    plt.bar(months_index - width, funded_amnt_short, width=width, color='#e5ae38', label='36 months loan term')

    plt.bar(months_index, funded_amnt_long, width=width, color='#008fd5', label='60 months loan term')

    plt.xlabel("Months")
    plt.ylabel(" Funded Amount (in USSD)")
    plt.title(" TOTAL AMOUNT OF LOAN DISBURSED IN 2018")
    plt.xticks(ticks=months_index, labels=months)
    plt.tight_layout()

    plt.legend()

    #   Writing the data extracted ("months", "funded_amnt_short", "funded_amnt_long") in another csv file
    #       This would be used to design the charts in the Dashboard
    d = [months, funded_amnt_short, funded_amnt_long]
    export_data = zip_longest(*d, fillvalue='')
    with open('total_loan_amnt.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("months", "funded_amnt_short", "funded_amnt_long"))
        wr.writerows(export_data)
    myfile.close()
    # --------- end of written doc. -------------

    plt.show()


main()
