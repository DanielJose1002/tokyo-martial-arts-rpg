import random

# Player & Enemy Stats
player = {
    "name": "You",
    "hp": 100,
    "max_hp": 100,
    "stamina": 100,
    "max_stamina": 100,
    "strength": 10,
    "defense": 5,
}

enemy = {
    "name": "School Bully",
    "hp": 80,
    "max_hp": 80,
    "stamina": 80,
    "max_stamina": 80,
    "strength": 8,
    "defense": 4,
}

# Moves
moves = {
    "1": {"name": "Jab", "damage": 10, "stamina_cost": 10, "type": "quick"},
    "2": {"name": "Roundhouse Kick", "damage": 25, "stamina_cost": 25, "type": "power"},
    "3": {"name": "Block", "damage": 0, "stamina_cost": 5, "type": "defense"},
}

def display_health_bars(player, enemy):
    """Show HP/Stamina bars."""
    def bar(current, max_val, length=20):
        filled = int((current / max_val) * length)
        return '█' * filled + '░' * (length - filled)
    
    print(f"\n[{player['name']}]")
    print(f"HP: {bar(player['hp'], player['max_hp'])} ({player['hp']}/{player['max_hp']})")
    print(f"Stamina: {bar(player['stamina'], player['max_stamina'])} ({player['stamina']}/{player['max_stamina']})")
    
    print(f"\n[{enemy['name']}]")
    print(f"HP: {bar(enemy['hp'], enemy['max_hp'])} ({enemy['hp']}/{enemy['max_hp']})")
    print(f"Stamina: {bar(enemy['stamina'], enemy['max_stamina'])} ({enemy['stamina']}/{enemy['max_stamina']})")

def player_turn(player, enemy):
    """Player's attack choice."""
    print("\nChoose your move:")
    for key, move in moves.items():
        print(f"{key}. {move['name']} (DMG: {move['damage']}, STAMINA: {move['stamina_cost']})")
    
    while True:
        choice = input("> ")
        if choice in moves:
            move = moves[choice]
            if player["stamina"] >= move["stamina_cost"]:
                player["stamina"] -= move["stamina_cost"]
                return move
            else:
                print("Not enough stamina!")
        else:
            print("Invalid choice!")

def enemy_turn(enemy, player):
    """Simple AI: Randomly picks a move."""
    move = random.choice(list(moves.values()))
    if enemy["stamina"] >= move["stamina_cost"]:
        enemy["stamina"] -= move["stamina_cost"]
        return move
    else:
        return {"name": "Rest", "damage": 0, "stamina_cost": 0}  # Enemy recovers stamina if too low

def apply_damage(attacker, defender, move):
    """Calculate damage."""
    if move["type"] == "defense":
        print(f"{attacker['name']} braces for impact!")
        return
    
    damage = max(0, move["damage"] + attacker["strength"] - defender["defense"])
    defender["hp"] -= damage
    print(f"{attacker['name']} uses {move['name']}! ({damage} damage)")

def combat_loop(player, enemy):
    """Main combat loop."""
    print(f"\n⚔️ A fight breaks out with {enemy['name']}! ⚔️")
    
    while player["hp"] > 0 and enemy["hp"] > 0:
        display_health_bars(player, enemy)
        
        # Player turn
        player_move = player_turn(player, enemy)
        apply_damage(player, enemy, player_move)
        if enemy["hp"] <= 0:
            break
        
        # Enemy turn
        enemy_move = enemy_turn(enemy, player)
        apply_damage(enemy, player, enemy_move)
        if player["hp"] <= 0:
            break
        
        # Recover some stamina each turn
        player["stamina"] = min(player["stamina"] + 5, player["max_stamina"])
        enemy["stamina"] = min(enemy["stamina"] + 5, enemy["max_stamina"])
    
    # Result
    display_health_bars(player, enemy)
    if player["hp"] > 0:
        print(f"\n🎉 You defeated {enemy['name']}!")
    else:
        print("\n💀 You were knocked out...")

# Start the fight!
combat_loop(player, enemy)
