
# [Lab] CS1P - Lab exam in practice

# [Lab] CS1P - Lab exam adjustments

# [Lecture] CS1F - Revision lecture - HCI 1

# [Lecture] CS1F - Revision lecture - HCI 2

# [Lecture] CS1P - Exam material - Introduction

# [Lecture] CS1P - Exam material - Advanced

# [Lecture] CS1F - Revision - SQL

# [Lecture] CS1F - Revision - Relational Algebra

# [Lecture] CS1P - Revision - Higher order functions

# [Lecture] CS1P - Revision - Algorithms

# [Revision] CS1F - Relational Algebra Quiz

# [Revision] CS1F - SQL Quiz

# [Revision] CS1F - IM Theoretical Material

# [Revision] CS1F - IM Practical Material

# [Revision] CS1F - HCI Research Material

# [Revision] CS1F - HCI User Interface Material

print([1, 2, 3][0:2])

def certify(s, certification="CERTIFIED"):
    return s + " " + certification

def combine(s):
    return "-".join(s)

def package(elts, pre="(", post=")"):
    return combine([pre+c+post for c in elts])

values = ["one", "two", "three"]
print(certify(package(values, "[", "]")))

def flatten(l):
    if type(l) == type([]):
        result = []
        for elt in l:
            result += flatten(elt)
        return result
    else:
        return [l]

print(flatten([[["a", "b"], "c", [["d"]]]]))
