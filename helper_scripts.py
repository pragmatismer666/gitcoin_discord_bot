import requests, json, time, datetime


def convert_to_date_time(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    hour = int(date[11:13])
    minute = int(date[14:16])
    second = int(date[17:19])
    dateTime = datetime.datetime(year, month, day, hour, minute, second)
    return dateTime


def string_bounty_data(data):
    url = data["url"]
    created_on = convert_to_date_time(data["created_on"])
    title = data["title"]
    level = data["experience_level"]
    expire_date = convert_to_date_time(data["expires_date"])
    reward = data["value_in_usdt"]
    bounty = f"***URL:*** {url}\n***Created:*** {created_on}\n***Title:*** {title}\n***Level:*** {level}\n***Expiration Date:*** {expire_date}\n***Bounty:*** {reward}"
    return bounty


def get_last_bounty():
    with open("last_bounty.json", "r") as outfile:
        last_bounty = json.load(outfile)
    return last_bounty


def get_bounties():
    response = requests.get(
        "https://gitcoin.co/api/v0.1/bounties?idx_status=open&applicants=ALL&order_by=-web3_created"
    )
    data = response.json()
    return data


def compare_bounties(bounty_list, last_bounty):
    latest_date = convert_to_date_time(last_bounty["created_on"])
    latestBounty = {}
    bounties = []
    for i in bounty_list:
        date = convert_to_date_time(i["created_on"])
        if date > latest_date:
            latestBounty = i
            bounties.append(i)
    if latestBounty:
        latestBounty = bounty_list[0]
        with open("last_bounty.json", "w") as outfile:
            json.dump(latestBounty, outfile)
    return bounties
