def bold_introduction(header):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"=================================\n"\
                  f"{header}\n"\
                  f"=================================\n")

            result = func(self, *args, **kwargs)
            return result
        return wrapper
    return decorator


def introduction(header):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"------------------------------------------------------------------------\n" \
            f"  🐾 {header} 🐾\n" \
            f"------------------------------------------------------------------------\n")
            result = func(self, *args, **kwargs)

            return result
        return wrapper
    return decorator