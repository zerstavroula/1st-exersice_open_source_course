import unittest

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
    return quantity * distance * freight_cost_per_unit

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

class TestSupplyChainFunctions(unittest.TestCase):

    def test_calculate_transportation_cost(self):
        # Test case 1
        self.assertEqual(calculate_transportation_cost(100, 200, 0.5), 100 * 200 * 0.5)
        # Test case 2
        self.assertEqual(calculate_transportation_cost(0, 200, 0.5), 0)

    def test_optimize_distribution(self):
        # Test case 1
        self.assertEqual(optimize_distribution(1000, 800), 800)
        # Test case 2
        self.assertEqual(optimize_distribution(500, 1000), 500)
        # Test case 3
        self.assertEqual(optimize_distribution(0, 500), 0)

if __name__ == '__main__':
    unittest.main()
