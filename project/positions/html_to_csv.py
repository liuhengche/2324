from bs4 import BeautifulSoup
import csv

# Specify the path to your HTML file
html_file_path = r'D:\documents\GitHub\2324\project\positions\james_harden.html'

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the header row
header = [th.get_text(strip=True) for th in soup.find('thead').find_all('th')]

# Find all data rows
rows = soup.find('tbody').find_all('tr')

# Store data
data = []
for row in rows:
    row_data = [td.get_text(strip=True) for td in row.find_all('td')]
    data.append(row_data)

# Write data to a CSV file
harden_csv_file_path = r'D:\documents\GitHub\2324\project\positions\james_harden.csv'
iverson_csv_file_path = r'D:\documents\GitHub\2324\project\positions\allen_iverson.csv'
lebron_csv_file_path = r'D:\documents\GitHub\2324\project\positions\lebron_james.csv'

with open(harden_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)
print(f"Data has been written to {harden_csv_file_path}")







# Specify the path to your HTML file
html_file_path = r'D:\documents\GitHub\2324\project\positions\allen_iverson.html'

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the header row
header = [th.get_text(strip=True) for th in soup.find('thead').find_all('th')]

# Find all data rows
rows = soup.find('tbody').find_all('tr')

# Store data
data = []
for row in rows:
    row_data = [td.get_text(strip=True) for td in row.find_all('td')]
    data.append(row_data)

# Write data to a CSV file
harden_csv_file_path = r'D:\documents\GitHub\2324\project\positions\james_harden.csv'
iverson_csv_file_path = r'D:\documents\GitHub\2324\project\positions\allen_iverson.csv'
lebron_csv_file_path = r'D:\documents\GitHub\2324\project\positions\lebron_james.csv'

with open(iverson_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)
print(f"Data has been written to {iverson_csv_file_path}")


# Specify the path to your HTML file
html_file_path = r'D:\documents\GitHub\2324\project\positions\lebron_james.html'

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the header row
header = [th.get_text(strip=True) for th in soup.find('thead').find_all('th')]

# Find all data rows
rows = soup.find('tbody').find_all('tr')

# Store data
data = []
for row in rows:
    row_data = [td.get_text(strip=True) for td in row.find_all('td')]
    data.append(row_data)

# Write data to a CSV file
harden_csv_file_path = r'D:\documents\GitHub\2324\project\positions\james_harden.csv'
iverson_csv_file_path = r'D:\documents\GitHub\2324\project\positions\allen_iverson.csv'
lebron_csv_file_path = r'D:\documents\GitHub\2324\project\positions\lebron_james.csv'

with open(lebron_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)
print(f"Data has been written to {lebron_csv_file_path}")