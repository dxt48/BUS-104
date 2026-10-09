import pulp as pl

prob = pl.LpProblem("ShortestPath", pl.LpMinimize)

x_ab = prob.add_variable("x_ab", lowBound=0)
x_ac = prob.add_variable("x_ac", lowBound=0)
x_bc = prob.add_variable("x_bc", lowBound=0)

prob += 1*x_ab + 4*x_ac + 2*x_bc

prob += x_ab + x_ac == 1, "A"
prob += x_bc - x_ab == 0, "B"
prob += x_ac + x_bc == 1, "C"

res = prob.solve()

print("Status:", res.status.name)
print("Optimal Solution:")
print(f"x_ab = {x_ab.varValue}")
print(f"x_ac = {x_ac.varValue}")
print(f"x_bc = {x_bc.varValue}")
print(f"Minimum Cost = {pl.value(prob.objective)}")
