# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ndict = defaultdict(int)
        for char in tasks:
            ndict[char] += 1
        maxf = max(ndict.values())
        count = sum(1 for v in ndict.values() if v == maxf)
        time = (maxf - 1) * (n + 1) + count
        return max(len(tasks), time)


        