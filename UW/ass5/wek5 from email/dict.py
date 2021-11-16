my_dict = {"Name": "Andy", "Job": "Tutor"}

assert list(my_dict.items()) == [("Name", "Andy"), ("Job", "Tutor")]

for key, value in my_dict.items():
    print(key, value)


people = [
    {"Name": "Andy", "Job": "Tutor"},
    {"Name": "Fred", "Job": "Analyst"},
    {"Name": "Pam", "Job": "Nurse"},
]

assert people[1]["Name"] == "Fred"


people = {
    '111-11-1111': {"Name": "Andy", "Job": "Tutor"},
    '222-22-2222': {"Name": "Fred", "Job": "Analyst"},
    '333-33-3333': {"Name": "Pam", "Job": "Nurse"},
}

assert people['222-22-2222'] == {"Name": "Fred", "Job": "Analyst"}
assert people['222-22-2222']['Name'] == "Fred"

# dictionary keys must be unique; show what happens when they are not
my_dict = {
    "Name": "Andy",
    "Job": "Tutor",
    "Job": "Analyst",
    "Preferred_name": "Andy",
}

assert my_dict == {"Name": "Andy", "Job": "Analyst", "Preferred_name": "Andy"}

my_new_dict = {}
for key, value in my_dict.items():
    my_new_dict[value] = key

assert my_new_dict == {"Andy": "Preferred_name", "Analyst": "Job"}
