import hashlib


def contains_a_tripple(md5: str) -> chr:
    for l in range(30):
        if md5[l] == md5[l + 1] == md5[l + 2]:
            return md5[l]
    return None


def contains_a_fipple(md5: str, m: chr) -> bool:
    for l in range(27):
        if m == md5[l] == md5[l + 1] == md5[l + 2] == md5[l + 3] == md5[l + 4]:
            return True
    return False


def to_md5_x(s: str, cache: dict) -> str:
    if s in cache.keys():
        return cache[s]
    s2 = s
    for _ in range(2017):
        s2 = to_md5(s2)
    cache[s] = s2
    return s2


def to_md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def find_code_num(w: str, n: int):
    i = 0
    while True:
        i += 1
        e = contains_a_tripple(to_md5(w + str(i)))
        if e:
            for l in range(1, 1001):
                if contains_a_fipple(to_md5(w + str(i + l)), e):
                    n -= 1
                    if n == 0:
                        return i
                    break


def find_code_with_cache(w: str, n: int):
    cache = {}
    i = 0
    while True:
        i += 1
        e = contains_a_tripple(to_md5_x(w + str(i), cache))
        if e:
            for l in range(1, 1001):
                if contains_a_fipple(to_md5_x(w + str(i + l), cache), e):
                    n -= 1
                    if n == 0:
                        return i
                    break


print(find_code_num("cuanljph", 64))
print(find_code_with_cache("cuanljph", 64))
