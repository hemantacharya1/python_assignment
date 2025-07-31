from collections import Counter
def analyze_friendships():
    """
    Analyze friendship patterns across different social media platforms """
    # User friends on different platforms
    facebook_friends = {"alice", "bob", "charlie", "diana", "eve", "frank"}
    instagram_friends = {"bob", "charlie", "grace", "henry", "alice", "ivan"}
    twitter_friends = {"alice", "diana", "grace", "jack", "bob", "karen"}
    linkedin_friends = {"charlie", "diana", "frank", "grace", "alice", "mary"}
    # Your tasks:
    # 1. Find friends who are on ALL four platforms
    # 2. Find friends who are ONLY on Facebook (not on any other platform)
    # 3. Find friends who are on Instagram OR Twitter but NOT on both
    # 4. Find the total unique friends across all platforms
    # 5. Find friends who are on exactly 2 platforms
    # Return a dictionary with all results
    result={}
    # 1. Friends on ALL four platforms
    result['all_platforms'] = facebook_friends & instagram_friends & twitter_friends & linkedin_friends

    # 2. Friends ONLY on Facebook
    result['facebook_only'] = facebook_friends - (instagram_friends | twitter_friends | linkedin_friends)

    # 3. Friends on Instagram OR Twitter but NOT both (symmetric difference)
    result['instagram_xor_twitter'] = instagram_friends ^ twitter_friends

    # 4. Total unique friends across all platforms
    result['total_unique'] = facebook_friends | instagram_friends | twitter_friends | linkedin_friends

    return result

    # Test your function
result = analyze_friendships()
print("All platforms:", result.get('all_platforms'))
print("Facebook only:", result.get('facebook_only'))
print("Instagram XOR Twitter:", result.get('instagram_xor_twitter'))
print("Total unique friends:", result.get('total_unique'))
