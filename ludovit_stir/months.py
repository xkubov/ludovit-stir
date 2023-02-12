from unidecode import unidecode

CZ_TO_SK_MONTHS = {
    "Leden": "Január",
    "Ledna": "Januára",
    "Lednu": "Januári",
    "Lednem": "Januárom",
    "Únor": "Február",
    "Února": "Februára",
    "Únoru": "Februári",
    "Únorem": "Februárom",
    "Březen": "Marec",
    "Března": "Marca",
    "Březnu": "Marci",
    "Březnem": "Marcom",
    "Duben": "Apríl",
    "Dubna": "Apríla",
    "Dubnu": "Apríli",
    "Dubnem": "Aprílom",
    "Květen": "Máj",
    "Května": "Mája",
    "Květnu": "Máji",
    "Květnem": "Májom",
    "Červen": "Jún",
    "Června": "Júna",
    "Červnu": "Júni",
    "Červnem": "Júnom",
    "Červenec": "Júl",
    "Července": "Júla",
    "Červenci": "Júli",
    "Červencem": "Júlom",
    "Srpen": "August",
    "Srpna": "Augusta",
    "Srpnu": "Augusti",
    "Srpnem": "Augustom",
    "Září": "Septemberi",
    "Zářím": "Septemberom",
    "Říjen": "Október",
    "Října": "Októbra",
    "Říjnu": "Októbri",
    "Říjnem": "Októbrom",
    "Listopad": "November",
    "Listopadu": "Novemberi",
    "Listopadem": "Novemberom",
    "Prosinec": "December",
    "Prosince": "Decembra",
    "Prosinci": "Decemberi",
    "Prosincem": "Decemberom",
}
SK_TO_CZ_MONTHS = {v: k for k, v in CZ_TO_SK_MONTHS.items()}

CZ_TO_SK_NORM = {unidecode(k).lower(): v for k, v in CZ_TO_SK_MONTHS.items()}
SK_TO_CZ_NORM = {unidecode(k).lower(): v for k, v in SK_TO_CZ_MONTHS.items()}


def check_for_months(text: str) -> tuple[list[str], list[str]]:
    """Check for slovak and czech versions of month names in the text."""
    slovak_months = []
    czech_months = []

    for word in text.split():
        norm = unidecode(word).lower()
        if norm in SK_TO_CZ_NORM:
            slovak_months.append(word)

        elif norm in CZ_TO_SK_NORM:
            czech_months.append(word)

    return slovak_months, czech_months


def translate_slovak_to_czech_months(text: str, slovak_months: list[str] | None = None) -> str:
    """
    Translates slovak months to czech months in text.
    """
    if slovak_months is None:
        slovak_months, _ = check_for_months(text)

    new_text = str(text)

    for word in slovak_months:
        result = SK_TO_CZ_NORM[unidecode(word).lower()]
        to_replace = result if word[0].isupper() else result.lower()
        new_text = new_text.replace(word, to_replace, 1)

    return new_text


def translate_czech_to_slovak_months(text: str, czech_months: list[str] | None = None) -> str:
    """
    Translates czech months to slovak months in text.
    """
    if czech_months is None:
        _, czech_months = check_for_months(text)

    new_text = str(text)

    for word in czech_months:
        result = CZ_TO_SK_NORM[unidecode(word).lower()]
        to_replace = result if word[0].isupper() else result.lower()
        new_text = new_text.replace(word, to_replace, 1)

    return new_text
