def climbingSteps(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        x = climbingSteps(n-1) + climbingSteps(n-2)
        return x
    