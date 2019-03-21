def calc_exp(units, log=False):
	exp = {"total":0, "by_unit":[]}
	unitsExp = 0
	for i in range(1,units + 1):
		if exp["total"] == 0:
			unitsExp = i
		else:
			unitsExp = 1 / exp["total"]
		if log:
			print("{}: {} + {} = {}".format(i, exp["total"], unitsExp, exp["total"] + unitsExp))
		exp["by_unit"].append(unitsExp)
		exp["total"] = exp["total"] + unitsExp
	return exp

test = calc_exp(78)
bu = test["by_unit"]
reduce(lambda x,y: x + y, bu[:19])
