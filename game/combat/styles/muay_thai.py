from ..core import FightingStyle, Move

class MuayThaiStyle(FightingStyle):
    def __init__(self):
        super().__init__()
        self.name = "Muay Thai"
        self.description = "The art of eight limbs - brutal striking with knees and elbows"
        
        self.moves = [
            Move(name="Low Kick", stamina_cost=15, base_damage=12, move_type="strike"),
            Move(name="Knee Strike", stamina_cost=20, base_damage=18, move_type="strike"),
            Move(name="Elbow Strike", stamina_cost=18, base_damage=20, move_type="strike"),
            Move(name="Clinch", stamina_cost=25, base_damage=5, move_type="grapple", unlock_level=3),
            Move(name="Teep Push", stamina_cost=12, base_damage=8, move_type="strike", unlock_level=2)
        ]
        
        self.perks = {
            "iron_shins": {
                "description": "Kicks deal 20% more damage",
                "requirements": {"level": 2},
                "effect": {"kick_damage": 0.2}
            },
            "clinch_master": {
                "description": "Clinch drains opponent stamina",
                "requirements": {"level": 4},
                "effect": {"clinch_drain": 5}
            }
        }
        
    def calculate_damage_modifier(self, move: Move, target_style: FightingStyle) -> float:
        # Muay Thai is strong against other strikers
        if target_style and target_style.name in ["Boxing", "Karate"]:
            return 1.2
        return 1.0
