def bold_introduction(header, Symbol):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"=================================\n"\
                  f"{Symbol}  {header}  {Symbol}\n"\
                  f"=================================\n")

            result = func(self, *args, **kwargs)
            return result
        return wrapper
    return decorator


def introduction(header, Symbol):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"------------------------------------------------------------------------\n" \
            f"  {Symbol}  {header}  {Symbol}\n" \
            f"------------------------------------------------------------------------\n")
            result = func(self, *args, **kwargs)

            return result
        return wrapper
    return decorator