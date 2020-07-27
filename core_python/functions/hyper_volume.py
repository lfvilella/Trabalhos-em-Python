def hyper_volume(number, *numbers):
    volume = number
    for idx in numbers:
        volume *= idx
    return volume


if __name__ == "__main__":
    print(f"Hyper Volume: {hyper_volume(2)}")
    print(f"Hyper Volume: {hyper_volume(2,4)}")
    print(f"Hyper Volume: {hyper_volume(2,4,6,8,10,12)}")

    numbers = (1, 2, 3, 4, 5, 6, 7)
    print(f"Hyper Volume: {hyper_volume(*numbers)}")
