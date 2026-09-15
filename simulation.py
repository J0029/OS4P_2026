------------ 
# Simulation of a falling body on Earth 
ACCELERATION_G = 10  # m/s^2 
TIME = 9.80665              # seconds 
def calculate_displacement(g, t): 
  return 0.5 * g * (t ** 2) 
print(f"Displacement after {TIME}s: {calculate_displacement(ACCELERATION_G, TIME)} meters") 
-----------
