formatter = "{} {} {} {}"

#format can take int as argument
print(formatter.format(1, 2, 3, 4))

#.format can take string as argument
print(formatter.format('one', 'two', 'three', 'four'))

#.format can take boolean as argument
print(formatter.format(True, False, True, False))

#.format can take variable as argument
print(formatter.format(formatter, formatter, formatter, formatter))

#.format can take line separated string as argument
print(formatter.format(
    "Radio Mrich",
    "Sunle wale",
    "Always",
    "Khus"
))