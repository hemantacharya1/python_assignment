from collections import Counter
from collections import defaultdict
posts=[{"id":1,"user":"alice","content":"Love Programing","likes":15,"tags":["python","coding"]},
       {"id":2,"user":"bob","content":"Great Weather Today","likes":8,"tags":["weather","life"]},
       {"id":3,"user":"alice","content":"data structures and fun","likes":32,"tags":["python","learning"]},
]
users={
    "alice":{"followers":150,"following":75},
    "bob":{"followers":89,"following":120}
}

all_tags=[]

user_likes = defaultdict(int)

def most_popular_tags():
    for i in posts:
        all_tags.extend(i['tags'])
    print(Counter(all_tags))

def user_engagement():
    for pt in posts:
        user=pt["user"]
        likes=pt["likes"]
        user_likes[user]+=likes
    print(dict(user_likes))

def top_posts():
    sorted_list=sorted(posts,key=lambda posts:posts["likes"],reverse=True)
    print(sorted_list[0])

def user_activity():
    activity = defaultdict(lambda: {"posts": 0, "likes": 0})
    for post in posts:
        user = post["user"]
        activity[user]["posts"] += 1
        activity[user]["likes"] += post["likes"]
    print(dict(activity))

most_popular_tags()
user_engagement()
top_posts()
user_activity()