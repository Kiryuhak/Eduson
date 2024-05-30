from dataclasses import dataclass

@dataclass
class Source:
	id: int = 1
	name: str = "Wikipedia"
	url: str = "https://en.wikipedia.org"
	breed_id: int = None