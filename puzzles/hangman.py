# https://techdevguide.withgoogle.com/paths/foundational/hangman-challenge-archetypal/#!
import random
from collections import Counter
from dataclasses import dataclass, field
from functools import lru_cache
from typing import List


def get_look(word: str, guesses: List[str]) -> str:
    result = ""
    for c in word:
        result += c if c in guesses else "-"
    return result


@lru_cache(maxsize=1)
def load_words() -> list:
    with open("puzzles/data/words_alpha.txt", "r") as f:
        return [line.rstrip() for line in f]


def get_random_word() -> str:
    words = load_words()
    return words[random.randint(0, len(words))]


def search_word(word_len: int, guesses: list) -> str:
    guesses = [g.lower() for g in guesses]
    words = load_words()
    cs = [Counter(word) for word in words if len(word) == word_len]
    for c in cs:
        for char in guesses:
            c[char] = 0
    return (
        Counter("".join([c.most_common(1)[0][0] for c in cs]))
        .most_common(1)[0][0]
        .upper()
    )


@dataclass
class HangMan:
    word: str
    guesses: list = field(default_factory=list)
    counter: int = 0
    max_counter: int = 8
    is_success: bool = False


def main():
    hm = HangMan(word=get_random_word().upper())
    while hm.counter <= hm.max_counter:
        print("Welcom to Hangman!")
        look = get_look(hm.word, hm.guesses)
        print(f"The word now looks like this: {look}")
        if look == hm.word:
            hm.is_success = True
            break

        print(f"The most possible guessing is: {search_word(len(hm.word), hm.guesses)}")

        print(f"You have {hm.max_counter - hm.counter} guesses left.")
        g = input("Your guess: ").upper()
        print(g)
        hm.guesses.append(g)
        hm.counter += 1 if g not in hm.word else 0
    if hm.is_success:
        print(f"You guessed the word: {hm.word}")
        print("You win.")
    else:
        print(f"The word was: {hm.word}")
        print("You lose.")


if __name__ == "__main__":
    main()
