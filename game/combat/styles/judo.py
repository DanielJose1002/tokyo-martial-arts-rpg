from ..core import FightingStyle, Move

class JudoStyle(FightingStyle):
    def __init__(self):
        super().__init__()
        self.name = "Judo"
        self.description = "The gentle way - using opponent's strength against them"
        
        self.moves = [
            Move(name="Hip Throw", stamina_cost=20, base_damage=15, move_type="grapple"),
            Move(name="Foot Sweep", stamina_cost=15, base_damage=10, move_type="grapple"),
            Move(name="Armbar", stamina_cost=25, base_damage=30, move_type="grapple", unlock_level=3),
            Move(name="Defensive Posture", stamina_cost=10, base_damage=0, move_type="defense"),
            Move(name="Sacrifice Throw", stamina_cost=30, base_damage=25, move_type="grapple", unlock_level=5)
        ]
        
        self.perks = {
            "breakfall": {
                "description": "Take 20% less damage when thrown",
                "requirements": {"level": 2},
                "effect": {"throw_resist": 0.2}
            },
            "transition_master": {
                "description": "Chain throws together for 15% more damage",
                "requirements": {"level": 4},
                "effect": {"chain_bonus": 0.15}
            }
        }
        
    def calculate_damage_modifier(self, move: Move, target_style: FightingStyle) -> float:
        # Judo is strong against strikers, weak against dirty fighters
        if target_style and target_style.name == "Street Fighting":
            return 0.8
        if target_style and target_style.name in ["Boxing", "Muay Thai"]:
            return 1.3
        return 1.0
