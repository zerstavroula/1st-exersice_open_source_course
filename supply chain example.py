def calculate_transportation_cost(quantity, distance, freight_cost_per_unit):
    """
    Calculate the total transportation cost.

    Parameters:
    quantity (int): Quantity of goods to transport.
    distance (float): Distance of transportation.
    freight_cost_per_unit (float): Freight cost per unit distance.

    Returns:
    float: Total transportation cost.
    """
    return quantity * distance * freight_cost_per_unit*5

def optimize_distribution(supply, demand):
    """
    Optimize the distribution of goods given supply and demand constraints.

    Parameters:
    supply (int): Total supply of goods.
    demand (int): Total demand for goods.

    Returns:
    int: Optimal quantity of goods to distribute.
    """
    return min(supply, demand)

# Example usage:
supply_quantity = 1000  # Total supply of goods
demand_quantity = 800   # Total demand for goods
distance = 500          # Distance of transportation (in miles)
freight_cost_per_unit_distance = 0.05  # Freight cost per unit distance (in dollars)

optimal_quantity = optimize_distribution(supply_quantity, demand_quantity)
total_cost = calculate_transportation_cost(optimal_quantity, distance, freight_cost_per_unit_distance)

print("Optimal quantity to distribute:", optimal_quantity)
print("Total transportation cost:", total_cost)

