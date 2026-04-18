import random

# ---------------------------
# NAMES
# ---------------------------

MALE_NAMES = [
    ("Mohamed", 12), ("Ahmed", 11), ("Ali", 9), ("Yacine", 8),
    ("Karim", 7), ("Sofiane", 6), ("Nassim", 6), ("Riad", 5),
    ("Walid", 5), ("Samir", 5), ("Amine", 7)
]

FEMALE_NAMES = [
    ("Amina", 10), ("Sara", 9), ("Yasmine", 8), ("Nesrine", 7),
    ("Imane", 7), ("Khadija", 6), ("Samira", 6)
]

LAST_NAMES = [
    ("Benali", 12), ("Brahimi", 10), ("Mansouri", 9),
    ("Zerrouki", 8), ("Saadi", 7), ("Touati", 7),
    ("Meziane", 8), ("Bouzid", 7), ("Khelifi", 6),
    ("Bensalem", 6), ("Cherif", 6), ("Hamdi", 5)
]

# ---------------------------
# WILAYAS (sample set)
# ---------------------------

WILAYAS = [
    {
        "province_name": "Adrar",
        "province_name_ar": "أدرار",
        "province_code": "01",
        "cities": ["Adrar", "Reggane", "Timimoun"]
    },
    {
        "province_name": "Chlef",
        "province_name_ar": "الشلف",
        "province_code": "02",
        "cities": ["Chlef", "Ténès", "Oued Fodda"]
    },
    {
        "province_name": "Alger",
        "province_name_ar": "الجزائر",
        "province_code": "16",
        "cities": ["Alger", "Bab Ezzouar", "El Harrach"]
    },
    {
        "province_name": "Setif",
        "province_name_ar": "سطيف",
        "province_code": "19",
        "cities": ["Setif", "El Eulma", "Ain Oulmene"]
    },
    {
        "province_name": "Oran",
        "province_name_ar": "وهران",
        "province_code": "31",
        "cities": ["Oran", "Es Senia", "Bir El Djir"]
    }
]

# ---------------------------
# INTERNAL HELPERS
# ---------------------------

def _weighted_choice(data):
    names = [x[0] for x in data]
    weights = [x[1] for x in data]
    return random.choices(names, weights=weights, k=1)[0]


def _generate_phone():
    prefix = random.choices(["05", "06", "07"], weights=[3, 4, 3])[0]
    return prefix + ''.join(str(random.randint(0, 9)) for _ in range(8))


_used_phones = set()


def _generate_address():
    wilaya = random.choice(WILAYAS)
    city = random.choice(wilaya["cities"])

    return {
        "province_name": f'{wilaya["province_name"]} - {wilaya["province_name_ar"]}',
        "province_code": wilaya["province_code"],
        "city": city.upper()
    }

# ---------------------------
# PUBLIC API
# ---------------------------

def go(unique_phone=True):
    gender = random.choice(["male", "female"])

    first_name = _weighted_choice(MALE_NAMES if gender == "male" else FEMALE_NAMES)
    last_name = _weighted_choice(LAST_NAMES)

    # phone generation
    if unique_phone:
        while True:
            phone = _generate_phone()
            if phone not in _used_phones:
                _used_phones.add(phone)
                break
    else:
        phone = _generate_phone()

    return {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "address": _generate_address()
    }