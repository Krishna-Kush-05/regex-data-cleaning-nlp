import re
from demo import PATTERNS

TESTS = {
 "1": (["9876543210","6000000001","+91 9123456780","+91-8888888888","7012345678"],
       ["5876543210","98765","98765432101","abcdefghij","+92 9876543210"]),
 "2": (["01/01/2024","31/12/1999","15/08/2026","29/02/2024","10/10/2010"],
       ["32/01/2024","00/05/2024","12/13/2024","1/1/2024","12-05-2024"]),
 "3": (["#python","#Data_Science","#TOC2026","#nlp","#a1_b2"],
       ["python","#","#1stplace","# space","#bad-tag"]),
 "4": (["http://example.com","https://www.google.co.in","https://github.com/user/repo","http://a-b.org/page?x=1","https://sub.domain.edu/path/file.html"],
       ["example.com","ftp://example.com","http://","https://nodot","http://exa mple.com"]),
 "5": (["Rs100","Rs.250.50","₹999","₹10.00","Rs.5"],
       ["100","Rs","₹1.5","Rs.-20","$50"]),
}
bad = 0
for k,(name,pat) in PATTERNS.items():
    v,i = TESTS[k]
    print(f"\n{k}. {name}   {pat}")
    for s in v:
        ok = bool(re.fullmatch(pat,s)); bad += (not ok)
        print(f"  {s!r:42} expected Valid   got {'Valid' if ok else 'Invalid'}  {'OK' if ok else 'MISMATCH'}")
    for s in i:
        ok = not re.fullmatch(pat,s); bad += (not ok)
        print(f"  {s!r:42} expected Invalid got {'Invalid' if ok else 'Valid'}  {'OK' if ok else 'MISMATCH'}")
print("\nMismatches:", bad)
