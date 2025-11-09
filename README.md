# Tunnel Survey Computation

This project calculates the coordinates of tunnel points based on deflection angles, open angles, and edge lengths. It is implemented in Python.

## Overview

The code performs a simple **2D tunnel alignment calculation**:

1. **Inputs:**
   - Deflection angles (`k1, k2, k3`) in grads
   - Edge lengths (`s1, s2, s3`) in meters
2. **Calculations:**
   - Convert grad angles to radians
   - Compute delta X and delta Y for each tunnel segment
   - Determine cumulative coordinates of each point along the tunnel
   - Compute total delta X and delta Y
   - Calculate tunnel axis direction in radians and degrees
3. **Outputs:**
   - Coordinates (`X`, `Y`) of all tunnel points
   - Total ΔX and ΔY
   - Tunnel axis angle in radians and degrees

## How to use

1. Open the Python script `tunnel_alignment.py`.
2. Adjust the input angles (`k1, k2, k3`) and segment lengths (`s1, s2, s3`) if needed.
3. Run the script. It prints:
   - Deflection and open angles
   - ΔX and ΔY for each segment
   - Cumulative coordinates
   - Tunnel axis direction

## Notes

- The code uses **grad units** for angles, which are converted to **radians** for trigonometric calculations.
- Initial coordinates start at `(100, 100)` for demonstration purposes.
- The tunnel axis angle is computed using `atan(ΔY / ΔX)`.

