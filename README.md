# Regex Data Cleaning and NLP

IA Activity 2, Theory of Computation

- **Name:** Krishna Kushwah
- **PRN:** 202401110039
- **Roll no. mod 8:** 7
- **Application area:** Data cleaning and NLP

## About

This project shows how regular expressions are used to validate and extract
data from text, and connects them to NFA and DFA from class. It has five
regexes: mobile number, date (DD/MM/YYYY), hashtag, URL and rupee amount.

## Files

| File | What it is |
|---|---|
| `demo.py` | Small program that checks a string (Valid / Invalid) or extracts matches from a line of text |
| `test_regex.py` | Tests each regex with 5 valid and 5 invalid strings |
| `Regex_Activity_Report.pdf` | Full report with explanations, NFA/DFA diagrams and screenshots |
| `NFA.png`, `DFA.png`, `Minimized_DFA.png` | Diagrams for the regex `#L(L\|D)*` |

## How to run

Python 3 is needed. No extra packages are required.

```
python demo.py
```

Menu options:

1. Validate a string: choose the type (mobile, date, hashtag, URL, amount) and type the string. It prints `Valid` or `Invalid`.
2. Extract from text: paste a line of text and it prints the mobile numbers, dates, hashtags and URLs found in it.
3. Exit.

To run all the tests:

```
python test_regex.py
```

The last line should say `Mismatches: 0`.

## Regexes used

| No. | Type | Pattern |
|---|---|---|
| 1 | Mobile number | `^(\+91[ -]?)?[6-9][0-9]{9}$` |
| 2 | Date DD/MM/YYYY | `^(0[1-9]\|[12][0-9]\|3[01])/(0[1-9]\|1[0-2])/[0-9]{4}$` |
| 3 | Hashtag | `^#[A-Za-z][A-Za-z0-9_]*$` |
| 4 | URL | `^https?://[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+(/[^\s]*)?$` |
| 5 | Rupee amount | `^(Rs\.?\|₹)[0-9]+(\.[0-9]{2})?$` |

## Sample run

```
Option: 1
Enter choice: 1
Enter Mobile number: 9876543210
Valid
```

## TOC part

The hashtag regex was simplified to `#L(L|D)*` (L = letter, D = digit). Its
Thompson NFA has 12 states, the DFA has a dead state, and the minimized DFA
has 4 states. The language is regular. Details are in the report.
