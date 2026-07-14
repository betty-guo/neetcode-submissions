class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [] # stack to track fleets, if current fleet after one hour is behind the next item on the stack, combine the next item into the fleet
        # compute the time it takes for car at position[i] to reach the target
        # if the time for car at position[i] is < then car at position[i+1], then they become a fleet
        # use a stack to track the time for each car in order, append as long as the target time is > then the one in front of it
        # build tuple, sort by first position tuple, sort descending (default is ascending)
        sorted_positions = sorted(zip(position, speed), key=lambda x: x[0], reverse = True) # start with the car that is closest to the target
        print(sorted_positions)
        for p, s in sorted_positions:
            target_time = (target - p)/s
            if fleets and target_time <= fleets[-1] :
                #fleets.append(target_time) # should not append, it becomes a fleet with the existing one
                continue
            else:
                fleets.append(target_time)
        
        return len(fleets)

        # fleets = []
        # fleets = [3] # it takes car at 4 3 hours to get to 10
        # fleets = [3] # it takes car at position 1 3 hours to get to 10