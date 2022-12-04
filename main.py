import csv

filename = "Bronie prototyp - PERK (1).csv"

class Perk:
    def __init__(self, row):
        self.ID = str(row[0])
        self.origin = str(row[1])
        self.name = str(row[2])
        self.requirements = str(row[3])
        self.effect = str(row[4])
        self.description = str(row[5])
        self.limitations = str(row[6])

    def __str__(self):
        return f"ID:{self.ID}, origin:{self.origin}, name:{self.name}, requirements:{self.requirements}, " \
               f"effect:{self.effect}, description:{self.description}, limitations:{self.limitations}"

def checkPerkNames(perks:list[Perk]):
    perk_ids = []
    for pk in perks:
        if pk.ID in perk_ids:
            print(f"Duplicate perk {pk.ID} definition!")
            continue
        perk_ids.append(pk.ID)
        name = pk.name.upper().replace("Ą", "A").replace("Ó", "O").replace("Ł", "L").replace("Ń", "N").\
            replace("Ś", "S").replace("Ę", "E").replace("Ż", "Z").replace("Ź", "Z").replace("Ć", "C").replace(".", "").\
            replace(",", "").replace("!", "").replace("/", "").replace("?", "").replace("'", "").replace("&", "").\
            replace("-", "").replace(" ", "").replace("(","").replace(")","").\
            replace("10", "DZIESIEC").replace("3", "TRZY").replace("2", "DWA").replace("1", "JEDEN")
        if pk.ID != "PERK_"+name:
            print(f"Out of rules ID field {pk.ID} vs {name}")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    perks = []
    with open(filename, encoding="utf8", newline='') as csvfile:
        perkReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for idx, row in enumerate(perkReader):
            if idx == 0:
                # skip header row
                continue
            if str(row[0]) == str(row[1]) == str(row[2]) == str(row[3]) == "":
                # empty row
                continue
            perk = Perk(row)
            perks.append(perk)
    checkPerkNames(perks)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
