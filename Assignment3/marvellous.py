def CheckPrime(no):
    for i in range(2, no + 1):
        if i != no:
            if no % i == 0:
                return False
        else:
            return True
