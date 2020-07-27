def hyper_volume(*numbers):
    gen = iter(numbers)
    volume = next(gen)
    for idx in gen:
        volume *= idx
    return volume


if __name__ == "__main__":
    print(f"Hyper Volume: {hyper_volume(2,4)}")
    print(f"Hyper Volume: {hyper_volume(2,4,6,8,10,12)}")
