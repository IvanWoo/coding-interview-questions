# https://leetcode.com/problems/restore-ip-addresses/
"""
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]

Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
0 <= s.length <= 3000
s consists of digits only.
"""


def restore_ip_addresses(s: str) -> list[str]:
    n = len(s)
    ans = []

    def backtrack(p, path):
        if len(path) > 4:
            return
        if p >= n:
            if len(path) == 4:
                ans.append(".".join(path))
            else:
                return
        for i in range(3):
            if p + i <= n - 1:
                cur = s[p : p + i + 1]
                # leading zero
                if len(cur) >= 2 and cur[0] == "0":
                    continue
                if 0 <= int(cur) <= 255:
                    path.append(cur)
                    backtrack(p + i + 1, path)
                    path.pop()

    backtrack(0, [])
    return ans


def restore_ip_addresses(s: str) -> list[str]:
    def get_address(divisors):
        ip = []
        divisors = divisors + [len(s) - 1]
        for i in range(1, len(divisors)):
            a, b = divisors[i - 1], divisors[i]
            part = s[a + 1 : b + 1]
            ip.append(part)

        for part in ip:
            if len(part) > 1 and part.startswith("0"):
                return ""
            if int(part) > 255:
                return ""
        return ".".join(ip)

    def backtrack(divisors: list[int], cur_idx):
        n = len(divisors)
        if n == 4:
            print(divisors)
            ip = get_address(divisors)
            if ip:
                ans.append(ip)
            return
        for nxt in range(cur_idx, len(s) - 1):
            backtrack(divisors + [nxt], nxt + 1)

    ans = []
    backtrack([-1], 0)
    return ans
