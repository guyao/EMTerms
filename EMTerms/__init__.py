import pkgutil
from .emterms import EMTerms
from .emterms import load_emterms


def test():
    emt = EMTerms(pkgutil.get_data(__package__, "data/EMTerms.csv"))
    import csv
    import io
    import time
    data = pkgutil.get_data(__package__, "data/EMTerms.csv")
    csvio = io.StringIO(data.decode("utf-8"))
    csvreader = csv.reader(csvio)
    next(csvio) # skip first line
    count = 0
    st = time.time()
    for n, l in enumerate(csvreader):
        term, code, category, ex = l
        result = emt.match_one(term, ex)
        if not result:
            count += 1
    ed = time.time()
    print(n,"in", str(ed - st))
    print(count)

