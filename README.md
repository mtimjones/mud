# mud
MUD Development Hackathon

# Introduction

Submission for the "MUD in a month" hackathon, October 2024.

# Theme

A MUD set in a cyberpunk universe.  The world is set in a small dystopian city of neon streets, dark alleys, small apartment complexes, drug dens, and other notable locations.  While the city serves as home to its residents, it's also a prison that enforces their presence.  The player must navigate the small city in search of a cyberware dealer in order to infiltrate (both physically and virtually) a mainframe that will allow him to exit the city.  The player will engage and eliminate threats that block his path.

# Currency

The main currency of this world is bitcoin which can be used to buy and sell items.  Bitcoin is attained by killing enemies as well as finding througout the city.  A simple hacking minigame is also present in some locations as a puzzle element.

The other secondary currency is parts, which can be found on defeated enemies.  Parts can be sold for Bitcoin or used in crafting. [Stretch]

# Stats

Entity stats include:

 - Attack
 - Defense
 - Intelligence

# Leveling System

The stats structure for an entity defines the level, HP, and when to increase the entity's level via experience points (xp).

When xp is to be added to the entity, it is added to stats.xp, and then stats.xp is checked against the stats.next_lvl.  If stats.xp >= stats.next_lvl, then the following occurs:

    level++
    stats.xp = stats.xp - stats.next_lvl
    stats.hp += stats.base_hp * (1.0 - stats.factor)
    stats.next_lvl = stats.next_lvl + 
                        (stats.next_lvl * stats.factor)


# Enemies

- Drone, attack 2, defense 2, yields parts.
- Sentry, attack 1, defense 3, yields parts.
- Turret, attack 4, defense 2, yields parts.
...

# Combat/Armor/Equations


# Task List

- [x] Implement the multi-threaded socket server.
- [x] Implement the client socket handler.
- [ ] Define stats and their benefits.
- [x] Define game currency (bitcoin).
- [x] Define MUD theme (cyberpunk) and some lore.
- [ ] Define the enemies in the world and their stats.
- [ ] Define attack/armor/defense and equations.
- [ ] Implement new character creation.
- [x] Implement single room JSON (entry, safe).

- [x] Implement the 'look' command.
- [x] Implement the 'inventory' command.
- [ ] Implement the 'examine' command.
- [ ] Implement the 'wield' command.
- [ ] Implement the 'unwield' command.
- [ ] Implement the 'take' command.
- [ ] Implement combat and the 'attack' command.
- [ ] Implement hacking and the 'hack' command.
- [ ] Implement the 'use' command.
- [ ] Implement the 'buy' command.
- [ ] Implement the 'sell' command.
- [ ] Implement the 'drop' command.
- [ ] Implement the 'give' command.

- [x] Design the leveling system.
- [ ] Implement multi-room JSON.
- [ ] Implement movement commands.
- [ ] Implement item creation and dimension loading.
- [ ] Implement weapons and stats.
- [ ] Implement enemies.

- [ ] Implement symstick (health).
- [ ] Implement traps in the dimension.
- [ ] Implement puzzles.
- [ ] Implement merchants (buy/sell and currency).

- [ ] Implement mobs.
- [ ] Implement the final hand-crafted map.

# Stretch Goals

- [ ] Implement the 'throw' command.
- [ ] Implement potential NPC/LLM.
- [ ] Cyberware or implants.
- [ ] Implement crafting and a crafting tree.
