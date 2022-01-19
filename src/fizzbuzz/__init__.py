def fizzbuzz(n: int) -> dict:
    error = _invalid_n(n)
    if error:
        return dict(error=error)

    fizzbuzz = [_do_fizzbuzz(i) for i in range(1, n + 1)]
    return dict(data=fizzbuzz)


def _do_fizzbuzz(n: int) -> str:
    parts = []
    if n % 3 == 0:
        parts.append("fizz")
    if n % 5 == 0:
        parts.append("buzz")

    if parts:
        return "".join(parts)
    else:
        return str(n)


def _invalid_n(n):
    req = "Please provide a positive integer less than or equal to 1_000."
    if not isinstance(n, int):
        return f"Not an integer. {req}"
    if n < 1:
        return f"Zero and negative integers not supported. {req}"
    if n > 1_000:
        return f"Integer too large. {req}"
    return None
