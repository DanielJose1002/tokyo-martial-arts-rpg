from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Move:
    name: str
    stamina_cost: int
    base_damage: int
    move_type: str  # 'strike', 'grapple', 'dirty'
    description: str = ""
    unlock_level: int = 1

class FightingStyle(ABC):
    def __init__(self):
        self.name = ""
        self.description = ""
        self.moves: List[Move] = []
        self.perks: Dict[str, Dict] = {}
        self.active_perks: List[str] = []
        
    @abstractmethod
    def calculate_damage_modifier(self, move: Move, target_style: Optional['FightingStyle']) -> float:
        pass
        
    def get_available_moves(self, player_level: int) -> List[Move]:
        return [move for move in self.moves if move.unlock_level <= player_level]

class Combatant:
    def __init__(self, name: str, fighting_style: FightingStyle):
        self.name = name
        self.style = fighting_style
        self.hp = 100
        self.max_hp = 100
        self.stamina = 100
        self.max_stamina = 100
        self.level = 1
        self.xp = 0
        
        # Stats
        self.strength = 5
        self.speed = 5
        self.technique = 5
        self.defense = 5
        
    def execute_move(self, move: Move, target: 'Combatant') -> int:
        if self.stamina < move.stamina_cost:
            return 0  # Not enough stamina
            
        self.stamina -= move.stamina_cost
        damage = self.style.calculate_damage(self, move, target)
        target.take_damage(damage)
        return damage
        
    def take_damage(self, amount: int):
        self.hp = max(0, self.hp - amount)
        
    def recover_stamina(self, amount: int):
        self.stamina = min(self.max_stamina, self.stamina + amount)
