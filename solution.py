
def discretionary_exp(income, expense) :
    diff = [income[i] - expense[i] for i in range(len(income))]
    cummulative_diff = []
    cum_diff = 0
    for d in diff :
        cum_diff += d
        cummulative_diff.append(cum_diff)

    disc_exp = [cummulative_diff[0]]
    for i in range(1, len(cummulative_diff)) :
        diff = cummulative_diff[i]
        start_index = 0
        avg_disc_exp = 1. * (diff - sum(disc_exp[:start_index]))/(len(disc_exp[start_index:]) + 1)

        while avg_disc_exp > disc_exp[start_index] :
            start_index += 1
            if start_index < len(disc_exp) :
                avg_disc_exp = 1. * (diff - sum(disc_exp[:start_index]))/(len(disc_exp[start_index:]) + 1)
            else :
                avg_disc_exp = diff - sum(disc_exp[:start_index])
                break
        if avg_disc_exp < 0 :
            raise ValueError("Happiness is questionable! No solution possible for these inputs")
            
        for index in range(start_index, len(disc_exp)) :
            disc_exp[index] = avg_disc_exp
        disc_exp.append(avg_disc_exp)
    return disc_exp


income = [10, 10, 10, 10, 10]
expense = [9, 8, 6, 12, 6]
## this should give [1, 4/3, 4/3, 4/3, 4]
print(discretionary_exp(income, expense))


income = [10, 10, 10, 10, 10]
expense = [9, 12, 6, 12, 6]
## The following should lead to a value error as no solution is possible
print(discretionary_exp(income, expense))
