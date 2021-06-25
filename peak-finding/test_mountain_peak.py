import mountain_peak


def test_solution():
    cases = [
        ([0,1,0], 1),
        ([0,2,1,0], 1),
        ([0,10,5,2], 1),
        ([3,4,5,1], 2),
        ([24,69,100,99,79,78,67,36,26,19], 2)
    ]

    for case, sol in cases:
        assert mountain_peak.solution(case) == sol
