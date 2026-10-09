import pulp as pl
prob = pl.LpProblem("Test")
x = prob.add_variable("x", lowBound=0)
prob += x, "Obj"
prob += x <= 1, "C1"
prob.solve()
print("v.dj:", prob.variables()[0].dj)
print("c.pi:", prob.constraints()[0].pi)
print("c.slack:", prob.constraints()[0].slack)
