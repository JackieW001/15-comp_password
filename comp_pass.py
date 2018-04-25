def min_thresh(string):
    has_lower = [x for x in string if x.islower()]
    has_upper = [x for x in string if x.isupper()]
    has_num = [x for x in string if x.isdigit()]
    if (len(has_lower) > 0 and len(has_upper) > 0 and len(has_num) > 0):
        print "PASSWORD IS SECURE"
    else:
        print "PASSWORD IS NOT SECURE"

min_thresh("password")
min_thresh("Pa55w0rD")

def strength(string):
    has_lower = [x for x in string if x.islower()]
    has_upper = [x for x in string if x.isupper()]
    has_num = [x for x in string if x.isdigit()]
    s_char = {x for x in string if not x.isalnum()}

    char = [has_lower, has_upper, has_num, s_char]
    weights = [0.1,0.1,0.3,0.5]
    length = len(string)
    score = 0
    for i in range(len(char)):
        score += len(char[i])* weights[i]
    print "YOUR SCORE IS: ", score

strength("hehexd123")
strength("Pa55w0rD")
strength("Pa55w0rD!")
strength("!!!!@#$%^&*(()_!!adfweDWWEIOUTE109354780")
