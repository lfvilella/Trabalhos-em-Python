if __name__ == "__main__":
    two_more = lambda num=None: num + 2 if num else "Are you kidding me?"
    print(two_more(1))
    print(two_more())
