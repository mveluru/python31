import re


def string_compare(str1, str2):
    pattern = re.compile(str1)
    match = re.search(pattern, str2)
    if match:
        print(f"{str1} found in {str2}")
    else:
        print(f"{str2} found in {str1}")


string_compare('HelloGuru', "HelloGuruReddy")

string_compare('MuralidharReddy', "Muralidhar")
