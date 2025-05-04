def generate_hashtag(s):
    s = s.split()
    print(len(s) != 0)
    jon = "#"
    for i in s:
        jon += i.title()
    print(len(jon))
    return jon if len(jon) > 0 and len(jon) < 140 and len(s) != 0 else False

print(generate_hashtag(""))