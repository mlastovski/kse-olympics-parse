import csv

with open('athlete_events.csv') as csvfile:
    # create a list to store results
    result = []

    # read the file
    reader = csv.reader(csvfile)

    # for every line in the csv
    for row in reader:

        #create a user dict
        article = {}

        # fill in the user.
        article["id"] = row[0]
        article["name"] = row[1]
        article["country"] = row[6]
        article["country_short"] = row[7]
        article["year"] = row[9]
        article["game"] = row[12]
        article["medal"] = row[14]
        

        # add this user to the list of users
        result.append(article)

print(result)


# file = open(path, 'r')
# next_line = file.readline()
# # print(next_line)

# result = []

# while next_line:
#     next_line = file.readline()
#     next_line = next_line.replace('"', '')
#     next_line = next_line.replace('\n', '')
#     next_line = next_line.split(',')
#     # print(next_line)
#     # result.append(next_line)
#     try:
#         id = next_line[0]
#         name = next_line[1]
#         country = next_line[6]
#         country_short = next_line[7]
#         year = next_line[9]
#         game = next_line[12]
#         medal = next_line[14]

#         if id and name and country and country_short and year and game and medal:
#             article = {
#                 'id': id,
#                 'name': name,
#                 'country': country,
#                 'country_short': country_short,
#                 'year': year,
#                 'game': game,
#                 'medal': medal
#             }
#             result.append(article)

#     except IndexError:
#         break

# print('\n' + '\n' + '\n' + '\n' + '\n')
# print(result)