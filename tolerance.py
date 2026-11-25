nominal = 10.00
tolerance = 0.05

measured = float(input("Measured value in mm: "))

if abs(measured - nominal) <= tolerance:
    print("PASS")
else:
    print("FAIL: raise a non-conformance")
