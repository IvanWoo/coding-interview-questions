# https://wentao-shao.gitbook.io/leetcode/toposort/1136.parallel-courses
"""
There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

Example 1:
Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.

Example 2:
Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.

Note:
1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.
"""

# backtracking
def has_cycle(graph, i, visited):
    visited[i] = True
    for j in graph[i]:
        if visited[j]:
            return True
        if has_cycle(graph, j, visited):
            return True
    visited[i] = False
    return False


def dfs(u, graph, cache):
    if cache[u] != -1:
        return cache[u]
    res = 0
    for v in graph[u]:
        res = max(res, dfs(v, graph, cache) + 1)
    cache[u] = res
    return res


def parallel_courses(n, relations):
    graph = [[] for _ in range(n + 1)]
    for u, v in relations:
        graph[u].append(v)

    visited = [False] * (n + 1)
    # detect cycle
    for i in range(1, n + 1):
        if has_cycle(graph, i, visited):
            return -1

    cache = [-1 for _ in range(n + 1)]
    res = 0
    for u in range(1, n + 1):
        res = max(res, dfs(u, graph, cache))
    return res + 1
