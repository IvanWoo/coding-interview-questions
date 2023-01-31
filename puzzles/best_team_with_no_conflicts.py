# https://leetcode.com/problems/best-team-with-no-conflicts/description/
"""
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

Example 1:
Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.

Example 2:
Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

Example 3:
Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players.

Constraints:
1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 106
1 <= ages[i] <= 1000
"""
from dataclasses import dataclass


@dataclass
class Player:
    score: int
    age: int


# brute force: TLE
def best_team_score(scores: list[int], ages: list[int]) -> int:
    def sum_score(team):
        return sum([p.score for p in team])

    def helper(idx, age, team):
        if idx == n:
            return sum_score(team)
        cur = players[idx]
        return max(
            [
                helper(idx + 1, age, team),
                helper(
                    idx + 1,
                    cur.age,
                    [
                        p
                        for p in team
                        if (p.age < cur.age and p.score <= cur.score)
                        or p.age == cur.age
                    ]
                    + [cur],
                ),
            ]
        )

    players = [Player(score, age) for score, age in zip(scores, ages)]
    players.sort(key=lambda p: p.age)
    n = len(scores)
    return helper(0, 0, [])


def best_team_score(scores: list[int], ages: list[int]) -> int:
    dp = [0] * (1 + max(ages))
    score_age = sorted(zip(scores, ages))
    for score, age in score_age:
        dp[age] = score + max(dp[: age + 1])
    return max(dp)


def best_team_score(scores: list[int], ages: list[int]) -> int:
    age_score = sorted(zip(ages, scores))
    n = len(scores)
    dp = [0] * n
    for i in range(n):
        cur_score = age_score[i][1]
        dp[i] = cur_score
        for j in range(i):
            if age_score[j][1] <= cur_score:
                dp[i] = max(dp[i], dp[j] + cur_score)
    return max(dp)
