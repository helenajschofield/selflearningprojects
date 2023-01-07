# I completed this mini project on extracting files from a CSV for the final assessment of Code First Girls' 8-week kickstarter on Python and Apps.


# Option 3: Using sales.csv file,
# 1) read the data from the spreadsheet,
# 2) Collect all of the sales from each month into a single list
# 3) Output the total sales across all months
# Extension - Calculate the average
# Extension - Calculate months with highest and lowest sales

# task 1 - read data from csv
import csv

data = []

with open('sales.csv','r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)
    for row in spreadsheet:
        data.append(row)

print('Contents of spreadsheet ' + str(data))

# task 2 - collect sales from each month into a single list
all_sales = []
for row in data:
    sale = int(row['sales'])
    all_sales.append(sale)

print('All sales from each month ' + str(all_sales))

# task 3 - output total sales across all months
total = sum(all_sales)

print('Total sales: ' + str(total))

# extension 1 - average monthly sales
average_monthly_sales = total / len(all_sales)
print('Average monthly sales: ' + str(average_monthly_sales))

# extension 2 - months with highest and lowest sales
highest = data[0]
lowest = data[0]
for row in data:
    if row['sales'] > highest['sales']:
        highest = row
    if row['sales'] < lowest['sales']:
        lowest = row

print('Month with highest sales: ' + highest['month'] + ' ' + highest['year'] + ' (' + highest['sales'] + ')')
print('Month with lowest sales: ' + lowest['month'] + ' ' + lowest['year'] + ' (' + lowest['sales'] + ')')

