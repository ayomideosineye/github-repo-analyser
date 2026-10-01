# modular version of API calls for GitHub Repos

# import relevant modules

# library used for making API calls, will be calling from the GitHub API
import requests

# function to get the repository username
def get_username():
    username = input("Enter the username to get their repos: ")
    return username



# function that gets the API request and returns the repositories
def get_repositories(username: str):

    # implementing pagination: A way of dividing huge chunks of data into pages for more 
    # efficient data retrieval via API calls

    # 'page=' identifies the current page the data is being retrieved from
    base_url = f"https://api.github.com/users/{username}/repos"

    # stores all the repos for all the pages given the user
    all_repos = []

    # initial page num
    count = 1
  
    # instansiate a variable that determines if there are still more pages
    more_pages = True 

    while(more_pages):

         # trys to request the current page
        try:
            # per_page further splits the data into chunks but each call is 3 repos NOTE: NOT JUST TOP: 3 (when per_page : 3)
            # A lower per_page value means more API requests are needed to retrieve the same amount of data.
            # For example, per_page=3 with hundreds of repositories could use many requests and potentially
            # exhaust the API rate limit.
            
            current_page = requests.get(base_url, params={"page": count, "per_page": 100 })
            # raises an error if the status code is not between 200-299
            current_page.raise_for_status()
            # if the inital request doesnt work return an exception
        except requests.RequestException as e:
            print("The request was unsucessful")
            # terminates a running Python script and exits the interpreter
            raise SystemExit(e)
        else:
            # list of repos for current page
            current_page_repos = current_page.json()

            # check if the current_page is empty
            if len(current_page_repos) == 0:
                more_pages = False
            else:
            # loops through each repo in the current pages repo list
                for repo in current_page_repos:
                    # adds each repo for that given page to the all_repos list
                    all_repos.append(repo)

                print(f"Request was successful")
                # increment to the next current page
                count+=1
    
    return all_repos

# function that loads valid repository data for a username 
def load_data():

    # requested data is initially False
    requested_data = False

    # loops while the requested data is invalid
    while requested_data is False:
        username = get_username()
        requested_data = get_repositories(username)
    
    return username, requested_data


# returns the number of repos given the user repos API request
def total_repos(repos_data):
    return(len(repos_data))


# function that returns the languages used and their count, within the users repositories
def languages_count(repos_data):

    # languages dict
    lang_dict = {}

    if len(repos_data) == 0:
        return "N/A"

    for repo in repos_data:
        # check if the language used given the repo is not "null"
        if repo["language"] is not None:

            # check if the entry exists in the dictionary already
            if repo["language"] in lang_dict:
                lang_dict[repo["language"]] +=1
            else:
            # create the language entry
                lang_dict[repo["language"]] = 1

    return lang_dict


# returns the repository name and its star count.
def highest_stars(repos_data):
    current_highest = 0
    repo_name = ""

    if len(repos_data) == 0:
        return "N/A"

    # loop through each repo in the repos_list
    for repo in repos_data:
        # check if the current repos stars > current_highest
        if repo["stargazers_count"] > current_highest:
            current_highest = repo["stargazers_count"]
            repo_name = repo["name"]

    return (repo_name, current_highest)


def display_repos(repos_data):

    # loop through the repos and post them 
    for repo in repos_data:
        print(repo["name"])
    

# get the total starts given a user 
def total_stars(repos_data):

    # initialise inital total stars
    total_stars = 0

    # loop through each repo belonging to the user 
    # and add each repos stars together
    for repo in repos_data:
        total_stars += repo["stargazers_count"]

    return total_stars


def average_stars(repos_data):

    # check if the user actually has repositories
    if len(repos_data) == 0:
        return "N/A"

    # get the total stars given the user
    user_stars = total_stars(repos_data)
 
    # get the average stars per repo
    average  = user_stars / len(repos_data)

    return average


# start the inital program, getting the username and repo_data
username, repos_data = load_data()

display_repos(repos_data)



# get the languages used by the user given their repos
language_count = languages_count(repos_data)
print(f"languages used and count for user '{username}' : ",language_count, '\n')

# get the repository with the highest star count
highest_star_repo = highest_stars(repos_data)
print("Repo with the highest stars:", highest_star_repo, '\n')

# get the total stars the user has 
total = total_stars(repos_data)
print(f"{username}'s has a total of {total} stars", '\n')

# get the average stars 
average = average_stars(repos_data)
print(f"{username}'s average stars per repo is {average}")



