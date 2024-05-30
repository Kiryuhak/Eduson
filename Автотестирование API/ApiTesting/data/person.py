from dataclasses import dataclass, field

name: str = "Viktor"	
age: int = 30
married: bool = False
childrens: list = []

@dataclass
class Person:
	name: str = "Viktor"	
	age: int = 30
	married: bool = False
	childrens: list = field(default_factory=lambda: [])