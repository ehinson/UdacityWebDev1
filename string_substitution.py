given_string = "I think %s is a perfectly normal thing to do in public."
given_string2 = "I think %s and %s are perfectly normal things to do in public."
given_string3 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."


def string_sub1(s):
    return given_string %s

# substitute multiple strings
def string_sub2(s1, s2):
    return given_string2 %(s1, s2)

# advanced substitution
def string_sub3(name, nickname):
    return given_string3 %{"name": name, "nickname": nickname}

print string_sub1("running")
# >>> "I think running is a perfectly normal thing to do in public."

print string_sub1("crying")
# >>> "I think crying is a perfectly normal thing to do in public."

print string_sub2("running", "sleeping")
#>>> "I think running and sleeping are perfectly normal things to do in public."

print string_sub2("sleeping", "running")
#>>> "I think sleeping and running are perfectly normal things to do in public."

print string_sub3("Erin", "Wednesday")
#>>> "I'm Wednesday. My real name is Erin, but my friends call me Wednesday."
