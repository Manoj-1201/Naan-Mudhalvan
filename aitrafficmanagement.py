import random
import matplotlib.pyplot as plt
import pandas as pd

# Static control timing (in seconds)
STATIC_GREEN_TIME = 30
STATIC_YELLOW_TIME = 5
STATIC_RED_TIME = 30

# Dynamic control max and min green time
MAX_GREEN_TIME = 45
MIN_GREEN_TIME = 10

# Simulated intersection with four lanes
lanes = ['North', 'South', 'East', 'West']

# Function to simulate static control
def static_control_simulation():
    total_wait_times = []
    for cycle in range(10):  # Simulate 10 cycles
        cycle_wait_time = 0
        print("\nStatic Control - Cycle", cycle + 1)
        for lane in lanes:
            # Assuming a fixed vehicle count for simplicity
            vehicle_count = random.randint(10, 30)
            print(f"Lane {lane}: Vehicles = {vehicle_count}")
            # Static waiting time based on fixed timings
            wait_time = STATIC_GREEN_TIME + STATIC_YELLOW_TIME + STATIC_RED_TIME
            cycle_wait_time += vehicle_count * wait_time  # No need to divide by len(lanes)
        total_wait_times.append(cycle_wait_time)
    return total_wait_times

# Function to simulate dynamic control
def dynamic_control_simulation():
    total_wait_times = []
    for cycle in range(10):  # Simulate 10 cycles
        cycle_wait_time = 0
        print("\nDynamic Control - Cycle", cycle + 1)
        for lane in lanes:
            # Random vehicle count for each lane
            vehicle_count = random.randint(10, 30)
            print(f"Lane {lane}: Vehicles = {vehicle_count}")
            # Adjust green time based on vehicle count
            green_time = min(MAX_GREEN_TIME, max(MIN_GREEN_TIME, vehicle_count))
            # Dynamic waiting time based on adjusted green time
            wait_time = green_time + STATIC_YELLOW_TIME + STATIC_RED_TIME
            cycle_wait_time += vehicle_count * wait_time  # No need to divide by len(lanes)
        total_wait_times.append(cycle_wait_time)
    return total_wait_times

# Run simulations
static_wait_times = static_control_simulation()
dynamic_wait_times = dynamic_control_simulation()

# Data visualization
cycles = list(range(1, 11))  # Cycle numbers for x-axis
df = pd.DataFrame({
    'Cycle': cycles,
    'Static Wait Time': static_wait_times,
    'Dynamic Wait Time': dynamic_wait_times
})

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df['Cycle'], df['Static Wait Time'], marker='o', label="Static Control")
plt.plot(df['Cycle'], df['Dynamic Wait Time'], marker='x', label="Dynamic Control")
plt.xlabel('Cycle')
plt.ylabel('Total Wait Time (seconds)')
plt.title('Static vs Dynamic Traffic Signal Control')
plt.legend()
plt.grid()
plt.show()
