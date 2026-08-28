def try_float(value) -> float | None:
	# tries to convert a value to a float (just a wrapper to avoid try...except blocks in code)
	try:
		return float(value)
	except (ValueError, TypeError):
		return None
