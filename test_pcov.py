import subprocess
import re
from distutils.util import strtobool

STATEMENT_COV = "Statement"
BRANCH_COV = "Branch"
CONDITION_COV = "Condition"

cov_re = re.compile(r'(\d+\.\d+)% \((\d+) / (\d+)\)')

def run_pcov(target, *args):
	cmd = ["python3", "pcov.py", "-t", target] + list(args)
	ret = subprocess.run(cmd, capture_output=True, text=True)
	return ret.stdout

def run_pcov_verbose(target, *args):
	cmd = ["python3", "pcov.py", "-v", "-t", target] + list(args)
	ret = subprocess.run(cmd, capture_output=True, text=True)
	return ret.stdout

def get_coverage(cov_type, output):
	_line = list(filter(lambda x: x.startswith(cov_type), output.split("\n")))[0]
	match = cov_re.search(_line)
	if match:
		return float(match.group(1)), int(match.group(2)), int(match.group(3))
	else:
		return 0, 0, 0

def get_verbose_output(output):
	_lines = list(filter(lambda x: x.startswith("Line"), output.split("\n")))
	return _lines

def process_verbose_output(lines):
	return [(int(x.split(":")[0].split(" ")[1]), bool(strtobool(x.split("==>")[1].strip()))) for x in lines]

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
	assert tuples[0] == (3, True)
	assert tuples[1] == (3, True)	

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
	
	assert (6, False) == tuples[0]
	assert (8, True) == tuples[1]
	assert (6, True) == tuples[2]
	assert (6, False) == tuples[3]
	assert (8, True) == tuples[4]
	
	assert lines[0].find("x == 10 and y == 5") > 0
	assert lines[1].find("y == 1") > 0
	assert lines[2].find("x == 10") > 0
	assert lines[3].find("y == 5") > 0
	assert lines[4].find("y == ") > 0

def test_example3_1_branch():
	output = run_pcov("examples/example3.py", "1")
	cov, covered, total = get_coverage(BRANCH_COV, output)
	assert covered == 3
	assert total == 4

def test_example3_1_condition():
	output = run_pcov("examples/example3.py", "1")
	cov, covered, total = get_coverage(CONDITION_COV, output)
	assert covered == 1
	assert total == 2

def test_example3_2_branch():
	output = run_pcov("examples/example3.py", "2")
	cov, covered, total = get_coverage(BRANCH_COV, output)
	assert covered == 4
	assert total == 4

def test_example3_2_condition():
	output = run_pcov("examples/example3.py", "2")
	cov, covered, total = get_coverage(CONDITION_COV, output)
	assert covered == 2
	assert total == 2



