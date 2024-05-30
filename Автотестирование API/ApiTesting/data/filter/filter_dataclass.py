from dataclasses import dataclass, field
@dataclass
class Filter:
    breeds: list = field(default_factory=lambda: [])
    categories: list = field(default_factory=lambda: [Category])
    id: int = 6
    url: str = "https://28.media.tumblr.com/tumblr_ks1a707b1b1qa9hjso1_1280.png"
    width: int = 507
    height: int = 375
    
@dataclass
class Category:
    id: int = 1
    name: str = "hats"