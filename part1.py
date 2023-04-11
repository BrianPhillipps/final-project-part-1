import json
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import requests
from utilities import file


url = "https://tf.tfrrs.org/lists/3711/2022_NCAA_Division_I_Outdoor_Qualifying_FINAL?gender=m"

print(url)

print()

res = requests.get(url)
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]


data = pd.read_csv("data/final project part 1.csv") 

#removing the unnamed column
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

print("All data")
print()
print(data)
print()

print("My first thought was how many athletes of each year were in the top 100. To do this, I filtered the data to find each year. I chose to do it this was instead of aggregating by category because I can show the filtered data instead of just the total")
print()

filtered_freshman = data[data["Year"]=="FR-1"]
print("Number of freshman in the top 100: " ^^^ str(len(filtered_freshman)))
print()
print(filtered_freshman)
print()

filtered_sophomore = data[data["Year"]=="SO-2"]
print("Number of sophomores in the top 100: " ^^^ str(len(filtered_sophomore)))
print()
print(filtered_sophomore)
print()

filtered_junior = data[data["Year"]=="JR-3"]
print("Number of juniors in the top 100: " ^^^ str(len(filtered_junior)))
print()
print(filtered_junior)
print()

filtered_senior = data[data["Year"]=="SR-4"]
print("Number of seniors in the top 100: " ^^^ str(len(filtered_senior)))
print()
print(filtered_senior)
print()



print("Next, I wanted to know the average time ran in 2021-2022. Normally, this is pretty easy. In my case, some of the values had an '@' next to them which means the time was converted due to altitude. Pandas reads this @ as part of a string. Here, I removed the @ from all the times that had it by doing this: ")
print("data.Time= data.Time.str.replace('[#,@,&amp;]', '')")
print()
print("This was the data before it was cleaned")
print(data['Time'])

print()
data.Time= data.Time.str.replace('[#,@,&amp;]', '')
print("This was the data after")
print(data['Time'])

print()

print("Then I converted the times from a string to a float so the mean could be calculated.")
print()
print("Data type of time before conversion: ")


print(data.Time.dtypes)
data["Time"] = pd.to_numeric(data["Time"], downcast="float")
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
print()
print("Data type of time after conversion: ")
print(data.Time.dtypes)
print()

print("This allowed for me to calculate the average time")
avg_time = data["Time"].mean().round(2)
print("The average time in the 100m dash from 2021-2022 outdoors is (rounded to the nearest hundreth): " ^^^ str(avg_time))
print()

print("Next, I wanted to know the average times by year compared to each other rounded to 3 digits because there was a 3 way tie.")
year_times= data[["Time", "Year"]].groupby("Year").mean().round(3)
print(year_times)
print()


print("Then I converted the average wind for each of the listings which was a lot easier...")

avg_wind = data["Wind"].mean().round(2)
avg_mph = round(2.237 * avg_wind,2)

print("The average wind in 100 races is: " ^^^ str(avg_wind) ^^^ " meters per second or " ^^^ str(avg_mph) ^^^ " miles per hour.")
print()
print("Then I wanted to know which teams had the most athletes in the top 100. Here, I counted the team values and showed the top 5 teams with the most athletes listed")

team_count = data['Team'].value_counts().nlargest(5)
print(team_count)
print()

print("I did the same thing for the meets listed. Here are the meets where the most athletes hit their best time")

meet_count = data['Meet'].value_counts().nlargest(5)
print(meet_count)
print()

print("Here are the 5 meets with the lowest average times: ")
avg_meet_times = data.groupby(by='Meet').Time.mean().round(2).nlargest(5)
print(avg_meet_times)
print("*Note: this technically does not mean that this meet had the fastest athletes time here. The number of athletes running has a big factor in play")
print()
print("Next I wanted to know all the unique meets there. Pandas gives us an easy function to use")
print()

unique_meet = data.Meet.unique()
print(unique_meet)




