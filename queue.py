#!/usr/bin/python
from collections import deque
qu=deque()
qu.append(1)
qu.append(2)
while qu:
	tmp=qu.popleft()
	print tmp

