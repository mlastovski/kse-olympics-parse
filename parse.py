import csv
import argparse

parser = argparse.ArgumentParser(description='Process some data.')
parser.add_argument('path', metavar='N', type=str, help='path to the file')
parser.add_argument('-medals', type=str, nargs='*', help='enter country')
parser.add_argument('-year', type=int, help='enter year')
parser.add_argument('-output', nargs='?', type=str)

args = parser.parse_args()

path = str(args.path)
country_input = args.medals
if len(country_input) > 1:
    country_input = ' '.join(country_input)
else:
    country_input = ''.join(country_input)
year_input = str(args.year)

with open(path) as csvfile:
    result = []
    reader = csv.reader(csvfile)

    for row in reader:
        article = {
            'id': row[0],
            'name': row[1],
            'country': row[6],
            'country_short': row[7],
            'year': row[9],
            'game': row[12],
            'medal': row[14],
        }
        result.append(article)

formatted_list = []

for d in result:
    if year_input in d.values() and country_input in d.values():
        if d['medal'] == 'Bronze' or d['medal'] == 'Silver' or d['medal'] == 'Gold':
            formatted_list.append(d)

check_country = []
for countries in result:
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

if len(formatted_list) < 10:
    answer = 'This country has less than 10 medals.' + '\n'
    print(answer)

ten_first = formatted_list[:10]

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

if args.output:
    file_name = str(args.output)
    f = open(file_name, 'w')

    for x in range(len(outputs)):
        f.write(outputs[x] + '\n')
    f.write('\n')
    f.write(total)
    f.close()
