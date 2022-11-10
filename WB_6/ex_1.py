"""Выполните по вариантам соответственно реализацию генетического
алгоритма в соответствии с приложенными начальными данными."""

x = y = [-2, -1, 0, 1]


def qZ(x, y):
    return (x - 3 * y + 1) / (3 * x ** 2 + 3 * y ** 2 + 1)


def q_sum(z):
    return sum(z)


def exchange_scheme(olx_x, old_y, sorted_id):
    x = y = [0 for _ in range(4)]

    x[2] = x[3] = olx_x[sorted_id[2]]

    x[0] = olx_x[sorted_id[0]]
    x[1] = olx_x[sorted_id[1]]

    y[0] = y[1] = old_y[sorted_id[2]]

    y[2] = old_y[sorted_id[0]]
    y[3] = old_y[sorted_id[1]]

    return x, y


def sorting(z):
    sorted_id = sorted(range(len(z)), key=lambda k: z[k])
    return sorted_id


def evo_step(x, y, z):
    _, min_id = min((value, id) for (id, value) in enumerate(z))
    x = x[:]
    y = y[:]
    z = z[:]

    x.pop(min_id)
    y.pop(min_id)
    z.pop(min_id)

    return x, y, z


def evo_steps(x, y, step_num=4):
    results = []
    for i in range(step_num):
        arr_z = [qZ(x, y[i]) for i, x in enumerate(x)]
        x, y, z = evo_step(x, y, arr_z)
        x, y = exchange_scheme(x, y, sorting(z))
        results.append([x, y, q_sum(arr_z), arr_z])
    return x, y, results


if __name__ == '__main__':
    results = evo_steps(x, y)
    quality_arr_z = []
    for i in range(len(results[2])):
        print(f'max_{i + 1}_step: {results[2][i][2]}')
        quality_arr_z += results[2][i][3]
    print(f'max z: {max(quality_arr_z)}')

