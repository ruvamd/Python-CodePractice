import requests

#api call and store
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f'status code: {r.status_code}')

#store API response in a variable
response_dict=r.json()
print(f"total repo: {response_dict['total_count']}")

#explore
repo_dicts=response_dict['items']
print(f'repo returned: {len(repo_dicts)}')

#exam first repo
repo_dict=repo_dicts[0]

print('\nselected each repo')
for repo_dict in repo_dicts:
    print(f"name: {repo_dict['name']}")
    print(f"owner: {repo_dict['owner']['login']}")
    print(f"stars: {repo_dict['stargazers_count']}")
    print(f"repo: {repo_dict['html_url']}")
    print(f'\nkeys: {len(repo_dict)}')
    print(f"created: {repo_dict['created_at']}")
    print(f"description: {repo_dict['description']}")

# for key in sorted(repo_dict.keys()):
#     print(key)

print(response_dict.keys())
