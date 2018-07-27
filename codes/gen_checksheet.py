#!/usr/bin/env python

# gen_checksheet.py ver. 0.1
# Usage: Type "./gen_checksheet.py -h" in project root directory.

import argparse
import re

parser = argparse.ArgumentParser(usage = './gen_checksheet.py <notes>')
parser.add_argument('notes', metavar = 'notes <STRING>', type = str, help = 'path to notes')
args = parser.parse_args()

# Targets
R1 = re.compile(r"\*{2}.+\*{2}")


def pick_highlights(line):
	target = re.findall(R1, line)
	if len(target) > 0:
		# Reomve **
		answer = target
		question = re.sub(R1, "(     )", line.decode("utf-8")).strip().replace('*','').encode("utf-8")
		return {'type':1, 'q':question,'a':answer}
	else:
		return None


# Display QAs
def display_qa(qa_dict):
	for key in qa_dict.keys():
		print("Q"+str(key)+": ")
		print(qa_dict[key]['q'])
		print("A"+str(key)+": ")
		for ans in qa_dict[key]['a']:
			print(ans.replace('*',''))


if __name__ == '__main__':
	with open(args.notes, "rt") as f:
		notes = f.readlines()

	qs = {}
	num = 0
	# print('lines: ',len(notes))
	for n, line in enumerate(notes):
		result = pick_highlights(line)
		if result is not None:
			num += 1
			result.update({'line':n})
			qs.update({num: result})

	display_qa(qs)