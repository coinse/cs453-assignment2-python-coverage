import ast
import argparse
import sys
from copy import deepcopy
import test_pcov

def save_result(target, verbose:bool, stmt_covered:int, stmt_total:int, stmt_missing:list[str], branch_covered:int, branch_total:int, branch_missing:list[str]):
	#Please satisfy the type of each parameters
	result_path = "./pcov.json"
	stmt_coverage = 0 if stmt_total == 0 else stmt_covered / stmt_total * 100
	branch_coverage = 0 if branch_total == 0 else branch_covered / branch_total * 100

	result = {}
	result["target_file"] = target
	result["covered_lines"] = stmt_covered
	result["num_statements"] = stmt_total
	result["statement_coverage"] = format(stmt_coverage, ".2f")
	if verbose:
		result["missing_lines"] = stmt_missing
	
	result["covered_branches"] = branch_covered
	result["num_branches"] = branch_total
	result["branch_coverage"] = format(branch_coverage, ".2f")
	if verbose:
		result["missing_branches"] = branch_missing

	with open(result_path, 'w') as f:
		json.dump(result, f, indent=4)

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

	save_result(target, args.verbose, stmt_covered, stmt_total, stmt_missing, branch_covered, branch_total, branch_missing)