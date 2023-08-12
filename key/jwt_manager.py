from jwt import encode, decode

def create_access_token(data: dict):
    return encode(
        payload     = data,
        key         = "Jimmy4-Unwrapped-Justify",
        algorithm   = "HS256"
    )


def decode_access_token(token: str) -> dict:
    return decode(
        jwt         = token,
        key         = "Jimmy4-Unwrapped-Justify",
        algorithms  = ["HS256"]
    )