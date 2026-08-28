import re

class EntityFilter:
	# implements an entity filter following Home Assistant recorder's syntax
	def __init__(self, config):
		config = config or {}
		include = config.get('include', {}) or {}
		exclude = config.get('exclude', {}) or {}
		
		self.include_entities = set(include.get('entities', []))
		self.exclude_entities = set(exclude.get('entities', []))
		
		self.include_domains = set(include.get('domains', []))
		self.exclude_domains = set(exclude.get('domains', []))
		
		# regular expression arrays
		self.include_globs = [self._glob_to_regex(glob) for glob in include.get('entity_globs', [])]
		self.exclude_globs = [self._glob_to_regex(glob) for glob in exclude.get('entity_globs', [])]
		
		# inclusion/exclusion configuration blocks present
		self.has_includes = bool(self.include_entities or self.include_globs or self.include_domains)
		self.has_excludes = bool(self.exclude_entities or self.exclude_globs or self.exclude_domains)

	def _glob_to_regex(self, pattern: str) -> re.Pattern:
		'''Converts a HA glob expression string into a compiled Regex'''
		regex_str = re.escape(pattern).replace(r'\*', '.*')
		return re.compile(f'^{regex_str}$')

	def is_included(self, entity_id: str) -> bool:
		domain, _, _ = entity_id.partition('.')

		if not (self.has_includes or self.has_excludes):
			# no rules -> everything passes
			return True

		# precedence: entities over entity_globs over domains
		if entity_id in self.include_entities:
			return True
			
		if entity_id in self.exclude_entities:
			return False
			
		if any(pattern.match(entity_id) for pattern in self.include_globs):
			return True

		if any(pattern.match(entity_id) for pattern in self.exclude_globs):
			return False

		if domain in self.include_domains:
			return True

		if domain in self.exclude_domains:
			return False

		if self.include_globs or self.include_domains:
			# if we have includes, but entity didn't match any of them -> exclude it
			return False

		if self.exclude_globs or self.exclude_domains:
			# if we have only excludes, but entity didn't match any of them -> include it
			return True
			
		# there were rules, but entity didn't match any of them -> exclude it
		return False
