from test_pcov import *

def test_example2_statement():
    output = run_pcov("examples/example2.py", "10", "1")
    cov, covered, total = get_coverage(STATEMENT_COV, output)
    assert covered == 6
    assert total == 8

def test_example2_branch():
    output = run_pcov("examples/example2.py", "10", "1")
    cov, covered, total = get_coverage(BRANCH_COV, output)
    assert covered == 2
    assert total == 4

def test_example2_condition():
    output = run_pcov("examples/example2.py", "10", "1")
    cov, covered, total = get_coverage(CONDITION_COV, output)
    assert covered == 3
    assert total == 6

def test_example2_verbose():
    output = run_pcov_verbose("examples/example2.py", "10", "1")
    lines = get_verbose_output(output)
    tuples = process_verbose_output(lines)

    should_contain_tuples = [
        (6, False),
        (8, True),
        (6, True),
        (6, False),
        (8, True)
    ]

    should_contain_lines = [
        "x == 10",
        "y == 1",
        "x == 10 and y == 5",
        "y == 5",
        "y == 1"
    ]

    assert sorted(tuples) == sorted(should_contain_tuples)
    assert check_required_line_contents(lines, should_contain_lines)