class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start = 0
        stop = len(skill)-1
        team_sum = skill[0] + skill[-1]
        total = 0
        while start<=stop:
            if (team_sum != skill[start]+skill[stop]):
                return -1
            total += skill[start]*skill[stop]
            start += 1
            stop -=1
        return total
            


