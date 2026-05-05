s = "hello"

def reverse_string(s: str) -> str:
    res = []
    for ch in s:
        res.append(ch)

    left, right = 0, len(res) - 1
    while left < right:
        res[left], res[right] = res[right], res[left]
        left += 1
        right -= 1

    return "".join(res)

print(reverse_string(s))