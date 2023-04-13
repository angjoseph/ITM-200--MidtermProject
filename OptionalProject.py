import csv
import matplotlib.pyplot as plt

#Step 1: Reading CSV File
with open('Data.csv', mode = 'r') as fileCSV: # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)                  # Reading the csv file
    for line in fCSV:
      print(line)


#Step 2:Total Sale
with open('data.csv', 'r') as file: # Open the data file and read the contents
    data = file.readlines()

totalV = {}# Initialize a dictionary to store the total vehicles sold in each year

for line in data[1:]:# Loop through the lines in the data file

    # Split the line into a list of values
    values = line.strip().split(',')

    # Get the year from the first value in the list
    year = int(values[0])

    # Get the total number of vehicles sold for the year
    total = sum([int(v) for v in values[1:]])

    # Add the total to the dictionary
    totalV[year] = total

# Write the results to a file
with open('stats.txt', 'w') as file:
    for year, total in totalV.items():
        file.write(f'{year}: {total}\n')

#Step 3: Bar Plot
plt.bar(totalV.keys(), totalV.values())

plt.title('Total Vehicle Sales by Year')# Set the chart title and axis labels

plt.xlabel('Year')
plt.ylabel('Number of Vehicles Sold')

plt.show()# Display the chart


#Step 4: Sale Estimation
# Read the data file
with open('Data.csv', 'r') as file:
    data = file.readlines()

sales_2021 = []# Initialize variables to store the sales data
sales_2022 = []

for line in data[1:]:# Loop through the data and extract the sales data for 2021 and 2022
    values = line.strip().split(',')
    if int(values[0]) == 2021:
        sales_2021.extend([int(v) for v in values[1:7]])
        sales_2022.extend([0] * 6)
    elif int(values[0]) == 2022:
        sales_2022.extend([int(v) for v in values[1:7]])

total_sales_2021 = sum(sales_2021)# Calculate the total sales for the first 6 months of 2021 and 2022
total_sales_2022 = sum(sales_2022)

sgr = (total_sales_2022 - total_sales_2021) / total_sales_2021# Calculate the sales growth rate


# Calculate the estimated sales for the last 6 months of 2022
estimated_sales_2022 = [int(sales_2022[i+6] + sales_2022[i+6] * sgr) for i in range(6)]

# Write the results to the stats.txt file
with open('stats.txt', 'w') as file:
    file.write(f'Total sales in first 6 months of 2021: {total_sales_2021}\n')
    file.write(f'Total sales in first 6 months of 2022: {total_sales_2022}\n')
    file.write(f'Sales growth rate for first 6 months of 2022: {sgr}\n')
    file.write('Estimated sales for last 6 months of 2022:\n')
    for i, sales in enumerate(estimated_sales_2022):
        month = i + 7
        file.write(f'Month {month}: {sales}\n')

#Step 5: Horizontal Bar Plot
# Calculate the estimated sales for the last six months of 2022
estimated_sales_2022 = [data["Dec"][10] + data["Dec"][10] * SGR,
                        data["Nov"][10] + data["Nov"][10] * SGR,
                        data["Oct"][10] + data["Oct"][10] * SGR,
                        data["Sep"][10] + data["Sep"][10] * SGR,
                        data["Aug"][10] + data["Aug"][10] * SGR,
                        data["Jul"][10] + data["Jul"][10] * SGR]

# Plot the estimated sales for the last six months of 2022
import matplotlib.pyplot as plt

months = ["Dec", "Nov", "Oct", "Sep", "Aug", "Jul"]
plt.barh(months, estimated_sales_2022)
plt.title("Estimated Sales for Last Six Months of 2022")
plt.xlabel("Number of Vehicles Sold")
plt.ylabel("Month")
plt.show()
