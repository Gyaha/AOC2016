gens_1 = [5, 0, 0, 0]
chps_1 = [3, 2, 0, 0]
gens_2 = [7, 0, 0, 0]
chps_2 = [5, 2, 0, 0]


def chk_meltdown(gens, chps):
    for i in range(len(gens)):
        if gens[i] and gens[i] < chps[i]:
            return True
    return False


def chk_done(gens, chps):
    s = sum(gens)
    i = len(gens) - 1
    return gens[i] == s and chps[i] == s


def mov_abt(gens, chps, elev, move, done):
    if done[0]:
        return
    if chk_meltdown(gens, chps):
        return
    if chk_done(gens, chps):
        print(move)
        done[0] = True
        return
    move += 1
    if elev < 3:
        mov_up(gens, chps, elev, move, done)
    if elev > 0:
        mov_dwn(gens, chps, elev, move, done)


def mov_up(gens_org: list, chps_org: list, elev, move, done):
    # 2 0
    gens = gens_org.copy()
    chps = chps_org.copy()
    if gens[elev] >= 2:
        gens[elev] -= 2
        gens[elev + 1] += 2
        mov_abt(gens, chps, elev + 1, move, done)

    # 0 2
    gens = gens_org.copy()
    chps = chps_org.copy()
    if chps[elev] >= 2:
        chps[elev] -= 2
        chps[elev + 1] += 2
        mov_abt(gens, chps, elev + 1, move, done)

    # 1 1
    gens = gens_org.copy()
    chps = chps_org.copy()
    if chps[elev] >= 1 and gens[elev] >= 1:
        chps[elev] -= 1
        chps[elev + 1] += 1
        gens[elev] -= 1
        gens[elev + 1] += 1
        mov_abt(gens, chps, elev + 1, move, done)


def mov_dwn(gens_org, chps_org, elev, move, done):
    # 1 0
    gens = gens_org.copy()
    chps = chps_org.copy()
    if gens[elev] >= 1:
        gens[elev] -= 1
        gens[elev - 1] += 1
        mov_abt(gens, chps, elev - 1, move, done)

    # 0 1
    gens = gens_org.copy()
    chps = chps_org.copy()
    if chps[elev] >= 1:
        gens[elev] -= 1
        gens[elev - 1] += 1
        mov_abt(gens, chps, elev - 1, move, done)


mov_abt(gens_1, chps_1, 0, 0, [False])
mov_abt(gens_2, chps_2, 0, 0, [False])
