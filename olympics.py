# import libraries
import csv
import argparse

# add console arguments to program
parser = argparse.ArgumentParser(description='Process some data.')
parser.add_argument('path', metavar='PATH', type=str, help='Path to the file')
group = parser.add_mutually_exclusive_group()
group.add_argument('-medals', metavar='COUNTRY', type=str, nargs='*', required=False, help='Enter country')
group.add_argument('-total', metavar='YEAR', nargs='?', type=int, help='Specify year to display total quantity of medals')
parser.add_argument('-year', type=int, required=False, help='Specify year')
parser.add_argument('-output', metavar='PATH_TO_FILE', nargs='?', required=False, type=str, help='Enter name of the .txt file to write output to')
group.add_argument('-overall', type=str, required=False, nargs='+', help='Enter countries to get the highest medals count')

args = parser.parse_args()

path = str(args.path)
if args.medals:
    country_input = args.medals
    year_input = str(args.year)

    if args.year == None:
        print('Please specify a year')
        exit()

    # for correct reading of countries that contain 2 or more words in their name
    if len(country_input) > 1:
        country_input = ' '.join(country_input)
    else:
        country_input = ''.join(country_input)

if args.total:
    year_input = str(args.total)

    if args.year:
        print('You are not allowed to use "-year" along with "-total".')
        exit()

if args.overall:
    country_input = args.overall
    separate_country = country_input[0].split(', ')
    country_input = separate_country

    if args.year:
        print('You are not allowed to use "-year" along with "-overall".')
        exit()

# convert data from csv file to dict using only necessary keys and values
with open(path) as csvfile:
    result = []
    reader = csv.reader(csvfile)

    for row in reader:
        article = {
            'name': row[1],
            'country': row[6],
            'country_short': row[7],
            'year': row[9],
            'game': row[12],
            'medal': row[14],
        }
        result.append(article)

formatted_list = []

# if action is medals - select positions of given country and year that have medals 
if args.medals:
    for d in result:
        if year_input in d.values() and country_input in d.values():
            if d['medal'] != 'NA':
                formatted_list.append(d)

# # if action is total - select positions of given year that have medals 
if args.total:
    for d in result:
        if year_input in d.values():
            if d['medal'] != 'NA':
                formatted_list.append(d)


def check_years():
    check_year = []
    for years in result:
        if bool(year_input in years.values()) == False or int(year_input) < 1896:
            check = 0
        else:
            check = 1
        check_year.append(check)

    if 1 not in check_year:
        answer = 'This year the Olympiad was not held.'
        print(answer)
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


final_list = []
def total_all_countries():
    countries_and_medals = []
    for e in formatted_list:
        match = e['country_short'] + ' - ' + e['medal']
        countries_and_medals.append(match)
    
    set_medals = set(countries_and_medals)
    set_medals = list(set_medals)

    results = []
    for item in set_medals:
        quantity = countries_and_medals.count(item)
        name_of_country = str(item)
        formatted_item = name_of_country + ' : ' + str(quantity)
        results.append(formatted_item)

    results = sorted(results)
    print('\n' + '\n')


    for i, element in enumerate(results):
        shortened_name = element.split(' - ')[0]
        which_medal = element.split(' - ')[1]

        if i < len(results)-1:
            next_element = results[i+1]
        else:
            None

        if i < len(results)-2:
            next_next_element = results[i+2]
        else:
            None


        if shortened_name in element and element.split(' - ')[0] in next_element and next_element.split(' - ')[0] in next_next_element:
            output = shortened_name + ' ||||| ' + next_element.split(' - ')[1] + ' / ' + next_next_element.split(' - ')[1] + ' / ' + which_medal + '\n' + '---------------------------------------------------'
            del results[:2]
            final_list.append(output)
            continue
        
        if shortened_name in element and element.split(' - ')[0] in next_element:
            output = shortened_name + ' ||||| ' + next_element.split(' - ')[1] + ' / ' + which_medal + '\n' + '---------------------------------------------------'
            del results[:1]
            final_list.append(output)
            continue

        else:
            output = shortened_name + ' ||||| ' + which_medal + '\n' + '---------------------------------------------------'
            final_list.append(output)
            continue
    
    for el in final_list:
        print(el)


overall_list = []
def overall_countries():
    print('---------------------------------------------------')
    overall_list.append('---------------------------------------------------')
    for country in country_input:
        try:
            for d in result:
                if country in d.values():
                    if d['medal'] == 'Bronze' or d['medal'] == 'Silver' or d['medal'] == 'Gold':
                        formatted_list.append(d)

            for i in formatted_list:
                i['count'] = sum([1 for j in formatted_list if j['year'] == i['year'] and j['country'] == i['country']])

            max_value = max(item['count'] for item in formatted_list)
            
            for e in formatted_list:
                if e['count'] == max_value:
                    max_year = e['year']
            
            response = '||||| ' + country + " in " + str(max_year) + ': ' + str(max_value) + ' medals.' + '\n' + '---------------------------------------------------'
            formatted_list.clear()
            overall_list.append(response)
            print(response)

        except ValueError:
            response = " \nThere is no " + country + ' in database, please check if you have entered name properly\n'
            overall_list.append(response)
            print(response)


def write_to_file():
    file_name = str(args.output)
    f = open(file_name, 'w')

    if args.medals:
        for x in range(len(outputs)):
            f.write(outputs[x] + '\n')
        tot = ''.join(summary)
        f.write(tot)
    
    elif args.total:
        for x in range(len(final_list)):
            f.write(final_list[x] + '\n') 

    elif args.overall:
        for x in range(len(overall_list)):
            f.write(overall_list[x] + '\n')

    f.close()


if __name__ == "__main__":
    if args.medals:
        if check_countries() == 'ok' and check_years() == 'ok':
            ten_first_medals()

    if args.total:
        if check_years() == 'ok':
            total_all_countries()

    if args.overall:
        overall_countries()

    if args.output:
        write_to_file()
