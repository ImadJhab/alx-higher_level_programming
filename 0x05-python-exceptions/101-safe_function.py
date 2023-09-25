def safe_function(fct, *args):
    import sys
    try:
        i = fct(*args)
        return i
    except (Exception) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
