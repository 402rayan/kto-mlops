from typing import List

class NameAnalyzer:
    def __init__(self, names: List[str]):
        self.names = names

    def count_names_too_long(self, max_length: int = 7, verbose:bool = False) -> int:
        """Return an integer, the length of words that are longer than {max_length} characters"""
        long_names = [name for name in self.names if len(name) > max_length]

        for name in self.names:
            comparison = "supérieur" if len(name) > max_length else "inférieur ou égal"
            print(f"{name} est un prénom avec un nombre de lettres {comparison} à {max_length}") if verbose else None

        return len(long_names)