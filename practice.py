from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0  # Total gas available from all stations.
        total_cost = 0  # Total cost to travel between all stations.
        current_gas = 0  # Gas available at the current station.
        start_index = 0  # Starting station index.

        for i in range(len(gas)):
            # Calculate the difference between gas available and the cost at the current station.
            diff = gas[i] - cost[i]

            # Update the current gas and total values.
            current_gas += diff
            total_gas += diff
            total_cost += diff

            # If running out of gas at this station, update the start index to the next station.
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1

        # If the total gas available is greater than or equal to the total cost, a valid route exists.
        if total_gas >= total_cost:
            return start_index
        else:
            return -1  # No valid route exists.

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]