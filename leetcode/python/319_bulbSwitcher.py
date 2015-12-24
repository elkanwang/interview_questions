'''
There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every third
bulb (turning on if it's off or turning off if it's on). For the nth round, you
only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
'''

'''
def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    resArr = [0] * (n + 1)
    for i in range(1, n):
        for j in range(1, n):
            index = i * j
            if (index <= n):
                oVal = resArr[index]
                if (oVal == 1):
                    resArr[index] = 0
                else:
                    resArr[index] = 1
    print resArr
    res = 0
    for i in range(1, n):
        if resArr[i] == 1:
            res = res + 1
    return res
'''


'''
For prime numbers, they must be off because we can reach them only twice (The first round and their own round).
For other numbers, if we can reach them odd times, then they are on; otherwise, they are off. So only
 those numbers who have square root will be reached odd times and there are sqrt(n) of them because
 for every x > sqrt(n), x*x > n and thus should not be considered as the answer. */
'''

def bulbSwitch(n):
    import math
    return int(math.sqrt(n))
print bulbSwitch(3)
print bulbSwitch(99)


