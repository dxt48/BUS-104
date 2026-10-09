import pulp as pl
prob = pl.LpProblem("Test", pl.LpMaximize)
x = prob.add_variable("x", lowBound=0)
prob += x, "Obj"
prob += x <= 1
res = prob.solve()
print("res =", res)
print("res name =", getattr(res, 'name', None))
