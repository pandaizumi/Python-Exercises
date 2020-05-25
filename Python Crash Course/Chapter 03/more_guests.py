# Exercise 3.6

guests = ['jamie', 'hewitt', 'skye']

print(f"Hello {guests[0].title()}, you've been invited to dinner.")
print(f"Hello {guests[1].title()}, you've been invited to dinner.")
print(f"Hello {guests[2].title()}, you've been invited to dinner.")
print()

print(f"Oh no, it looks like {guests[0].title()} can't make it.")

guests[0] = 'terris'

print()
print(f"Hello {guests[0].title()}, you've been invited to dinner.")
print(f"Hello {guests[1].title()}, you've been invited to dinner.")
print(f"Hello {guests[2].title()}, you've been invited to dinner.")

print()

print("Hey, everyone it looks like I've found a bigger dinner table.")

guests.insert(0, 'kay')
guests.insert(2, 'alexi')
guests.append('shan')

print()
print(f"Hello {guests[0].title()}, you've been invited to dinner.")
print(f"Hello {guests[1].title()}, you've been invited to dinner.")
print(f"Hello {guests[2].title()}, you've been invited to dinner.")
print(f"Hello {guests[3].title()}, you've been invited to dinner.")
print(f"Hello {guests[4].title()}, you've been invited to dinner.")
print(f"Hello {guests[5].title()}, you've been invited to dinner.")
