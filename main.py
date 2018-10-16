from utils import get_function_details
from WOA import WOA # comment and uncomment below to test your version
#from WOA_hoog import WOA
import matplotlib.pyplot as plt

n_agents = 30
func_name = 'F1'
max_iter = 500
lower_b, upper_b, dim, bench_f = get_function_details(func_name)

woa = WOA(n_agents, max_iter, lower_b, upper_b, dim, bench_f)
best_score, best_pos, conv_curve = woa.forward()
print(best_score)

fig, ax = plt.subplots()
ax.plot(conv_curve)
ax.set(xlabel='iter', ylabel='leader_score',
       title='Objective Space')
plt.show()
