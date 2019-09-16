# function for adding single digits
def written(string0):
    singles = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
               "8": "Eight", "9": "Nine"}
    if string0 in list(singles.keys()):
        return singles[string0]


# funtions for adding teens
def teens(string0):
    teenage = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen",
               "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}
    if string0 in list(teenage.keys()):
        return teenage[string0]


# function for adding tens
def tens(string0):
    ten = {"2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty",
           "9": "Ninety"}
    if string0 in list(ten.keys()):
        return ten[string0]


# function for adding hundreds
def hundreds(string0):
    if string0[0] == "0":
        string0.remove(string0[0])
        nonesave = ""
        return nonesave
    elif string0[1] == "0" and string0[2] == "0":
        hunsave = written(string0[0]) + " " + "Hundred"
        string0.remove(string0[0])
        string0.remove(string0[0])
        return hunsave
    else:
        hunsave = written(string0[0]) + " " + "Hundred" + " " + "and"
        string0.remove(string0[0])
        return hunsave


# function for adding
def doubles(string0):
    if string0[0] == "0":
        number.remove(string0[0])
        nonesave = ""
        return nonesave
    elif string0[0] == "1":
        joint = "".join(string0[0:2])
        doublesave = teens(joint)
        if len(string0) == 5:
            doublesave = teens(joint) + " " + "Thousand"
        elif len(string0) == 8:
            doublesave = teens(joint) + " " + "Million"
        elif len(string0) == 11:
            doublesave = teens(joint) + " " + "Billion"
        string0.remove(string0[0])
        string0.remove(string0[0])
        return doublesave
    else:
        doublesave = tens(string0[0])
        string0.remove(string0[0])
        return doublesave


def add(string0, string1):
    if string0[0] == "0":
        string0.remove(string0[0])
    else:
        addsave = written(string0[0]) + " " + string1
        string0.remove(string0[0])
        return addsave


def spec(string0):
    specials = {"100000": "One Hundred Thousand", "1000000": "One Million", "100000000": "One Hundred Million",
                "10000000": "Ten Million", "1000000000000": "One Trillion"}
    new = "".join(string0)
    if new in list(specials.keys()):
        done = specials[new]
        return done
    else:
        return False
