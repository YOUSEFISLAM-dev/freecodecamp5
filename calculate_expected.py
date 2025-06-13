# Working backwards from expected test values
# Line 1: 1880 -> -0.54, 2050 -> 15.85
x1, y1 = 1880, -0.54
x2, y2 = 2050, 15.85

slope_expected_1 = (y2 - y1) / (x2 - x1)
intercept_expected_1 = y1 - slope_expected_1 * x1

print(f"Expected Line 1: slope={slope_expected_1:.6f}, intercept={intercept_expected_1:.6f}")

# Line 2: 2000 -> 6.95, 2050 -> 14.38
x3, y3 = 2000, 6.95
x4, y4 = 2050, 14.38

slope_expected_2 = (y4 - y3) / (x4 - x3)
intercept_expected_2 = y3 - slope_expected_2 * x3

print(f"Expected Line 2: slope={slope_expected_2:.6f}, intercept={intercept_expected_2:.6f}")

# Let's also check what these would produce at key points
print(f"\nExpected Line 1 check:")
print(f"  1880: {slope_expected_1 * 1880 + intercept_expected_1:.2f}")
print(f"  2050: {slope_expected_1 * 2050 + intercept_expected_1:.2f}")

print(f"\nExpected Line 2 check:")
print(f"  2000: {slope_expected_2 * 2000 + intercept_expected_2:.2f}")
print(f"  2050: {slope_expected_2 * 2050 + intercept_expected_2:.2f}")

print(f"\nSlope 1 is about {slope_expected_1:.6f} which is about {slope_expected_1:.3f} per year")
print(f"Slope 2 is about {slope_expected_2:.6f} which is about {slope_expected_2:.3f} per year")
