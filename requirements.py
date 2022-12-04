from enum import Enum, unique


@unique
class REQUIREMENT_TYPE(Enum):
    WSPOLCZYNNIK = 1
    UMIEJETNOSC = 2
    PLEC = 3
    ZAWOD = 4
    POCHODZENIE = 5
    PROFESJA = 6
    SELECT = 7
    UNKNOWN = 8


@unique
class WSPOLCZYNNIK(Enum):
    ZRECZNOSC = "zręczność"
    PERCEPCJA = "percepcja"
    CHARAKTER = "charakter"
    SPRYT = "spryt"
    BUDOWA = "budowa"

@unique
class UMIEJETNOSC(Enum):
    BIJATYKA = "bijatyka"
    BRON_RECZNA = "broń ręczna"
    RZUCANIE = "rzucanie"

    PISTOLETY = "pistolety"
    KARABINY = "karabiny"
    BRON_MASZYNOWA="broń maszynowa"

    LUK="łuk"
    KUSZA="kusza"
    PROCA="proca"

    SAMOCHOD="samochód"
    CIEZAROWKA="ciężarowka"
    MOTOCYKL="motocykl"

    KRADZIEZ_KIESZONKOWA="kradzież kieszonkowa"
    ZWINNE_DLONIE="zwinne dłonie"
    OTWIERANIE_ZAMKOW="otwieranie zamków"

    WYCZUCIE_KIERUNKU="wyczucie kierunku"
    TROPIENIE="tropienie"
    PRZYGOTOWYWANIE_PULAPKI="przygotowanie pułapki",

    NASLUCHIWANIE="nasłuchiwanie"
    WYPATRYWANIE="wypatrywanie"
    CZUJNOSC="czujność"

    SKRADANIE_SIE="skradanie się"
    UKRYWANIE_SIE="ukrywanie się"
    MASKOWANIE="maskowanie"

    LOWIECTWO="łowiectwo"
    ZDOBYWANIE_WODY="zdobywanie wody"
    ZNAJOMOSC_TERENU="znajomość terenu"

    PERSWAZJA="perswazja"
    ZASTRASZANIE="zastraszanie"
    ZDOLNOSCI_PRZYWODCZE="zdolności przywódcze"

    POSTRZEGANIE_EMOCJI="postrzeganie emocji"
    BLEF="blef"
    OPIEKA_NAD_ZWIERZETAMI="opieka nad zwierzętami"

    ODPORNOSC_NA_BOL="odporność na ból"
    NIEZLOMNOSC="niezłomność"
    MORALE="morale"

    LECZENIE_RAN="leczenie ran"
    LECZENIE_CHOROB="leczenie chorób"
    PIERWSZA_POMOC="pierwsza pomoc"

    MECHANIKA="mechanika"
    ELEKTRONIKA="elektronika"
    KOMPUTERY="komputery"

    MASZYNY_CIEZKIE="maszyny ciężkie"
    WOZY_BOJOWE="wozy bojowe"
    KUTRY="kutry"

    RUSZNIKARSTWO="rusznikarstwo"
    WYRZUTNIE="wyrzutnie"
    MATERIALY_WYBUCHOWE="materiały wybuchowe"

    PLYWANIE="pływanie"
    WSPINACZKA="wspinaczka"
    KONDYCJA="kondycja"

    JAZDA_KONNA="jazda konna"
    POWOZENIE="powożenie"
    UJEZDZANIE="ujeżdżanie"


class UMIEJETNOSC_GROUP(Enum):
    WALKA_WRECZ = "walka wręcz"
    BRON_STRZELECKA = "broń strzelecka"
    BRON_DYSTANSOWA = "broń dystansowa"
    PROWADZENIE_POJAZDOW = "prowadzenie pojazdów"
    ZDOLNOSCI_MANUALNE = "zdolności manualne"
    ORIENTACJA_W_TERENIE = "orientacja w terenie"
    SPOSTRZEGAWCZOSC = "spostrzegawczość"
    KAMUFLAZ = "kamuflaż"
    PRZETRWANIE = "przetrwanie"
    NEGOCJACJE = "negocjacje"
    EMPATIA = "empatia"
    SILA_WOLI = "siła woli"
    MEDYCYNA = "medycyna"
    TECHNIKA = "technika"
    SPRZET = "sprzęt"
    PIROTECHNIKA = "pirotechnika"
    SPRAWNOSC = "sprawność"
    JEZDZIECTWO = "jeździectwo"


