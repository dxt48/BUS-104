import pulp as pl

prob = pl.LpProblem("ShortestPath", pl.LpMinimize)

x_ab = prob.add_variable("x_ab", lowBound=0)
x_ac = prob.add_variable("x_ac", lowBound=0)
x_bc = prob.add_variable("x_bc", lowBound=0)

prob += 1*x_ab + 4*x_ac + 2*x_bc

prob += x_ab + x_ac == 1, "Node_A"
prob += x_bc - x_ab == 0, "Node_B"
prob += x_ac + x_bc == 1, "Node_C"

res = prob.solve()

print("Status:", res.status.name)
