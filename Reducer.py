#!/usr/bin/env python

import sys

reason_last = None
reason_count = 0

for line in sys.stdin:
	reason, count = line.strip().split("\t")
	count = int(count)

	if not reason_last:
		reason_last = str(reason)

	if reason == reason_last:
		reason_count = reason_count + count
	else:
		result = [reason_last, reason_count]
		print("\t".join(str(i) for i in result))
		reason_last = str(reason)
		reason_count = 1

print("\t".join(str(i) for i in [reason_last, reason_count]))
