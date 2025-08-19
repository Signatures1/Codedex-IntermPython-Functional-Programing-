import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(suffix):
    return suffix.capitalize()

capitalized_suffixes = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [
    create_fantasy_name(prefixes, capitalized_suffixes) 
    for _ in range(10)
]

def fire_in_name(name):
    return 'fire' in name.lower()

def concatenate_names(name1, name2):
    return name1 + ' ' + name2

fire_usernames = list(filter(fire_in_name, random_names))
usernames = reduce(concatenate_names, random_names, '')

def display_name_info():
    print("Random Usernames:")
    for name in random_names:
        print(" -", name)
    print("\nUsernames containing 'fire':")
    for name in fire_usernames:
        print(" -", name)
    print("\nAll Usernames Combined:")
    print(usernames)

display_name_info()