def predictPartyVictory1(self, senate: str) -> str:
        #initialize 2 queue
        rad = []
        dir = []
        #loop through lst and put senators on corresponding queue
        for idx in range(len(senate)):
            if senate[idx] == "R":
                rad.append(idx)
            else:
                dir.append(idx)
        #let the senators fight each other until one team has no members left
        while len(rad) > 0 and len(dir) > 0:
            if rad[0] < dir[0]:
                dir.pop(0)
                rad.append(rad[0] + len(senate))
                rad.pop(0)
            else:
                rad.pop(0)
                dir.append(dir[0] + len(senate))
                dir.pop(0)
        #output winner
        return "Radiant" if len(rad) > 0 else "Dire"

from collections import deque
def predictPartyVictory2(senate: str) -> str:
        # O(n) time and space
        r_positions = deque([i for i, s in enumerate(senate) if s == 'R'])
        d_positions = deque([i for i, s in enumerate(senate) if s == 'D'])
        next_position = len(senate)
        while r_positions and d_positions:
            if r_positions[0] < d_positions[0]:
                r_positions.append(next_position)
            else:
                d_positions.append(next_position)
            r_positions.popleft()
            d_positions.popleft()
            next_position += 1
        return 'Radiant' if r_positions else 'Dire'

print(predictPartyVictory2("RDDDRDRRDR"))
