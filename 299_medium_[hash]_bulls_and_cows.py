from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_character_to_count_map = defaultdict(int)

        bulls, cows = 0, 0
        for index, secret_character in enumerate(secret):
            guess_character = guess[index]
            if secret_character == guess_character:
                bulls += 1
            else:
                secret_character_to_count_map[secret_character] += 1

        i = 0
        while i < len(secret):
            secret_character, guess_character = secret[i], guess[i]
            if secret_character == guess_character:
                pass
            elif secret_character_to_count_map[guess_character] > 0:
                cows += 1
                secret_character_to_count_map[guess_character] -= 1

            i += 1

        return f'{bulls}A{cows}B'


if __name__ == '__main__':
    s = Solution()

    assert s.getHint("1807", "7810") == "1A3B"

    assert s.getHint("1123", "0111") == "1A1B"

    assert s.getHint("1", "0") == "0A0B"

    assert s.getHint("1", "1") == "1A0B"

    assert s.getHint("1122", "1222") == "3A0B"

