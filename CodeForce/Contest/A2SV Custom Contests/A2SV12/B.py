def charge_joysticks(charges):
    count = 0
    while min(charges) > 0 and max(charges) > 1:
        charges = [min(charges) + 1, max(charges) - 2]
        count += 1
    return count


if __name__ == "__main__":
    inputs = list(map(int, input().split()))
    print(charge_joysticks(inputs))
