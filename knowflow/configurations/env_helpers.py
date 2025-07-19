from os import getenv


def strtobool(val: str) -> bool:
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True
    elif val in ("n", "no", "f", "false", "off", "0"):
        return False
    else:
        raise ValueError(f"Invalid truth value: {val}")


def get_env_var(key):
    return getenv(key)


def get_bool_env_var(key):
    return strtobool(getenv(key))


def get_list_env_var(key):
    return getenv(key).split(',')


def get_int_env_var(key):
    return int(getenv(key))
