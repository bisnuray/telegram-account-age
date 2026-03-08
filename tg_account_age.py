import json
from datetime import datetime, timedelta

with open("uid_ts.json", "r") as f:
    user_id_timestamps = json.load(f)

user_id_timestamps.sort()

def approximate_creation_date(user_id):
    user_id = int(user_id)

    if user_id <= user_id_timestamps[0][0]:
        return f"Before {datetime.utcfromtimestamp(user_id_timestamps[0][1]).strftime('%Y-%m-%d')}"

    if user_id >= user_id_timestamps[-1][0]:
        return f"After {datetime.utcfromtimestamp(user_id_timestamps[-1][1]).strftime('%Y-%m-%d')}"

    for i in range(1, len(user_id_timestamps)):
        prev_id, prev_time = user_id_timestamps[i - 1]
        next_id, next_time = user_id_timestamps[i]

        if prev_id <= user_id <= next_id:
            ratio = (user_id - prev_id) / (next_id - prev_id)
            estimated_time = int(prev_time + ratio * (next_time - prev_time))
            return f"Approximately {datetime.utcfromtimestamp(estimated_time).strftime('%Y-%m-%d')}"

    return "Unknown date"

def format_time_ago(timestamp):
    now = datetime.utcnow()
    dt = datetime.utcfromtimestamp(timestamp)
    delta = now - dt

    if delta < timedelta(minutes=1):
        return "just now"
    elif delta < timedelta(hours=1):
        return f"{delta.seconds // 60} minutes ago"
    elif delta < timedelta(days=1):
        return f"{delta.seconds // 3600} hours ago"
    elif delta < timedelta(days=7):
        return f"{delta.days} days ago"
    elif delta < timedelta(days=30):
        return f"{delta.days // 7} weeks ago"
    elif delta < timedelta(days=365):
        return f"{delta.days // 30} months ago"
    else:
        return f"{delta.days // 365} years ago"

user_input = input("Enter a User ID: ")
creation_date = approximate_creation_date(user_input)

print(f"Estimated Creation Date: {creation_date}")

if "Approximately" in creation_date or "After" in creation_date or "Before" in creation_date:
    date_str = creation_date.split()[-1]
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    unix_time = int(date_obj.timestamp())
    print(f"Time Ago: {format_time_ago(unix_time)}")
