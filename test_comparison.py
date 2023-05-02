from test_pcov import *

def test_example1_statement():
    output = run_pcov("examples/example1.py")
    cov, covered, total = get_coverage(STATEMENT_COV, output)
    assert cov == 100.00
    assert covered == 3
    assert total == 3

def test_example1_branch():
    output = run_pcov("examples/example1.py")
    cov, covered, total = get_coverage(BRANCH_COV, output)
    assert cov == 50.00
    assert covered == 1
    assert total == 2

def test_example1_verbose():
    output = run_pcov_verbose("examples/example1.py")
    lines = get_verbose_output(output)
    tuples = process_verbose_output(lines)

    should_contain_tuples = [
        (3, True),
        (3, True)
    ]
    assert sorted(tuples) == sorted(should_contain_tuples)