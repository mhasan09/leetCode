class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull_counter = 0
        cows_counter = 0
        new_secret = []
        new_guess = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull_counter += 1
            else:
                new_secret.append(secret[i])
                new_guess.append(guess[i])

        for i in new_guess:
            if i in new_secret:
                cows_counter += 1
                new_secret.remove(i)
        return f"{bull_counter}A{cows_counter}B"



print(Solution().getHint("1807", "7810"))
