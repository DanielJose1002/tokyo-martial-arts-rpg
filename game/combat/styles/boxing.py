from ..core import FightingStyle, Move

class BoxingStyle(FightingStyle):
    def __init__(self):
        super().__init__()
        self.name = "Boxing"
        self.description = "The sweet science of hitting without getting hit"
        
        self.moves = [
            Move(name="Jab", stamina_cost=10, base_damage=8, move_type="strike"),
            Move(name="Cross", stamina_cost=15, base_damage=12, move_type="strike"),
            Move(name="Hook", stamina_cost=20, base_damage=18, move_type="strike"),
            Move(name="Uppercut", stamina_cost=25, base_damage=22, move_type="strike", unlock_level=3),
            Move(name="Dodge Roll", stamina_cost=12, base_damage=0, move_type="defense", unlock_level=2)
        ]
        
        self.perks = {
            "fast_footwork": {
                "description": "Increase dodge chance by 15%",
                "requirements": {"level": 2},
                "effect": {"dodge_chance": 0.15}
            },
            "combo_master": {
                "description": "Chained attacks deal 10% more damage",
                "requirements": {"level": 4, "perks": ["fast_footwork"]},
                "effect": {"combo_damage": 0.1}
            }
        }
        
    def calculate_damage_modifier(self, move: Move, target_style: FightingStyle) -> float:
        # Boxing is strong against striking styles, weak against grapplers
        if target_style and target_style.name == "Judo":
            return 0.8
        return 1.0
