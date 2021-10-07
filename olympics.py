import csv
import argparse
import sys

parser = argparse.ArgumentParser(description='Process some data.')
parser.add_argument('path', metavar='PATH', type=str, help='Path to the file')
group = parser.add_mutually_exclusive_group()
group.add_argument('-medals', metavar='COUNTRY', type=str, nargs='*', required=False, help='Enter country')
group.add_argument('-total', metavar='YEAR', nargs='?', type=int, help='Specify year to display total quantity of medals')
parser.add_argument('-year', type=int, required=False, help='Specify year')
parser.add_argument('-output', metavar='PATH_TO_FILE', nargs='?', required=False, type=str, help='Enter name of the .txt file to write output to')

args = parser.parse_args()
# print(args)

path = str(args.path)
if args.medals:
    country_input = args.medals
    year_input = str(args.year)

    if args.year == None:
        print('Please specify a year')
        exit()

    if len(country_input) > 1:
        country_input = ' '.join(country_input)
    else:
        country_input = ''.join(country_input)

if args.total:
    year_input = str(args.total)

    if args.year:
        print('You are not allowed to use "-year" along with "-total".')
        exit()

with open(path) as csvfile:
    result = []
    reader = csv.reader(csvfile)

    for row in reader:
        article = {
            # 'id': row[0],
            'name': row[1],
            'country': row[6],
            'country_short': row[7],
            'year': row[9],
            'game': row[12],
            'medal': row[14],
        }
        result.append(article)

formatted_list = []

if args.medals:
    for d in result:
        if year_input in d.values() and country_input in d.values():
            if d['medal'] == 'Bronze' or d['medal'] == 'Silver' or d['medal'] == 'Gold':
                formatted_list.append(d)

if args.total:
    for d in result:
        if year_input in d.values():
            if d['medal'] == 'Bronze' or d['medal'] == 'Silver' or d['medal'] == 'Gold':
                formatted_list.append(d)

def check_years():
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
        answer = 'This year the Olympiad was not held.'
        print(answer)
        # exit()
        return answer
    
    return 'ok'


def check_countries():
    if args.medals:
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
            return answer
            # exit()

        return 'ok'
    
    else:
        return 'not ok'


ten_first = formatted_list[:10]
outputs = []
summary = []


def ten_first_medals():
    if len(formatted_list) < 10:
        answer = 'This country has less than 10 medals.' + '\n'
        print(answer)

    for e in ten_first:
        output = e['name'] + ' - ' + e['game'] + ' - ' + e['medal']
        outputs.append(output)
        print(output)

    gold = len([i for i in formatted_list if i['medal'] == 'Gold'])
    silver = len([i for i in formatted_list if i['medal'] == 'Silver'])
    bronze = len([i for i in formatted_list if i['medal'] == 'Bronze'])

    total = '\n' + country_input + ' in ' + str(year_input) + ': ' + str(gold) + ' gold medals, ' + str(silver) + ' silver medals, ' + str(bronze) + ' bronze medals.'
    summary.append(total)
    print('\n' + total)
    return total


def total_all_countries():
    countries_and_medals = []
    for e in formatted_list:
        match = e['country_short'] + ' - ' + e['medal']
        countries_and_medals.append(match)
    
    count = 0

    # print(countries_and_medals)
    set_medals = set(countries_and_medals)
    set_medals = list(set_medals)
    # print(set_medals)

    results = {}
    
    for item in set_medals:
        results[item] = countries_and_medals.count(item)

    print(results)



# total_list = []
# def total_by_year():
#     for d in result:
#         if year_input in d.values():
#             if d['medal'] == 'Bronze' or d['medal'] == 'Silver' or d['medal'] == 'Gold':
#                 total_list.append(d)

#     countries_and_medals = []
#     for e in total_list:
#         match = e['country_short'] + ' - ' + e['medal']
#         countries_and_medals.append(match)

#     count = 0

#     for i in countries_and_medals:
#         if i == match:
#             count +=1 


#     print(count)


def write_to_file():
    file_name = str(args.output)
    f = open(file_name, 'w')
    for x in range(len(outputs)):
        f.write(outputs[x] + '\n')
    # f.write('\n')
    tot = ''.join(summary)
    f.write(tot)
    f.close()


if __name__ == "__main__":
    print('\n')
    print(args)
    print('\n')
    # print(check_countries())
    # print(check_years())
    # print(ten_first_medals())
    if args.medals:
        if check_countries() == 'ok' and check_years() == 'ok':
            ten_first_medals()

    if args.total:
        if check_years() == 'ok':
            total_all_countries()

    if args.output:
        write_to_file()