class PROFESSION(Enum):
    CHEMIK = "chemik"
    GANGER = "ganger"
    GLADIATOR = "gladiator"
    HANDLARZ = "handlarz"
    KAZNODZIEJA_NOWEJ_ERY = "kaznodzieja nowej ery"
    KOWBOJ = "kowboj"
    KURIER = "kurier"
    LOWCA = "lowca"
    LOWCA_MUTANTOW = "łowca mutantów"
    MAFIOZO = "mafiozo"
    MEDYK = "medyk"
    MONTER = "monter"
    NAJEMNIK = "najemnik"
    OCHRONIARZ = "ochroniarz"
    SEDZIA = "sedzia"
    SPEC = "spec"
    SZAMAN = "szaman"
    SZCZUR = "szczur"
    TRESER_BESTII = "treser bestii"
    TROPICIEL = "tropiciel"
    WOJOWNIK_AUTOSTRADY = "wojownik autostrady"
    ZABOJCA_MASZYN = "zabójca maszyn"
    ZABOJCA = "zabójca"
    ZLODZIEJ = "złodziej"
    ZOLNIERZ = "żołnierz"






skillnames = [
    "bijatyka", "broń ręczna", "rzucanie",
    "pistolety", "karabiny", "broń maszynowa",
    "łuk", "kusza", "proca",
    "samochód", "ciężarowka", "motocykl",
    "kradzież kieszonkowa", "zwinne dłonie", "otwieranie zamków",

    "wyczucie kierunku", "tropienie", "przygotowanie pułapki",
    "nasłuchiwanie", "wypatrywanie", "czujność",
    "skradanie się", "ukrywanie się", "maskowanie",
    "łowiectwo", "zdobywanie wody", "znajomość terenu",

    "perswazja", "zastraszanie", "zdolności przywódcze",
    "postrzeganie emocji", "blef", "opieka nad zwierzętami",
    "odporność na ból", "niezłomność", "morale",

    "leczenie ran", "leczenie chorób", "pierwsza pomoc",
    "mechanika", "elektronika", "komputery",
    "maszyny ciężkie", "wozy bojowe", "kutry",
    "rusznikarstwo", "wyrzutnie", "materiały wybuchowe",

    "pływanie", "wspinaczka", "kondycja",
    "jazda konna", "powożenie", "ujeżdżanie"]


class Requirement:
    def __init__(self, req_type, sub_type="", value="", children=[]):
        self.type: REQUIREMENT_TYPE = req_type
        self.subType: str = sub_type
        self.value: str = value
        self.children: list[Requirement] = children

dd = "Pistolety 3+ lub Karabiny 3+, Charakter 12+, Zręczność 12+"


def parseRequirements(req: str) -> list[Requirement]:
    reqs = []
    segs = req.lower().split(",")
    for seg in segs:
        reqs.append(parseSegment(seg))
    return reqs


def parseSegment(seg: str) -> Requirement:
    rq_type: REQUIREMENT_TYPE = REQUIREMENT_TYPE.UNKNOWN
    seg = seg.lower()
    if "lub" in seg:
        req = Requirement(REQUIREMENT_TYPE.SELECT)
        subsegs = seg.split("lub")
        for subseg in subsegs:
            req.children.append(parseSegment(subseg))
        return req

    # identify wspolczynnik
    for wspname in WSPOLCZYNNIK:
        if wspname.value in seg:
            seg = seg.replace(wspname.value, "").replace(" ", "").replace("+", "")
            if seg.isdigit():
                value = int(seg)
                return Requirement(REQUIREMENT_TYPE.WSPOLCZYNNIK, wspname, value)
            else:
                print(f"Invalid współczynnik value: {seg}")

    # identify umiejetnosc
    for umjname in UMIEJETNOSC:
        if umjname.value in seg:
            seg = seg.replace(umjname.value, "").replace(" ", "").replace("+", "")
            if seg.isdigit():
                value = int(seg)
                return Requirement(REQUIREMENT_TYPE.UMIEJETNOSC, umjname, value)
            else:
                print(f"Invalid umiejętność value: {seg}")




def extractNumber(value: str) -> int:
    return int(value.replace("+", "").replace(" ", ""))
