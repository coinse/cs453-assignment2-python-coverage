import ast
import argparse
import sys
from copy import deepcopy
import test_pcov

def print_result(verbose:bool, stmt_covered:int, stmt_total:int, stmt_missing:list[str], branch_covered:int, branch_total:int, branch_missing:list[str]):
	
	stmt_coverage = 0 if stmt_total == 0 else stmt_covered / stmt_total * 100
	branch_coverage = 0 if branch_total == 0 else branch_covered / branch_total * 100

	print("=====================================")
	print("Statement Coverage: {0:.2f} ({1}/{2})".format(stmt_coverage, stmt_covered, stmt_total))
	if verbose:
		print("Missing Statements: {}".format(", ".join([str(line_num) for line_num in stmt_missing])))
	print("=====================================")
	print("Branch Coverage: {0:.2f} ({1}/{2})".format(branch_coverage, branch_covered, branch_total))
	if verbose:
		print("Missing Branches: {}".format(", ".join([str(line_num) for line_num in branch_missing])))
	print("=====================================")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Measures coverage.')
	parser.add_argument('-v', '--verbose', action="store_true")
	parser.add_argument('-t', '--target', required=True)
	parser.add_argument("remaining", nargs="*")
	args = parser.parse_args()

	target = args.target
	lines = open(target, "r").readlines()
	root = ast.parse("".join(lines), target)
	
	
	# instrument the target script
	# ...

	# execute the instrumented target script 
	# ...

	# collect coverage
	# ...

	print_result(args.verbose, stmt_covered, stmt_total, stmt_missing, branch_covered, branch_total, branch_missing)