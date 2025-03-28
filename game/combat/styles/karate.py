from ..core import FightingStyle, Move

class KarateStyle(FightingStyle):
    def __init__(self):
        super().__init__()
        self.name = "Karate"
        self.description = "Traditional striking with disciplined technique"
        
        self.moves = [
            Move(name="Reverse Punch", stamina_cost=12, base_damage=10, move_type="strike"),
            Move(name="Front Kick", stamina_cost=15, base_damage=12, move_type="strike"),
            Move(name="Knifehand Strike", stamina_cost=18, base_damage=15, move_type="strike"),
            Move(name="Kata Stance", stamina_cost=10, base_damage=0, move_type="defense", unlock_level=3),
            Move(name="Spinning Back Kick", stamina_cost=25, base_damage=22, move_type="strike", unlock_level=5)
        ]
        
        self.perks = {
            "kime": {
                "description": "Critical hits deal 25% more damage",
                "requirements": {"level": 2},
                "effect": {"crit_damage": 0.25}
            },
            "kata_master": {
                "description": "Stance increases defense by 20%",
                "requirements": {"level": 4},
                "effect": {"stance_defense": 0.2}
            }
        }
        
    def calculate_damage_modifier(self, move: Move, target_style: FightingStyle) -> float:
        # Karate is balanced with slight advantage against dirty fighters
        if target_style and target_style.name == "Street Fighting":
            return 1.2
        return 1.0
