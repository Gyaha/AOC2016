def do_the_do(s: str) -> str:
    i = 0
    while i < len(s):
        if s[i] == "(":
            l = extract_marker_from(s, i)
            a, b = (int(c) for c in s[i + 1:i + l - 1].split("x"))
            s = "".join(list(s)[:i] + list(s)[i + l:])
            n = list(s)[i:i + a] * b
            s = "".join(list(s)[:i] + n + list(s)[i + a:])
            i += len(n)
        else:
            i += 1
    return s


def extract_marker_from(s: str, i: int):
    l = 0
    while not s[i + l] == ")":
        l += 1
    return l + 1


def really_extract_marker(s: str, i: int):
    l = 0
    while not s[i + l] == ")":
        l += 1
    l += 1
    a, b = (int(c) for c in s[i + 1:i + l - 1].split("x"))
    return l, a, b


def rec_values_and_subvalues(s: str, f: int, t: int):
    i = f
    v = 0
    while i < t:
        if s[i] == "(":
            l, a, b = really_extract_marker(s, i)
            sv = rec_values_and_subvalues(s, i + l, i + a + l)
            v += sv * b
            i += l + a
        else:
            i += 1
            v += 1
    return v


def decompress(s: str) -> int:
    return len(do_the_do(s))


def decomguess(s: str) -> int:
    return rec_values_and_subvalues(s, 0, len(s))


with open("input09") as file:
    d = file.read().strip()
    print(decompress(d))
    print(decomguess(d))
