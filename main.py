import requests

TOKEN = '2619421814940190'


def get_thanos_info():
    url = 'https://superheroapi.com/api/2619421814940190/search/thanos'
    response = requests.get(url, timeout=5)
    return response.json()


def get_hulk_info():
    url = 'https://superheroapi.com/api/2619421814940190/search/hulk'
    response = requests.get(url, timeout=5)
    return response.json()


def get_cap_info():
    url = 'https://superheroapi.com/api/2619421814940190/search/captain%20america'
    response = requests.get(url, timeout=5)
    return response.json()


def get_id():
    id_list = []
    thanos_data = get_thanos_info()
    hulk_data = get_hulk_info()
    cap_data = get_cap_info()
    thanos_id = thanos_data['results'][0]['id']
    hulk_id = hulk_data['results'][0]['id']
    cap_id = cap_data['results'][0]['id']
    id_list.append(thanos_id)
    id_list.append(hulk_id)
    id_list.append(cap_id)
    return id_list


def get_int():
    stats = get_id()
    int_list = []
    for hero_id in stats:
        url = f'https://superheroapi.com/api/2619421814940190/{hero_id}/powerstats'
        response = requests.get(url, timeout=5)
        res = response.json()['intelligence']
        int_list.append(res)
    return int_list


def max_int():
    stats = {}
    keys = get_id()
    values = get_int()
    for x in range(len(keys)):
        stats[keys[x]] = values[x]
    highest_int = 1
    max_id = int
    for x in stats:
        if int(stats[x]) > highest_int:
            highest_int = int(stats[x])
            max_id = x
    return max_id


def get_result():
    winner_id = max_int()
    url = f'https://superheroapi.com/api/2619421814940190/{winner_id}'
    response = requests.get(url, timeout=5)
    winner = response.json()['name']
    res = f'{winner} is the most intelligent'
    return res


print(get_result())
