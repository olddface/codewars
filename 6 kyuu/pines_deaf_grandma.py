def deaf_grandma(you):
    mother_fucker_deaf_grandma = []
    for word in you:
        if word == "BYE":
            mother_fucker_deaf_grandma.append("OK, BYE!")
            return mother_fucker_deaf_grandma
        else:
            no_lower_case = all(not ('a' <= letter <= 'z') for letter in word)
            if (no_lower_case):
                mother_fucker_deaf_grandma.append("NO, NOT SINCE 1938!")
            else:
                mother_fucker_deaf_grandma.append("HUH?! SPEAK UP, SONNY!")
    return mother_fucker_deaf_grandma

print(deaf_grandma(["hi grandma", "WHAT", "bye", "BYE"]))