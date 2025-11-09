# Tunnel Alignment / Tunnel Survey Computation
import math

# Input angles (grad) and distances (meters)
kn = 165.9824  # Not used in calculation
k1 = 230.1762
k2 = 219.3528
k3 = 171.4655

s1 = 62.19
s2 = 78.13
s3 = 70.84

# Point names
POINTS = ['N', 'P1', 'P2', 'K']

# Deflection angles (grad)
deflection_angles = [400 - k1, 400 - k2]  

# Open angles (grad) - cumulative calculation
open_angles = [
    100, 
    deflection_angles[0] + 100 - 200, 
    deflection_angles[1] + 100 - 200 + deflection_angles[0] - 200
]

# Edge lengths
edges = [s1, s2, s3]

# Function to convert grad to radians
def grad_to_radian(grad):
    return grad * (math.pi / 200)

# Compute delta Y and delta X for each edge
delta_y = [s1 * math.sin(grad_to_radian(open_angles[0])),
           s2 * math.sin(grad_to_radian(open_angles[1])),
           s3 * math.sin(grad_to_radian(open_angles[2]))]

delta_x = [s1 * math.cos(grad_to_radian(open_angles[0])),
           s2 * math.cos(grad_to_radian(open_angles[1])),
           s3 * math.cos(grad_to_radian(open_angles[2]))]

# Compute cumulative coordinates
y_coords = [100,
            100 + delta_y[0],
            100 + delta_y[0] + delta_y[1],
            100 + delta_y[0] + delta_y[1] + delta_y[2]]

x_coords = [100,
            100 + delta_x[0],
            100 + delta_x[0] + delta_x[1],
            100 + delta_x[0] + delta_x[1] + delta_x[2]]

# Total delta Y and delta X
total_delta_y = sum(delta_y)
total_delta_x = sum(delta_x)

# Print intermediate results
print("Deflection angles (grad):", deflection_angles)
print("Open angles (grad):", open_angles)
print("Delta X:", delta_x)
print("Delta Y:", delta_y)
print("X coordinates:", x_coords)
print("Y coordinates:", y_coords)
print("Total delta Y:", total_delta_y)
print("Total delta X:", total_delta_x)

# Compute tunnel axis direction (radians and degrees)
tunnel_axis_rad = math.atan(total_delta_y / total_delta_x)
tunnel_axis_deg = math.degrees(tunnel_axis_rad)

print(f"Tunnel axis angle: {tunnel_axis_deg} degrees")
print(f"Tunnel axis angle: {tunnel_axis_rad} radians")
