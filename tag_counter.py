import praw
import csv
from collections import Counter
import datetime
import re
import os
from dotenv import load_dotenv

load_dotenv()


def get_year_from_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).year


def normalize_tag(tag):
    tag = tag.lower()
    tag_mapping = {
        "hypr": "hyprland/hypr",
        "hyprland": "hyprland/hypr",
        "plasma kde": "kde",
        "plasma": "kde",
    }

    prefixes = ["kde", "xfce", "i3", "herbstluft", "sway", "gnome", "awesome"]
    for prefix in prefixes:
        if tag.startswith(prefix):
            return prefix

    return tag_mapping.get(tag, tag)


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = "script by u/dybdeskarphet"
reddit = praw.Reddit(
    client_id=client_id, client_secret=client_secret, user_agent=user_agent
)
subreddit = reddit.subreddit("unixporn")
creation_date = datetime.datetime.fromtimestamp(subreddit.created_utc)
start_year = creation_date.year
tag_counts = Counter()
current_year = datetime.datetime.now().year

for year in range(start_year, current_year + 1):
    print(f"Fetching data for year: {year}")
    for post in subreddit.top(time_filter="year", limit=None):
        post_year = get_year_from_timestamp(post.created_utc)
        if post_year == year:
            tags = re.findall(r"\[([^\]]+)\]", post.title)
            for tag_group in tags:
                for tag in re.split(r"[+/,|]", tag_group):
                    tag = tag.strip()
                    if tag:
                        if tag.isdigit() or len(tag) == 1:
                            continue
                        normalized_tag = normalize_tag(tag)
                        tag_counts.update([normalized_tag])


with open("data/tag_counts.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Tag", "Count"])
    for tag, count in tag_counts.most_common():
        writer.writerow([tag, count])

print("CSV file created with tag counts.")
