# -*- coding: utf-8 -*-


def m(get, exps, step, better):

    print(get, exps, step, better)
    # print(get, step, better)

    if step > better:
        return None

    for i in range(0, len(exps)):
        for j in range(0, len([0] + exps)):
            new_exp = exps[i] + ([0] + exps)[j]

            # print(new_exp)

            if new_exp == get:
                return step
            elif new_exp > get:
                return None

            # exps.append(new_exp)

            new_step = m(get, exps + [new_exp], step + 1, better)
            if new_step:
                if new_step < better:
                    better = new_step
                else:
                    return None

    return better


def result():
    # por definicion al inicio, el mejor será 15
    b = m(15, [1], 0, 15)

    return b
