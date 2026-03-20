import re
import pandas as pd

def preprocess(file_data):
    pattern = r'^(\d{2}/\d{2}/\d{2}),\s(\d{1,2}:\d{2}\s*[ap]m)\s-\s(.+?):\s(.*)'
    data = []
    for line in file_data.split("\n"):
        print(line)
        line = line.strip()
        match = re.match(pattern, line)

        if match:
            date = match.group(1)
            time = match.group(2)
            user = match.group(3)
            message = match.group(4)

            datetime = date + " " + time

            data.append([datetime, user, message])
    print(data)
    df = pd.DataFrame(data, columns=["date","user","message"])
    df["date"] = pd.to_datetime(df["date"],format="%d/%m/%y %I:%M %p")

    df["only_date"] = df["date"].dt.date
    df["year"] = df["date"].dt.year
    df["month_num"] = df["date"].dt.month
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["minute"] = df["date"].dt.minute
    df['day_name'] = df['date'].dt.day_name()

    print(df)
    return df