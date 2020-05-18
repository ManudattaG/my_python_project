"""
Working with Python Data Structures
"""

# Merge 2 dictionaries

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
z = {**x, **y}
print(z)

# Print the matrix

iterator = [i for i in range(1, 4)]
matrix = [[x * y for y in iterator] for x in iterator]
print(matrix)

# Occurrence of each element in a list

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
occ_list = [[x,weekdays.count(x)] for x in set(weekdays)]
print(occ_list)

# To find common letters in two strings

common_str = list(set("hello") & set("how"))
print(common_str)

# Parsing a payload

payload = {
	"ListOfServers":{
		"ServerDetails":[
			{
				"HostId":"111111111111",
				"HostName":"Serverfirst",
				"ServerCodes":None,
				"ServerSeatCount":"None"
			},
			{
				"HostId":"222222222222",
				"HostName":"Serversecond",
				"ServerCodes":None,
				"ServerSeatCount":"None"
			},
			{
				"HostId":"333333333333",
				"HostName":"Serverthird",
				"ServerCodes":None,
				"ServerSeatCount":"None"
			}
		]
	}
}

hostname_list = payload["ListOfServers"]["ServerDetails"]
for hostname in hostname_list:
	print(hostname)
	
# Generators

my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
print(next(a))

print(next(a))

print(next(a))

print(next(a))


# Getting data from the dictionary

api_response = 
{
    "ok": true,
    "user": {
        "id": "ABCD1234",
        "team_id": "T02NW42JD",
        "deleted": false,
        "color": "5b89d5",
        "tz": "Los Angeles/US",
        "tz_label": "Pacific Daylight Time(PST)",
        "tz_offset": 19800,
        "profile": {
            "title": "Sr. Manager",
			"username": "John Hopkin"
		}
	}
}

username = api_response["user"]["profile"]["username"]
print(username)
