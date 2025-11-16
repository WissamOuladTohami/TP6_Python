from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float 

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)
    def est_classique(self):
        return self.annee < 2000
    
film1 = Film("Les Misérables", "Moi", 1980, 9.5)
film2 = Film("Agent 007", "Toi", 2000, 8.2)
film3 = Film("911", "Lui", 2005, 5.9)

print(film1.to_json()) 
print(film1.est_classique())   
print(film2.to_json()) 
print(film2.est_classique()) 
print(film3.to_json()) 
print(film3.est_classique()) 