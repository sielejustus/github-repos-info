import requests
from pprint import pprint 


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code:',r.status_code)

response_dict = r.json()
# pprint(response_dict)
print('------------------------------------------------')

print(f"Total repositories: {response_dict['total_count']}")
# pprint(response_dict
repo_dicts = response_dict['items']
print(f"repositories returned: {len(repo_dicts)}")
repo_dict = repo_dicts[0]
print(f"keys: {len(repo_dict)}" )


print(f"name: {repo_dict['name']}")
print(f"owner: {repo_dict['owner']['login']}")
print(f"stars: {repo_dict['stargazers_count']}")
print(f"repository: {repo_dict['html_url']}")
print(f"created: {repo_dict['created_at']}")
print(f"updated: {repo_dict['updated_at']}")
print(f"description: {repo_dict['description']}")

for repo_dict in repo_dicts:
	print(f"\nname: {repo_dict['name']}")
	print(f"owner: {repo_dict['owner']['login']}")
	print(f"stars: {repo_dict['stargazers_count']}")
	print(f"repository: {repo_dict['html_url']}")
	print(f"description: {repo_dict['description']}")