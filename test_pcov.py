import subprocess
import re
import json
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

def run_covpy(target, *args):
	cmd = ["python3", "-m", "coverage", "erase"]
	subprocess.run(cmd, capture_output=True, text=True)

	cmd = ["python3", "-m", "coverage", "run", "--branch", target] + list(args)
	ret = subprocess.run(cmd, capture_output=True, text=True)

	cmd = ["python3", "-m", "coverage", "json"]
	ret = subprocess.run(cmd, capture_output=True, text=True)
	
	cov = json.load(open("coverage.json", "r"))
	stmt_covered = cov["files"][target]["summary"]["covered_lines"]
	stmt_total = cov["files"][target]["summary"]["num_statements"]
	stmt_missing = cov["files"][target]["missing_lines"]

	branch_covered = cov["files"][target]["summary"]["covered_branches"]
	branch_total = cov["files"][target]["summary"]["num_branches"]
	branch_missing = ["{}->{}".format(x[0], x[1]) for x in cov["files"][target]["missing_branches"]]

	return stmt_covered, stmt_total, stmt_missing, branch_covered, branch_total, branch_missing