# Mini project for using API calls to get data from online sources and use it



# 01/09/2026

# import relevant modules

# library used for making API calls, will be calling from the GitHub API
import requests


# getting data from a URL.
# The python program is requesting to see the data

#1 params used as extra instructions on how to present the requested data
#get_data = requests.get("https://api.github.com/users/octocat/repos", params= {"login": "octocat"})


# prints the JSON data from the request.
# print(get_data.text)

# covert the JSON response into a Python object (dictionary)
#user_data = get_data.json()

# TASK: print octocats's user name, number of public repositories, number of followers

#print("name:" , user_data["name"] , "\npublic repositories:" 
#     , user_data["public_repos"] , "\nNum of followers:" , user_data["followers"] )

# to get the status code 
# (essentially the response based on whether the data was recieved or not in numerical values)

# print(get_data.status_code)

# check if the status code is 200 (sucessfully recieved the request)
#if get_data.status_code == 200:
    # process the data
#    print("Request was sucessfull")
#    print(get_data.url)
#    processed_user_data = get_data.json()

#else:
#    print("Request was unsucessfull")

# 1) adapting get method to accept parameters that modify request (DONE)
# print(processed_user_data)



############################################################################### 03/09/2026 ####################################################################################

# 2) Find the GitHub API endpoint that
#  means: "List the repositories belonging to this user:"

# send a get request to the repos URL data

# get the JSON data related to octocats repos 
get_repos = requests.get("https://api.github.com/users/octocat/repos")


# check if the data was sucessfully stored
if get_repos.status_code == 200:
    print("Request was sucessfull\n")
    # convert to a dictionary format
    # NOTE: because octocat has multiple repositories, there are now a list of dictionaries 
    # rather than one in the previous example 
    repos_data = get_repos.json()
else:
    print("Request was unsucessfull\n")


# 3) Processing the data: Print the name of every repository
# 4) Print the name, programming language, number of stars

# loop through the list of dictionaries

print("List of repositories:\n")
for repos in repos_data:
    # print the name, pl and stars
    print(repos["name"], "\nProgramming language: ", repos["language"] , "\nStars: ", repos["stargazers_count"], "\n")

print("#############################################################################################")


# 5) printing repositories that are not "none"
# NOTE: JSON "null" -> when converted to python is None not "None"  <--- IMPORTANT


for rep_valid in repos_data:
    if rep_valid["language"] is not None:
        print(rep_valid["name"], "\nProgramming language: ", rep_valid["language"] , "\nStars: ", rep_valid["stargazers_count"], "\n")


print("#############################################################################################")


# 6) Summarise the repositories data
# a) Count how mant repositories use each programming language
# b) FInd the repository with the most stars
# c) Calculate the total number of stars across all repositories


# a)
# create a language dictionary

pl_dict = {}

for repo in repos_data:
    # check if the language is valid
    if repo["language"] is not None:

    # check if the current repos language is in the dict
        if repo["language"] in pl_dict :
            # incrememnt the entry
            pl_dict[repo["language"]] +=1
        else:
            # add the language entry to the dictionary
            pl_dict[repo["language"]] = 1

print("How many repositories use each language: ", pl_dict)

print("#############################################################################################")


# b)

# inital highest stars

highest_stars = 0
repo_highest = ""

# loop through the repositories
for repo in repos_data:
    if repo["stargazers_count"] > highest_stars:
        highest_stars = repo["stargazers_count"]
        repo_highest = repo["name"]

print(f'Repo {repo_highest} has the highest stars of: {highest_stars}')

print("#############################################################################################")

# C

total_stars = 0

# loop through all repos 
for repo in repos_data:
    total_stars += repo["stargazers_count"]

print(f'Total stars: {total_stars}')
    















