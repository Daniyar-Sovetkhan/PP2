def fahrenheit(F):
    celsius = (5 / 9) * (F - 32)
    return celsius



F = float(input())
C = fahrenheit(F)
print(F"{C:.2f}°C")