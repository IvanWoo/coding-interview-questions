def double_substring(line):
    """
    lenght of the longest substring that non-overlapping repeats more than once
    :param line:
    :return:
    """
    ruler = len(line) // 2
    for i in range(ruler, 0, -1):
        for j in range(len(line) - ruler + 1):
            atom = line[j : (j + i)]
            if line.count(atom) > 1:
                return len(atom)
    return 0


if __name__ == "__main__":
    print(double_substring("aaaa") == 2)
    print(double_substring("abc") == 0)
    print(double_substring("aghtfghkofgh") == 3)
    print('"Run" is good. How is "Check"?')
