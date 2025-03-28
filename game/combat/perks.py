from typing import Dict, Any

class PerkSystem:
    def __init__(self):
        self.available_perks: Dict[str, Dict] = {}
        
    def load_perks(self, styles: Dict[str, Dict]):
        """Load all perks from fighting styles"""
        for style_name, style_data in styles.items():
            self.available_perks[style_name] = style_data.perks
            
    def can_unlock_perk(self, player, style_name: str, perk_name: str) -> bool:
        """Check if player meets perk requirements"""
        perk = self.available_perks[style_name][perk_name]
        
        # Check level requirement
        if player.level < perk["requirements"].get("level", 0):
            return False
            
        # Check perk dependencies
        for required_perk in perk["requirements"].get("perks", []):
            if required_perk not in player.active_perks:
                return False
                
        return True
        
    def apply_perk(self, player, perk_name: str, perk_data: Dict[str, Any]):
        """Apply perk effects to player"""
        player.active_perks.append(perk_name)
        
        # Apply stat modifications
        for stat, value in perk_data["effect"].items():
            if hasattr(player, stat):
                current = getattr(player, stat)
                setattr(player, stat, current + value)
