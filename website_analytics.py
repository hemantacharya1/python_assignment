monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user2"}

def unique_visitors():
    s1 = set()
    fill_set(s1,monday_visitors)
    fill_set(s1,tuesday_visitors)
    fill_set(s1,wednesday_visitors)
    print(f'The toal number of unique visitor is {len(s1)} and the users are: {s1}')

def fill_set(s1,set2):
    for s in set2:
        s1.add(s)

def returning_visitor():
    print(monday_visitors.intersection(tuesday_visitors))

def new_user():
    print(f"Monday:{monday_visitors}, Tuesday:{tuesday_visitors.difference(monday_visitors)}, Wednesday:{wednesday_visitors.difference(tuesday_visitors,monday_visitors)}")

def loyal_customer():
    print(f"Loyal customer:{monday_visitors.intersection(tuesday_visitors,wednesday_visitors)}")


unique_visitors()
returning_visitor()
new_user()
loyal_customer()
    
