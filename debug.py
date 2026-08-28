def __LINE__() -> int | None:
	# returns the current line number, use like f'{__LINE__()}'
	from inspect import currentframe
	return currentframe().f_back.f_lineno
