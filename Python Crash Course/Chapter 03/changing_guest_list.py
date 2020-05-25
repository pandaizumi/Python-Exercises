# Exercise 3.5

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
