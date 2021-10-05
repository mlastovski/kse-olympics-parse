# from os import replace, getcwd
import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='Process some data.')
parser.add_argument('path', metavar='N', type=str, help='path to the file')
parser.add_argument('-medals', type=str, help='enter country')
parser.add_argument('year', type=int, help='enter year')
parser.add_argument('-output', nargs='?', type=str)



args = parser.parse_args()

path = sys.argv[1]
medals_input = sys.argv[2]
country_input = sys.argv[3]
year_input = sys.argv[4]
# print(year_input)

with open(path) as csvfile:
    result = []

    reader = csv.reader(csvfile)

    for row in reader:
        article = {}
        article["id"] = row[0]
        article["name"] = row[1]
        article["country"] = row[6]
        article["country_short"] = row[7]
        article["year"] = row[9]
        article["game"] = row[12]
        article["medal"] = row[14]
        result.append(article)

# print(result)

formatted_list = []

for d in result:
    if year_input in d.values() and country_input in d.values():
        if d['medal'] == 'Bronze' or d['medal'] == 'Silver' or d['medal'] == 'Gold':
            formatted_list.append(d)

check_country = []
for countries in result:
    # print(bool(country_input in countries.values()))
    if bool(country_input in countries.values()) == False:
        check = 0
    else:
        check = 1
    check_country.append(check)

if 1 not in check_country:
    answer = 'There is no such country.'
    print(answer)
    exit()

check_year = []
for years in result:
    # print(bool(country_input in countries.values()))
    if bool(year_input in years.values()) == False:
        check = 0
    elif int(year_input) < 1896:
        check = 0
    else:
        check = 1
    check_year.append(check)

if 1 not in check_year:
    answer = 'this year the Olympiad was not held.'
    print(answer)
    exit()


# print(len(formatted_list))
if len(formatted_list) < 10:
    answer = 'This country has less than 10 medals.' + '\n'
    print(answer)


# print(formatted_list)
# print('\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n')

ten_first = formatted_list[:10]
# print(ten_first)
# print('\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n')

outputs = []
for e in ten_first:
    output = e['name'] + ' - ' + e['game'] + ' - ' + e['medal']
    outputs.append(output)
    print(output)

gold = len([i for i in formatted_list if i['medal'] == 'Gold'])
silver = len([i for i in formatted_list if i['medal'] == 'Silver'])
bronze = len([i for i in formatted_list if i['medal'] == 'Bronze'])

total = country_input + ' in ' + str(year_input) + ': ' + str(gold) + ' gold medals, ' + str(silver) + ' silver medals, ' + str(bronze) + ' bronze medals.'
print('\n' + total)

if sys.argv[5]:
    file_name = sys.argv[6]
    f = open(file_name, 'w')

    for x in range(len(outputs)):
        f.write(outputs[x] + '\n')
    f.write('\n')
    f.write(total)
    f.close()
