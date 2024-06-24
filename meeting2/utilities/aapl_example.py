from pprint import pprint

filepath = "/Users/valeria/src/intel/intel-basic-python-jun-24/meeting2/data/AAPL.csv"
prices = []
with open(filepath) as f:
    header = f.readline().strip().split(",")
    for line in f:
        obj = {}
        for field, val in zip(header, line.replace("\n", "").split(",")):
            if field != 'Date':
                obj[field] = round(float(val), 2)
            else:
                obj[field] = val
        prices.append(obj)

pprint(prices)