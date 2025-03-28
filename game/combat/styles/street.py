from ..core import FightingStyle, Move

class StreetFightingStyle(FightingStyle):
    def __init__(self):
        super().__init__()
        self.name = "Street Fighting"
        self.description = "No rules, no mercy - whatever it takes to win"
        
        self.moves = [
            Move(name="Eye Poke", stamina_cost=5, base_damage=5, move_type="dirty"),
            Move(name="Groin Kick", stamina_cost=15, base_damage=20, move_type="dirty"),
            Move(name="Headbutt", stamina_cost=10, base_damage=12, move_type="dirty"),
            Move(name="Bottle Smash", stamina_cost=20, base_damage=25, move_type="dirty", unlock_level=3),
            Move(name="Taunt", stamina_cost=5, base_damage=0, move_type="mental", unlock_level=2)
        ]
        
        self.perks = {
            "dirty_tricks": {
                "description": "Dirty moves have 25% chance to stun",
                "requirements": {"level": 2},
                "effect": {"stun_chance": 0.25}
            },
            "intimidation": {
                "description": "Taunts reduce opponent attack by 15%",
                "requirements": {"level": 4},
                "effect": {"taunt_effect": 0.15}
            }
        }
        
    def calculate_damage_modifier(self, move: Move, target_style: FightingStyle) -> float:
        # Street fighting is unpredictable
        if target_style and target_style.name == "Karate":
            return 1.1
        return 1.0
