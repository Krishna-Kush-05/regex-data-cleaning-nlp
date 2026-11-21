# Data cleaning and NLP - regex validator and extractor
import re

PATTERNS = {
    "1": ("Mobile number", r"^(\+91[ -]?)?[6-9][0-9]{9}$"),
    "2": ("Date (DD/MM/YYYY)", r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"),
    "3": ("Hashtag", r"^#[A-Za-z][A-Za-z0-9_]*$"),
    "4": ("URL", r"^https?://[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+(/[^\s]*)?$"),
    "5": ("Rupee amount", r"^(Rs\.?|₹)[0-9]+(\.[0-9]{2})?$"),
}

EXTRACT = {
    "mobile": r"(?:\+91[ -]?)?[6-9][0-9]{9}",
    "date": r"(?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[0-2])/[0-9]{4}",
    "hashtag": r"#[A-Za-z][A-Za-z0-9_]*",
    "url": r"https?://[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+(?:/[^\s]*)?",
}


def validate():
    print("\nChoose a type to validate:")
    for k, (name, _) in PATTERNS.items():
        print(f"  {k}. {name}")
    choice = input("Enter choice: ").strip()
    if choice not in PATTERNS:
        print("Wrong choice")
        return
    name, pat = PATTERNS[choice]
    text = input(f"Enter {name}: ").strip()
    if re.fullmatch(pat, text):
        print("Valid")
    else:
        print("Invalid")


def extract():
    text = input("\nPaste a line of text: ")
    for label, pat in EXTRACT.items():
        found = re.findall(pat, text)
        print(f"{label:8}: {found if found else 'none'}")


def main():
    while True:
        print("\n1. Validate a string\n2. Extract from text\n3. Exit")
        op = input("Option: ").strip()
        if op == "1":
            validate()
        elif op == "2":
            extract()
        elif op == "3":
            break
        else:
            print("Wrong option")


if __name__ == "__main__":
    main()
