#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    if what.isupper():
        reply = 'Whoa, chill out!'
    elif what.isspace() or what is '':
        reply = 'Fine. Be that way!'
    elif what.strip()[-1] is '?':
        reply = 'Sure.'
    else:
        reply = 'Whatever.'
    return reply
