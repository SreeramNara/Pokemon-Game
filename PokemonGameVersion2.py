import random
import time

# new pokemon = hp, moveset(new move), type, evolutions, pokemon1/pokemon2/pokemon3, rarity
# new move = attackpower, type, pokemon moveset
# new type = type advantage, non type advantage, move changes, pokemon changes

starterpokemon1 = ["Charmander", "Squirtle", "Bulbasaur"]
starterpokemon2 = ["Charmeleon", "Wartortle", "Ivysaur"]
starterpokemon3 = ["Charizard", "Blastoise", "Venusaur"]

easycatch = ["Yes", "No", "Yes", "No", "Yes"]

hardcatch = ["No", "Yes", "No", "yes", "No", "No"]

pokemonrarity = ['Rare', "Rare", "Common", "Common", "Common", "Common", "Common", "Uncommon", "Uncommon", "Uncommon", "Very Rare", "Common", "Common", "Uncommon", "Very Rare", "Rare", "Super Rare"]

commongroundpokemon = ["Caterpie", "Rattata", "Pidgey", "Weedle", "Geodude"]
uncommongroundpokemon = ["Oddish", "Zubat", "Nidoran Male", "Nidoran Female", "Koffing", "Diglett"]
raregroundpokemon = ["Rhyhorn", "Machop", "Pichu", "Voltorb", "Bellsprout", "Grimer", "Venonat"]
veryraregroundpokemon = ["Ponyta", "Jigglypuff", "Onix", "Growlithe", "Tangela"]
superraregroundpokemon = ["Abra", "Vulpix", "Mime Junior"]

commonwaterpokemon = ["Magikarp"]
uncommonwaterpokemon = ["Krabby", "Tentacool"]
rarewaterpokemon = ["Seel", "Psyduck", "Shellder"]
veryrarewaterpokemon = ["Staryu", "Gyarados"]
superrarewaterpokemon = ["Lapras"]

gympokemon = {"Brock":["Geodude", "Onix"], "Misty":["Staryu", "Starmie"], "Lt. Surge":["Voltorb", "Pikachu", "Raichu"], "Erika":["Victreebel", "Tangela", "Vileplume"], "Koga":["Koffing", "Muk", "Weezing"], "Sabrina":["Kadabra", "Mr. Mime", "Venomoth", "Alakazam"], "Blaine":["Ponyta", "Rapidash", "Growlithe", "Arcanine"], "Giovanni":["Rhyhorn", "Dugtrio", "Nidoqueen", "Nidoking"]}

gymleaders = ["Brock", "Misty", "Lt. Surge", "Erika", "Koga", "Sabrina", "Blaine", "Giovanni"]

pokemonleaguetrainers = {"James", "Ethan", "Kevin", "Holt", "Ray", "Gray"}

leaguepokemon = {"James":["Butterfree", "Vileplume", "Arcanine"], "Ethan":["Graveller", "Koffing", "Lapras"], "Kevin":["Onix", "Beedrill", "Rhyperior"], "Holt":["Rapidash", "Electrode", "Victreebel"], "Ray":["Muk", "Crobat", "Dugtrio", "Raticate", "Tangrowth", "Venusaur"], "Gray":["Raichu", "Tentacruel", "Ninetales", "Nidoking", "Alakazam", "Blastoise"]}

gymbadges = {"Brock":"Boulder Badge", "Misty":"Cascade Badge", "Lt. Surge":"Thunder Badge", "Erika":"Rainbow Badge", "Koga":"Soul Badge", "Sabrina":"Marsh Badge", "Blaine":"Volcano Badge", "Giovanni":"Earth Badge"}

pokemon1 = ["Caterpie", "Rattata", "Pidgey", "Weedle", "Oddish", "Zubat", "Nidoran Male", "Nidoran Female", "Rhyhorn", "Ponyta", "Vulpix", "Jigglypuff", "Onix", "Machop", "Tentacool", "Staryu", "Growlithe", "Pichu", "Geodude", "Lapras", "Voltorb", "Bellsprout", "Tangela", "Koffing", "Grimer", "Abra", "Mime Junior", "Venonat", "Diglett", "Magikarp", "Krabby", "Seel", "Psyduck", "Shellder"]
pokemon2 = ["Metapod", "Raticate", "Pidgeotto", "Kakuna", "Gloom", "Golbat", "Nidorino", "Nidorina", "Rhydon", "Rapidash", "Ninetales", "Wigglytuff", "Machoke", "Tentacruel", "Starmie", "Arcanine", "Pikachu", "Graveler", "Electrode", "Weepinbell", "Tangrowth", "Weezing", "Muk", "Kadabra", "Mr. Mime", "Venomoth", "Dugtrio", "Gyarados", "Kingler", "Dewgong", "Golduck", "Cloyster"]
pokemon3 = ["Butterfree", "Pidgeot", "Beedrill", "Vileplume", "Crobat", "Rhyperior", "Machamp", "Golem", "Raichu", "Nidoqueen", "Nidoking", "Victreebel", "Alakazam"]


typeadvantages = {"Fire":["Grass", "Bug", "Ice"], "Grass":["Water", "Ground", "Rock"], "Water":["Fire", "Ground", "Rock"], "Ground":["Fire", "Electric", "Poison", "Rock"], "Bug":["Grass", "Psychic"], "Rock":["Fire", "Flying", "Bug", "Ice"], "Flying":["Grass", "Fighting", "Bug"], "Normal":[], "Fairy":["Fighting"], "Fighting":["Normal", "Rock", "Ice"], "Poison":["Fairy", "Grass"], "Electric":["Flying", "Water"], "Ice":["Grass", "Ground", "Flying"], "Psychic":["Fighting", "Poison"]}

noadvantagetypes = {"Fire":["Fire", "Normal", "Electric", "Fighting", "Poison", "Ground", "Flying", "Fairy", "Psychic"], "Grass":["Grass", "Normal", "Electric", "Fighting", "Fairy", "Ice", "Psychic"], "Water":["Water", "Normal", "Electric", "Fighting", "Poison", "Flying", "Bug", "Ice", "Psychic"], "Ground":["Ground", "Normal", "Water", "Fighting", "Ground", "Fairy", "Ice", "Psychic"], "Bug":["Bug", "Normal", "Water", "Electric", "Ground", "Bug", "Rock", "Ice"], "Rock":["Rock", "Normal", "Water", "Electric", "Grass", "Poison", "Rock", "Fairy", "Psychic"], "Flying":["Flying", "Normal", "Fire", "Water", "Poison", "Ground", "Flying", "Fairy", "Psychic"], "Normal":["Normal", "Fire", "Water", "Grass", "Electric", "Poison", "Ground", "Fairy", "Flying", "Bug", "Rock", "Ice", "Psychic"], "Fairy":["Fairy", "Normal", "Water", "Electric", "Grass", "Ground", "Flying", "Bug", "Rock", "Fairy", "Ice", "Psychic"], "Fighting":["Fighting", "Fire", "Water", "Electric", "Grass", "Fighting", "Ground"], "Poison":["Poison", "Normal", "Fire", "Water", "Electric", "Fighting", "Flying", "Bug", "Ice"], "Electric":["Electric", "Fire", "Normal", "Fighting", "Poison", "Bug", "Rock", "Fairy", "Ice", "Psychic"], "Ice":["Ice", "Normal", "Electric", "Fighting", "Poison", "Bug", "Rock", "Fairy", "Psychic"], "Psychic":["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Ground", "Flying", "Bug", "Rock", "Fairy"]}

pokemonmoves = {"Charmander":["Tackle", "Scratch", "Ember"], "Squirtle":["Tackle", "Water Gun", "Rapid Spin"], "Bulbasaur":["Tackle", "Vine Whip", "Razor Leaf"], "Caterpie":["Tackle", "Bug Bite"], "Rattata":["Tackle", "Quick Attack"], "Pidgey":["Tackle", "Gust", "Quick Attack"], "Weedle":["Tackle", "Poison Sting"], "Oddish":["Absorb", "Acid", "Mega Drain"], "Zubat":["Absorb", "Wing Attack"], "Nidoran Female":["Scratch", "Poison Sting", "Double Kick"], "Nidoran Male":["Poison Sting", "Peck", "Double Kick"], "Rhyhorn":["Tackle", "Smack Down", "Bulldoze"], "Ponyta":["Tackle", "Ember", "Flame Charge"], "Vulpix":["Ember", "Quick Attack", "Incinerate"], "Jigglypuff":["Tackle", "Pound", "Double Slap"], "Onix":["Bind", "Rock Throw", "Tackle"], "Machop":["Revenge", "Low Sweep"], "Tentacool":["Poison Sting", "Constrict", "Acid"], "Staryu":["Tackle", "Water Gun", "Swift"], "Growlithe":["Ember", "Flame Charge"], "Pichu":["Thunder Shock", "Nuzzle", "Tackle"], "Geodude":["Tackle", "Rock Throw", "Take Down"], "Voltorb":["Swift", "Self-Destruct", "Thunderbolt"], "Graveler":["Rock Slide", "Take Down", "Rock Throw", "Self-Destruct"], "Bellsprout":["Acid", "Vine Whip", "Wrap"], "Tangela":["Absorb", "Constrict", "Vine Whip"], "Charmeleon":["Flamethrower", "Fire Fang", "Slash", "Tackle"], "Wartortle":["Bite", "Water Pulse", "Water Gun", "Rapid Spin"], "Ivysaur":["Take Down", "Seed Bomb", "Razor Leaf", "Vine Whip"], "Metapod":["Tackle", "Bug Bite"], "Raticate":["Hyper Fang", "Super Fang", "Crunch", "Tackle"], "Pidgeotto":["wing Attack", "Gust", "Quick Attack", "Tackle"], "Kakuna":["Tackle", "Poison Sting"], "Gloom":["Giga Drain", "Mega Drain", "Acid"], "Golbat":["Wing Attack", "Bite", "Swift"], "Nidorino":["Poison Jab", "Horn Attack", "Peck", "Double kick"], "Nidorina":["Poison Jab", "Horn Attack", "Tackle", "Double kick"], "Rhydon":["Hammer Arm", "Horn Attack", "Drill Run"], "Rapidash":["Flame Charge", "Mega Horn", "Flame Wheel"], "Ninetales":["Fire Spin", "Inferno", "Fire Blast"], "Wigglytuff":["Pound", "Headbutt", "Thunder Punch", "Hyper beam"], "Machoke":["Vital Throw", "Revenge", "Dynamic Punch", "Low Sweep"], "Tentacruel":["Hydro Pump", "Surf", "Poison Jab"], "Starmie":["Hydro Pump", "Flash Cannon", "Tackle", "Water Gun"], "Arcanine":["Flare Blitz", "Flamethrower", "Fire Fang", "Flame Wheel"], "Pikachu":["Electro Ball", "Thunderbolt", "Thunder", "Quick Attack"], "Electrode":["Thunderbolt", "Explosion", "Self-Destruct", "Swift"], "Weepinbell":["Vine Whip", "Acid", "Razor Leaf"], "Charizard":["Fire Spin", "Inferno", "Flare Blitz", "Air Slash"], "Blastoise":["Hydro Pump", "Skull Bash", "Flash Cannon", "Aqua Tail"], "Venusaur":["Solar Beam", "Double-Edge", "Take Down", "Seed Bomb"], "Butterfree":["Bug Buzz", "Air Slash", "Gust", "Bug Bite"], "Pidgeot":["Brave Bird", "Razor Wind", "Air Slash", "Sky Attack"], "Beedrill":["Outrage", "Poison Jab", "Rage", "Peck"], "Vileplume":["Petal Blizzard", "Giga Drain", "Moonblast", "Acid"], "Crobat":["Air Slash", "Cross Poison", "Venoshock", "Absorb"], "Rhyperior":["Rock Wrecker", "Mega Horn", "Hammer Arm", "Earthquake"], "Machamp":["Double-Edge", "Cross Chop", "Dynamic Punch", "Strength"], "Golem":["Explosion", "Double-Edge", "Rock Slide", "Earthquake"], "Lapras":["Hydro Pump", "Body Slam", "Brine", "Icebeam"], "Raichu":["Electro Ball", "Thunderbolt", "Thunder", "Slam"], "Nidoking":["Mega Horn", "Thrash", "Earthquake", "Poison Jab"], "Nidoqueen":["Superpower", "Body Slam", "Earth Power", "Poison Jab"], "Victreebel":["Power Whip", "Vine Whip", "Acid", "Slam"], "Tangrowth":["Power Whip", "Slam", "Giga Drain", "Ancient Power"], "Koffing":["Tackle", "Sludge", "Self-Destruct"], "Weezing":["Sludge", "Sludge Bomb", "Explosion", "Self-Destruct"], "Grimer":["Sludge", "Sludge Bomb", "Pound"], "Muk":["Moonblast", "Sludge Bomb", "Pound", "Sludge"], "Abra":["Tackle"], "Kadabra":["Psychic", "Confusion", "Psybeam"], "Alakazam":["Psychic", "Confusion", "Psybeam", "Hyper Beam"], "Mime Junior":["Pound", "Confusion", "Psybeam"], "Mr. Mime":["Psychic", "Dazzling Gleam", "Psybeam", "Sucker Punch"], "Venonat":["Psybeam", "Confusion", "Tackle"], "Venomoth":["Bug Buzz", "Psychic", "Psybeam", "Confusion"], "Diglett":["Slash", "Bulldoze", "Sucker Punch"], "Dugtrio":["Earthquake",  "Earth Power", "Dig", "Slash"], "Magikarp":["Tackle"], "Gyarados":["Hyper Beam", "Hydro Pump", "Thrash", "Aqua Tail"], "Krabby":["Water Gun", "Bubble Beam", "Tackle"], "Kingler":["Crabhammer", "Slam", "Bubble Beam", "Water Gun"], "Seel":["Headbutt", "Aqua Jet", "Ice Shard"], "Dewgong":["Double-Edge", "Icebeam", "Take Down", "Waterfall"], "Psyduck":["Water Gun", "Scratch", "Confusion"], "Golduck":["Surf", "Hydro Pump", "Psybeam", "Water Pulse"], "Shellder":["Tackle", "Water Gun", "Ice Shard"], "Cloyster":["Hydro Pump", "Icebeam", "Aurora Beam", "Razor Shell"]}

pokemontype = {"Charmander":"Fire", "Squirtle":"Water", "Bulbasaur":"Grass", "Caterpie":"Bug", "Rattata":"Normal", "Pidgey":"Flying", "Weedle":"Bug", "Oddish":"Grass", "Zubat":"Poison", "Nidoran Male":"Poison", "Nidoran Female":"Poison", "Rhyhorn":"Rock", "Ponyta":"Fire", "Vulpix":"Fire", "Jigglypuff":"Fairy", "Onix":"Ground", "Machop":"Fighting", "Tentacool":"Water", "Staryu":"Water", "Growlithe":"Fire", "Pichu":"Electric", "Geodude":"Rock", "Voltorb":"Electric", "Bellsprout":"Grass", "Charmeleon":"Fire", "Wartortle":"Water", "Ivysaur":"Grass", "Metapod":"Bug", "Raticate":"Normal", "Pidgeotto":"Flying", "Kakuna":"Bug", "Gloom":"Grass", "Golbat":"Flying", "Nidorino":"Poison", "Nidorina":"Poison", "Rhydon":"Rock", "Rapidash":"Fire", "Ninetales":"Fire", "Wigglytuff":"Fairy", "Machoke":"Fighting", "Tentacruel":"Water", "Starmie":"Water", "Arcanine":"Fire", "Pikachu":"Electric", "Graveler":"Rock", "Weepinbell":"Grass", "Charizard":"Fire", "Blastoise":"Water", "Venusaur":"Grass", "Butterfree":"Bug", "Pidgeot":"Flying", "Beedrill":"Bug", "Vileplume":"Grass", "Crobat":"Flying", "Rhyperior":"Rock", "Machamp":"Fighting", "Golem":"Rock", "Lapras":"Water", "Electrode":"Electric", "Raichu":"Electric", "Nidoking":"Poison", "Nidoqueen":"Poison", "Victreebel":"Grass", "Tangela":"Grass", "Tangrowth":"Grass", "Koffing":"Poison", "Weezing":"Poison", "Grimer":"Poison", "Muk":"Poison", "Abra":"Psychic", "Kadabra":"Psychic", "Alakazam":"Psychic", "Mime Junior":"Psychic", "Mr. Mime":"Psychic", "Venonat":"Bug", "Venomoth":"Bug", "Diglett":"Ground", "Dugtrio":"Ground", "Magikarp":"Water", "Gyarados":"Water", "Krabby":"Water", "Kingler":"Water", "Seel":"Water", "Dewgong":"Water", "Psyduck":"Water", "Golduck":"Water", "Shellder":"Water", "Cloyster":"Water"}

movetype = {"Tackle":"Normal", "Scratch":"Normal", "Ember":"Fire", "Water Gun":"Water", "Rapid Spin":"Normal", "Vine Whip":"Grass", "Razor Leaf":"Grass", "Bug Bite":"Bug", "Quick Attack":"Normal", "Gust":"Flying", "Poison Sting":"Poison", "Absorb":"Grass", "Acid":"Poison", "Mega Drain":"Grass", "Wing Attack":"Flying", "Double Kick":"Fighting", "Peck":"Flying", "Smack Down":"Rock", "Bulldoze":"Ground", "Flame Charge":"Fire", "Incinerate":"Fire", "Pound":"Normal", "Double Slap":"Normal", "Bind":"Normal", "Rock Throw":"Rock", "Revenge":"Fighting", "Low Sweep":"Fighting", "Constrict":"Normal", "Swift":"Normal", "Thunder Shock":"Electric", "Nuzzle":"Electric", "Flamethrower":"Fire", "Fire Fang":"Fire", "Slash":"Normal", "Bite":"Normal", "Water Pulse":"Water", "Take Down":"Normal", "Seed Bomb":"Grass", "Hyper Fang":"Normal", "Super Fang":"Normal", "Crunch":"Normal", "Giga Drain":"Grass", "Poison Jab":"Poison", "Horn Attack":"Normal", "Fire Spin":"Fire", "Inferno":"Fire", "Fire Blast":"Fire", "Hammer Arm":"Fighting", "Drill Run":"Normal", "Mega Horn":"Normal", "Flame Wheel":"Fire", "Headbutt":"Normal", "Thunder Punch":"Electric", "Hyper Beam":"Normal", "Dynamic Punch":"Fighting", "Vital Throw":"Fighting", "Hydro Pump":"Water", "Surf":"Water", "Flash Cannon":"Normal", "Flare Blitz":"Fire", "Electro Ball":"Electric", "Thunderbolt":"Electric", "Thunder":"Electric", "Solar Beam":"Grass", "Double-Edge":"Normal", "Bug Buzz":"Bug", "Air Slash":"Flying", "Cross Chop":"Fighting", "Cross Poison":"Poison", "Aqua Tail":"Water", "Skull Bash":"Normal", "Air Attack":"Flying", "Brave Bird":"Flying", "Earthquake":"Ground", "Rock Wrecker":"Rock", "Razor Wind":"Flying", "Outrage":"Normal", "Rage":"Normal", "Moonblast":"Fairy", "Petal Blizzard":"Grass", "Venoshock":"Poison", "Strength":"Fighting", "Rock Slide":"Rock", "Self-Destruct":"Normal", "Explosion":"Normal", "Body Slam":"Normal", "Brine":"Water", "Slam":"Normal", "Thrash":"Normal", "Superpower":"Fighting", "Earth Power":"Ground", "Wrap":"Normal", "Power Whip":"Grass", "Ancient Power":"Rock", "Sludge":"Poison", "Sludge Bomb":"Poison", "Icebeam":"Ice", "Psychic":"Psychic", "Confusion":"Psychic", "Psybeam":"Psychic", "Sucker Punch":"Fighting", "Dazzling Gleam":"Fairy", "Bubble Beam":"Water", "Crabhammer":"Water", "Aqua Jet":"Water", "Waterfall":"Water", "Ice Shard":"Ice", "Aurora Beam":"Ice", "Razor Shell":"Water"}

pokemonhp = {"Charmander":70, "Squirtle":60, "Bulbasaur":70, "Caterpie":60, "Rattata":50, "Pidgey":60, "Weedle":50, "Oddish":60, "Zubat":50, "Nidoran Male":70, "Nidoran Female":70, "Rhyhorn":80, "Ponyta":60, "Vulpix":50, "Jigglypuff":40, "Onix":150, "Machop":50, "Tentacool":60, "Staryu":50, "Growlithe":60, "Pichu":50, "Geodude":60, "Voltorb":60, "Bellsprout":50, "Charmeleon":120, "Wartortle":110, "Ivysaur":110, "Metapod":90, "Raticate":90, "Pidgeotto":100, "Kakuna":90, "Gloom":100, "Weepinbell":100, "Golbat":90, "Nidorino":100, "Nidorina":100, "Rhydon":130, "Rapidash":100, "Ninetales":220, "Wigglytuff":100, "Machoke":110, "Tentacruel":100, "Starmie":70, "Arcanine":210, "Pikachu":100, "Graveler":110, "Charizard":250, "Blastoise":250, "Venusaur":250, "Butterfree":225, "Pidgeot":230, "Beedrill":210, "Vileplume":225, "Crobat":225, "Rhypherior":275, "Machamp":265, "Golem":270, "Lapras":250, "Electrode":215, "Raichu":230, "Nidoking":255, "Nidoqueen":255, "Victreebel":240, "Tangela":60, "Tangrowth":230, "Koffing":60, "Weezing":210, "Grimer":60, "Muk":210, "Abra":50, "Kadabra":110, "Alakazam":240, "Mime Junior":50, "Mr. Mime":210, "Venonat":60, "Venomoth":220, "Diglett":60, "Dugtrio":225, "Magikarp":60, "Gyarados":260, "Krabby":50, "Kingler":220, "Seel":60, "Dewgong":230, "Psyduck":60, "Golduck":230, "Shellder":60, "Cloyster":240}

moveattackpower = {"Tackle":10, "Scratch":10, "Ember":15, "Water Gun":20, "Rapid Spin":20, "Vine Whip":15, "Razor Leaf":20, "Bug Bite":10, "Quick Attack":20, "Gust":20, "Poison Sting":10, "Absorb":10, "Acid":20, "Mega Drain":20, "Wing Attack":20, "Double Kick":20, "Peck":10, "Smack Down":20, "Bulldoze":25, "Flame Charge":35, "Incinerate":40, "Pound":20, "Double Slap":30, "Bind":10, "Rock Throw":10, "Revenge":20, "Low Sweep":20, "Constrict":25, "Swift":30, "Thunder Shock":20, "Nuzzle":10, "Flamethrower":35, "Fire Fang":30, "Slash":20, "Bite":20, "Water Pulse":20, "Take Down":25, "Seed Bomb":30, "Hyper Fang":35, "Super Fang":40, "Crunch":30, "Giga Drain":30, "Poison Jab":20, "Horn Attack":30, "Fire Spin":35, "Inferno":30, "Fire Blast":40, "Hammer Arm":35, "Drill Run":20, "Mega Horn":50, "Flame Wheel":40, "Headbutt":20, "Thunder Punch":25, "Hyper Beam":40, "Dynamic Punch":35, "Vital Throw":30, "Hydro Pump":50, "Surf":30, "Flash Cannon":35, "Flare Blitz":40, "Electro Ball":20, "Thunderbolt":35, "Thunder":40, "Solar Beam":60, "Double-Edge":55, "Bug Buzz":50, "Air Slash":40, "Cross Chop":50, "Cross Poison":45, "Aqua Tail":45, "Skull Bash":50, "Air Attack":55, "Brave Bird":55, "Earthquake":55, "Rock Wrecker":60, "Razor Wind":40, "Outrage":60, "Rage":50, "Moonblast":55, "Petal Blizzard":50, "Venoshock":50, "Strength":50, "Rock Slide":30, "Self-Destruct":100, "Explosion":150, "Body Slam":40, "Brine":40, "Slam":50, "Thrash":50, "Superpower":50, "Earth Power":40, "Wrap":10, "Power Whip":45, "Ancient Power":55, "Sludge":15, "Sludge Bomb":40, "Icebeam":50, "Psychic":45, "Confusion":25, "Psybeam":35, "Dazzling Gleam":40, "Sucker Punch":45, "Bubble Beam":15, "Crabhammer":40, "Aqua Jet":20, "Ice Shard":20, "Waterfall":40, "Aurora Beam":30, "Razor Shell":35}

evolution1 = {"Charmander":"Charmeleon", "Squirtle":"Wartortle", "Bulbasaur":"Ivysaur", "Caterpie":"Metapod", "Rattata":"Raticate", "Pidgey":"Pidgeotto", "Weedle":"Kakuna", "Oddish":"Gloom", "Zubat":"Golbat", "Nidoran Male":"Nidorino", "Nidoran Female":"Nidorina", "Rhyhorn":"Rhydon", "Ponyta":"Rapidash", "Vulpix":"Ninetales", "Jigglypuff":"Wigglytuff", "Machop":"Machoke", "Tentacool":"Tentacruel", "Staryu":"Starmie", "Growlithe":"Arcanine", "Pichu":"Pikachu", "Geodude":"Graveler", "Voltorb":"Electrode", "Bellsprout":"Weepinbell", "Tangela":"Tangrowth", "Koffing":"Weezing", "Grimer":"Muk", "Abra":"Kadabra", "Mime Junior":"Mr. Mime", "Venonat":"Venomoth", "Diglett":"Dugtrio", "Magikarp":"Gyarados", "Krabby":"Kingler", "Seel":"Dewgong", "Psyduck":"Golduck", "Shellder":"Cloyster"}

evolution2 = {"Charmeleon":"Charizard", "Wartortle":"Blastoise", "Ivysaur":"Venusaur", "Metapod":"Butterfree", "Pidgeotto":"Pidgeot", "Kakuna":"Beedrill", "Golbat":"Crobat", "Rhydon":"Rhyperior", "Machoke":"Machamp", "Gloom":"Vileplume", "Graveler":"Golem", "Pikachu":"Raichu", "Nidorino":"Nidoking", "Nidorina":"Nidoqueen", "Weepinbell":"Victreebel", "Kadabra":"Alakazam"}

finalevolutions = ["Charizard", "Ninetales", "Blastoise", "Venusaur", "Butterfree", "Pidgeot", "Beedrill", "Crobat", "Rhyperior", "Machamp", "Pikachu", "Tentacruel", "Starmie", "Arcanine", "Rapidash", "Nidorino", "Nidorina", "Vileplume", "Raticate", "Wigglytuff", "Golem", "Lapras", "Electrode", "Raichu", "Nidoking", "Nidoqueen", "Victorybell", "Tangrowth", "Weezing", "Muk", "Alakazam", "Mr. Mime", "Venomoth", "Digtrio", "Onix", "Gyarados", "Kingler", "Dewgong", "Golduck", "Cloyster"]

print("Welcome to the Pokemon world, in this world there are creatures called pokemon, people make friends with pokemon or they use them to help them out in their daily lives. Every pokemon is special in their own way and are usually kept in a Pokeball. Anyway, it is time for you to pick your first pokemon to start your journey.\n")

mymainpokemon = {}
mypokedex = []
inventory = []
currentgym = "Brock"
currentleaguetrainer = "James"
myleaguepokemon = {}
badges = []
money = 0

name = input("What is your name:")

print("\nOk "+str(name)+", there are 3 choices for you.\n")
print("1. Charmander")
print("2. Squirtle")
print("3. Bulbasaur\n")
print("Which pokemon would you like to choose as your partner?\n")
while len(list(mymainpokemon.keys())) == 0:
	choice = input("Please type 1 for Charmander, 2 for Squirtle or 3 for Bulbasaur:")
	if choice == "1" or choice == "1.":
		print("Charmander is a fire type pokemon that has 70 HP and knows these moves.\n")
		print(str(pokemonmoves["Charmander"]))
		c = input("If you want to choose this pokemon type 'y', if you don't want to choose this pokemon, type 'n':")
		if c=="y":
			mymainpokemon["Charmander"] = [70, 0]
			mypokedex.append("Charmander")
			print("Congratulations, Charmander is now part of your team and your new partner!\n")
		else:
			pass
	elif choice == "2" or choice == "2.":
		print("Squirtle is a water type pokemon that has 60 HP and knows these moves.\n")
		print(str(pokemonmoves["Squirtle"]))
		c = input("If you want to choose this pokemon type 'y', if you don't want to choose this pokemon, type 'n':")
		if c=="y":
			mymainpokemon["Squirtle"] = [60, 0]
			mypokedex.append("Squirtle")
			print("Congratulations, Squirtle is now part of your team and your new partner!\n")
		else:
			pass
	elif choice == "3" or choice == "3.":
		print("Bulbasaur is a grass type pokemon that has 60 HP and knows these moves.\n")
		print(str(pokemonmoves["Bulbasaur"]))
		c = input("If you want to choose this pokemon type 'y', if you don't want to choose this pokemon, type 'n':")
		if c=="y":
			mymainpokemon["Bulbasaur"] = [60, 0]
			mypokedex.append("Bulbasaur")
			print("Congratulations, Bulbasaur is now part of your team and your new partner!\n")
		else:
			pass

	else:
		print("Please enter your input correctly.\n")

input("To start off, I will be giving you 6 pokeballs.\n")
pokeballs = 6
input("A pokeball is a device that you can use to catch a pokemon when it is at low health.\n")
input("It is now time for you to start your journey.\n")
input("Good Luck!\n")

input("By the way, Professor Oak asked to see you before you left.\n\n")

input("At Professor Oak's Lab...\n\n")

input("Professor Oak: Hello "+name+"\n")

input("Professor Oak: I wanted to talk to you about something important that I was researching. It is called a Pokedex.\n")

input("Professor Oak: I wanted you to have this device so that you can collect data on every type of pokemon there is so that others can use it to know before-hand what the pokemon is.\n")

input("Professor Oak: I could make a big breakthrough using Pokedex technology!BTW, I won't allow you to catch 2 or more of the same pokemon so that the Pokedex doesn't get confused as it is still a prototype and the rest of the same pokemon will be automatically left in the wild! Also the first 6 pokemon you catch will be your main team, the rest will be sent to me\n")

input("Professor Oak: Along the way you can challenge the gyms and once you collect 8 badges, you can challenge the pokemon league!\n")

input("Professor Oak: I need you to do this for me so thanks and I want you to come back to me once you catch 6 pokemon!\n")
input("Professor Oak: Good Luck on your journey!\n")

def shop():
	global pokeballs
	global money
	global mymainpokemon
	print("\nWelcome to the Pokemon Center!")
	print("Here you can heal your pokemon and buy pokeballs!\n")
	print("What would you like to do?")
	i = input("Type 'h' to heal your pokemon and 's' to buy more pokeballs and 'q' to quit:")
	if i == 'h':
		print("Your pokemon are being healed...")
		time.sleep(1)
		for i in mymainpokemon.keys():
			mymainpokemon[i] = [pokemonhp[i], mymainpokemon[i][1]]
		print("\nAll of your pokemon have been fully healed!\n")
		i = input("If you would like to do anything else, type 'h' to heal your pokemon and 's' to buy more pokeballs and 'q' to quit:")
	elif i == "s":
		print("One pokeball costs $10.")
		a = input("How many would you like to buy:")
		if (int(a)*10) <= money:
			money -= int(a)*10
			pokeballs += int(a)
			print("You have successfully purchased "+a+" pokeballs!\n")
		else:
			print("You are unable to purchase these pokeballs due to lack of money!")
			print("Come back when you earn more money!\n")
		i = input("If you would like to do anything else, type 'h' to heal your pokemon and 's' to buy more pokeballs and 'q' to quit:")
	elif i == "q":
		return
	else:
		print("Please enter your input correctly!\n")
	if i == 'h':
		print("Your pokemon are being healed...")
		time.sleep(1)
		for i in mymainpokemon.keys():
			mymainpokemon[i] = [pokemonhp[i], mymainpokemon[i][1]]
			print("\nAll of your pokemon have been fully healed!\n")
	elif i == "s":
		print("One pokeball costs $10.")
		a = input("How many would you like to buy:")
		if (int(a)*10) <= money:
			money -= int(a)*10
			pokeballs += int(a)
			print("You have successfully purchased "+a+" pokeballs!\n")
		else:
			print("You are unable to purchase these pokeballs due to lack of money!")
			print("Come back when you earn more money!\n")
	else:
		return

def battle():
	global money
	global pokeballs
	global mymainpokemon
	global mypokedex
	currentpokemon = []
	caughtpokemon = []
	acc = 0
	opponent = 0
	pr = input("\nIf you want to search the wilderness, type '1', if you want to fish for pokemon, type '2':")
	rarity = random.choice(pokemonrarity)
	while opponent == 0:
		if pr == "1":
			if rarity == "Common":
				opponent = random.choice(commongroundpokemon)
			elif rarity == "Uncommon":
				opponent = random.choice(uncommongroundpokemon)
			elif rarity == "Rare":
				opponent = random.choice(raregroundpokemon)
			elif rarity == "Very Rare":
				opponent = random.choice(veryraregroundpokemon)
			elif rarity == "Super Rare":
				opponent = random.choice(superraregroundpokemon)

		else:
			if rarity == "Common":
				opponent = random.choice(commonwaterpokemon)
			elif rarity == "Uncommon":
				opponent = random.choice(uncommonwaterpokemon)
			elif rarity == "Rare":
				opponent = random.choice(rarewaterpokemon)
			elif rarity == "Very Rare":
				opponent = random.choice(veryrarewaterpokemon)
			elif rarity == "Super Rare":
				opponent = random.choice(superrarewaterpokemon)

	opponenthp = pokemonhp[opponent]
	print("\nYou found a wild "+opponent)
	print("You sent out "+list(mymainpokemon.keys())[0]+"\n")
	currentpokemon = list(mymainpokemon.keys())[0]
	currentpokemonhp = mymainpokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 or opponent in caughtpokemon:
			print("\nYou won the battle!")
			print("You earned 20 dollars!\n")
			mymainpokemon[currentpokemon][1] += 10
			print(currentpokemon+" earned 10 XP!\n")
			money += 20
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in mymainpokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle!\n")
				shop()
				return
			while mymainpokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in mymainpokemon.keys():
					if mymainpokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in mymainpokemon.keys():
					if mymainpokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = mymainpokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
	
		print("\nWould you like to attack, switch your pokemon or use a pokeball?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon and 3 to use a pokeball and 4 to escape the battle:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				mymainpokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			for i in mymainpokemon.keys():
				if mymainpokemon[i][0] > 0:
					print(i)
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in mymainpokemon.keys() and mymainpokemon[c][0] > 0:
				currentpokemon = c
				currentpokemonhp = mymainpokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")

			elif c in mymainpokemon.keys() and mymainpokemon[c][0] < 0:
				print(i+" has already fainted!\n")

			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			mymainpokemon[currentpokemon][0] = currentpokemonhp

		elif play == "3":
			if pokeballs > 0:
				if opponenthp <= 15 and opponenthp >= 1:
					print("You threw a pokeball!")
					pokeballs -= 1
					print(".")
					time.sleep(1)
					print("..")
					time.sleep(1)
					print("...")
					time.sleep(1)

					if random.choice(easycatch) == "Yes":
						print("You caught the wild "+opponent+"!\n")
						if len(mymainpokemon.keys()) <= 5:
							mymainpokemon[opponent] = [opponenthp, 0]
						else:
							mypokedex.append(opponent)
						caughtpokemon.append(opponent)

					else:
						print("....")
						time.sleep(1)
						print("Oh no, the wild "+opponent+" escaped!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

						if opponenthp > 0:
							opponentmove = random.choice(pokemonmoves[opponent])

							print(opponent+" used "+opponentmove+"!\n")
							
							if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
								if opponentmove == "Absorb":
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp += moveattackpower[opponentmove]*0.5
									print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

								elif opponentmove == "Mega Drain":
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp += moveattackpower[opponentmove]*0.5
									print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

								elif opponentmove == 'Giga Drain':
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp += moveattackpower[opponentmove]*0.5
									print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

								elif opponentmove == 'Explosion':
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp = 0

								elif opponentmove == 'Self-Destruct':
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp = 0
									
								else:
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
								print("It was not effective!\n")
									
							elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
								if opponentmove == "Absorb":
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp += moveattackpower[opponentmove]*2
									print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

								elif opponentmove == "Mega Drain":
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp += moveattackpower[opponentmove]*2
									print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

								elif opponentmove == 'Giga Drain':
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp += moveattackpower[opponentmove]*2
									print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

								elif opponentmove == 'Explosion':
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp = 0

								elif opponentmove == 'Self-Destruct':
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp = 0
									
								else:
									currentpokemonhp -= moveattackpower[opponentmove]*2
								print("It was super effective!\n")

							else:
								if opponentmove == "Absorb":
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp += moveattackpower[opponentmove]
									print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

								elif opponentmove == "Mega Drain":
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp += moveattackpower[opponentmove]
									print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

								elif opponentmove == 'Giga Drain':
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp += moveattackpower[opponentmove]
									print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

								elif opponentmove == 'Explosion':
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp = 0

								elif opponentmove == 'Self-Destruct':
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp = 0
									
								else:
									currentpokemonhp -= moveattackpower[opponentmove]
								print("It was effective!\n")

							print(opponent+" has "+str(opponenthp)+"HP left.")
							print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")


				elif opponenthp > 15:
					print("You threw a pokeball!")
					pokeballs -= 1
					print(".")
					time.sleep(1)
					print("..")
					time.sleep(1)
					print("...")
					time.sleep(1)

					if random.choice(hardcatch) == "Yes":
						print("You caught the wild "+opponent+"!\n")
						print("You caught the wild "+opponent+"!\n")
						if len(mymainpokemon.keys()) <= 5:
							mymainpokemon[opponent] = [opponenthp, 0]
						else:
							mypokedex.append(opponent)
						caughtpokemon.append(opponent)

					else:
						print("....")
						time.sleep(1)
						print("Oh no, the wild "+opponent+" escaped!\n")
						print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

						if opponenthp > 0:
							opponentmove = random.choice(pokemonmoves[opponent])

							print(opponent+" used "+opponentmove+"!\n")
							
							if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
								if opponentmove == "Absorb":
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp += moveattackpower[opponentmove]*0.5
									print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

								elif opponentmove == "Mega Drain":
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp += moveattackpower[opponentmove]*0.5
									print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

								elif opponentmove == 'Giga Drain':
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp += moveattackpower[opponentmove]*0.5
									print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

								elif opponentmove == 'Explosion':
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp = 0

								elif opponentmove == 'Self-Destruct':
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
									opponenthp = 0
									
								else:
									currentpokemonhp -= moveattackpower[opponentmove]*0.5
								print("It was not effective!\n")
									
							elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
								if opponentmove == "Absorb":
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp += moveattackpower[opponentmove]*2
									print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

								elif opponentmove == "Mega Drain":
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp += moveattackpower[opponentmove]*2
									print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

								elif opponentmove == 'Giga Drain':
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp += moveattackpower[opponentmove]*2
									print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

								elif opponentmove == 'Explosion':
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp = 0

								elif opponentmove == 'Self-Destruct':
									currentpokemonhp -= moveattackpower[opponentmove]*2
									opponenthp = 0
									
								else:
									currentpokemonhp -= moveattackpower[opponentmove]*2
								print("It was super effective!\n")

							else:
								if opponentmove == "Absorb":
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp += moveattackpower[opponentmove]
									print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

								elif opponentmove == "Mega Drain":
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp += moveattackpower[opponentmove]
									print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

								elif opponentmove == 'Giga Drain':
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp += moveattackpower[opponentmove]
									print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

								elif opponentmove == 'Explosion':
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp = 0

								elif opponentmove == 'Self-Destruct':
									currentpokemonhp -= moveattackpower[opponentmove]
									opponenthp = 0
									
								else:
									currentpokemonhp -= moveattackpower[opponentmove]
								print("It was effective!\n")

							print(opponent+" has "+str(opponenthp)+"HP left.")
							print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			else:
				print("You need to buy more pokeballs!\n")

		elif play == "4":
			print("You have escaped!\n")
			return

		else:
			print("Please enter your input correctly!\n")


def data():
	global money
	global pokeballs
	global mymainpokemon
	print("\nHere is your data:\n")
	print("You have $"+str(money)+".\n")
	print("This is what you have in your inventory:\n")
	print(str(inventory)+"\n")
	print("You have "+str(pokeballs)+" pokeballs.\n")
	print("Here are your pokemon, their health and their xp:\n")
	for i in mymainpokemon.keys():
		print(i+" has "+str(mymainpokemon[i][0])+"HP left and has "+str(mymainpokemon[i][1])+" xp.\n")
	print("Here are your Badges: "+str(badges)+"\n")
	inpu = input("If you would like to view your Pokedex type 'y' and if you don't type 'n':")
	if inpu == "y":
		print("These are the pokemon you have collected data on:\n")
		for x in mypokedex:
			print(x)
		print("\n\n")
	else:
		pass
	y = input("If you want to change the order of your pokemon please type 'y', otherwise, type 'n':")
	if y=="y":
		mynewpokemon = {}
		print("\nPlease type in the names of the pokemon in the order that you want!\n")
		print(str(list(mymainpokemon.keys())))
		while len(mymainpokemon) != len(mynewpokemon):
			lp = input("Please type in the name of the pokemon you chose:")
			if len(lp)>0:
				p = lp.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
			if p in mymainpokemon.keys():
				mynewpokemon[p] = [mymainpokemon[p][0], mymainpokemon[p][1]]
				print("\n")
			else:
				print("Please type in your input correctly!\n")
		mymainpokemon = mynewpokemon
	



def firstevolution():
	global mymainpokemon
	for i in list(mymainpokemon.keys()):
		xp = mymainpokemon[i][1]
		if i in evolution1.keys():
			if xp >= 100:
				print("\nWait, "+i+" is trying to evolve!")
				print(".")
				time.sleep(1)
				print("..")
				time.sleep(1)
				p = input("Do you want "+i+" to evolve, type 'y' if you want it to and 'n' if you don't want it to:")
				if p == "y":
					mypokedex.append(evolution1[i])
					mymainpokemon.pop(i)
					mymainpokemon[evolution1[i]] = [pokemonhp[evolution1[i]], xp]
					print(i+" has evolved into "+evolution1[i]+"!\n")
				else:
					print(i+" did not evolve!\n")
					pass

def finalevolution():
	global mymainpokemon
	for i in list(mymainpokemon.keys()):
		xp = mymainpokemon[i][1]
		if i in evolution2.keys():
			if xp >= 500:
				print("\nWait, "+i+" is trying to evolve!")
				print(".")
				time.sleep(1)
				print("..")
				time.sleep(1)
				if i == "Pikachu":
					p = input("Do you want Pikachu to evolve using the Thunder Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Thunder Stone" in inventory:
							inventory.pop("Thunder Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Thunder Stone!\n")
						else:
							print("You don't have a Thunder Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Nidorino":
					p = input("Do you want Nidorino to evolve using the Moon Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Moon Stone" in inventory:
							inventory.pop("Moon Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Moon Stone!\n")
						else:
							print("You don't have a Moon Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Nidorina":
					p = input("Do you want Nidorina to evolve using the Moon Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Moon Stone" in inventory:
							inventory.pop("Moon Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Moon Stone!\n")
						else:
							print("You don't have a Moon Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Weepinbell":
					p = input("Do you want Weepinbell to evolve using the Leaf Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Leaf Stone" in inventory:
							inventory.pop("Leaf Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Leaf Stone!\n")
						else:
							print("You don't have a Leaf Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Gloom":
					p = input("Do you want Gloom to evolve using the Leaf Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Leaf Stone" in inventory:
							inventory.pop("Leaf Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Leaf Stone!\n")
						else:
							print("You don't have a Leaf Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Vulpix":
					p = input("Do you want Vulpix to evolve using the Fire Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Fire Stone" in inventory:
							inventory.pop("Fire Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Fire Stone!\n")
						else:
							print("You don't have a Fire Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Growlithe":
					p = input("Do you want Growlithe to evolve using the Fire Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Fire Stone" in inventory:
							inventory.pop("Fire Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Fire Stone!\n")
						else:
							print("You don't have a Fire Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Jigglypuff":
					p = input("Do you want Jigglypuff to evolve using the Moon Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Moon Stone" in inventory:
							inventory.pop("Moon Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Moon Stone!\n")
						else:
							print("You don't have a Moon Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Staryu":
					p = input("Do you want Staryu to evolve using the Water Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Water Stone" in inventory:
							inventory.pop("Water Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Water Stone!\n")
						else:
							print("You don't have a Water Stone!\n")
					else:
						print(i+" did not evolve!\n")
				elif i == "Shellder":
					p = input("Do you want Shellder to evolve using the Water Stone, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						if "Water Stone" in inventory:
							inventory.pop("Water Stone")
							mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
							print(i+" has evolved into "+evolution2[i]+" using the Water Stone!\n")
						else:
							print("You don't have a Water Stone!\n")
					else:
						print(i+" did not evolve!\n")
				else:
					p = input("Do you want"+i+" to evolve, type 'y' if you want it to and 'n' if you don't want it to:")
					if p == "y":
						mypokedex.append(evolution2[i])
						mymainpokemon.pop(i)
						mymainpokemon[evolution2[i]] = [pokemonhp[evolution2[i]], xp]
						print(i+" has evolved into "+evolution2[i]+"!\n")
					else:
						print(i+" did not evolve!\n")


def gymbattle():
	global money
	global pokeballs
	global mymainpokemon
	global badges
	global currentgym
	acc = 0
	opponent = gympokemon[currentgym][0]
	lastopponent = gympokemon[currentgym][len(gympokemon[currentgym])-1]
	opponenthp = pokemonhp[opponent]
	print("\nYou have challenged "+currentgym+"'s gym!")
	print(currentgym+" sent out "+opponent)
	print("You sent out "+list(mymainpokemon.keys())[0]+"!\n")
	currentpokemon = list(mymainpokemon.keys())[0]
	currentpokemonhp = mymainpokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 and opponent != lastopponent:
			print(opponent+" has fainted!")
			opponent = gympokemon[currentgym][gympokemon[currentgym].index(opponent)+1]
			mymainpokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			print(currentgym+" sent out "+opponent)
			opponenthp = pokemonhp[opponent]
		elif opponent == lastopponent and opponenthp <= 0:
			print("Congratulations!, you won the battle!\n")
			print("You earned $50 and the "+gymbadges[currentgym]+"!\n")
			mymainpokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			badges.append(gymbadges[currentgym])
			if currentgym == "Brock":
				currentgym = "Misty"
			elif currentgym == "Misty":
				currentgym = "Lt. Surge"
			elif currentgym == "Lt. Surge":
				currentgym = "Erika"
			elif currentgym == "Erika":
				currentgym = "Koga"
			elif currentgym == "Koga":
				currentgym = "Sabrina"
			elif currentgym == "Sabrina":
				currentgym = "Blaine"
			elif currentgym == "Blaine":
				currentgym = "Giovanni"
			elif currentgym == "Giovanni":
				currentgym = "Pokemon League"
			money += 50
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in mymainpokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle!\n")
				shop()
				return
			while mymainpokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in mymainpokemon.keys():
					if mymainpokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in mymainpokemon.keys():
					if mymainpokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = mymainpokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
		
		print("\nWould you like to attack or switch your pokemon?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				mymainpokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			print(str(list(mymainpokemon.keys())))
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in mymainpokemon.keys():
				currentpokemon = c
				currentpokemonhp = mymainpokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")
			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			mymainpokemon[currentpokemon][0] = currentpokemonhp

		else:
			print("Please enter your input correctly!")

def jamesbattle():
	global money
	global mymainpokemon
	global currentgym
	global myleaguepokemon
	global currentleaguetrainer
	global myleaguepokemon
	print("\nYou have completed registration!\n")
	print("Your matchup is James!\n")
	print("You have to pick 3 pokemon for the first few rounds to fight with you and each pokemon will be recharged fully after each battle!")
	print(str(list(mymainpokemon.keys())))
	lp = input("Please type in the name of the first pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your second pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the second pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your third pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the third pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now battle James\n!")
	else:
		print("Please enter your input correctly!\n")
	acc = 0
	opponent = leaguepokemon[currentleaguetrainer][0]
	lastopponent = leaguepokemon[currentleaguetrainer][len(leaguepokemon[currentleaguetrainer])-1]
	opponenthp = pokemonhp[opponent]
	print("\nYou are going to battle "+currentleaguetrainer+"!")
	print(currentleaguetrainer+" sent out "+opponent)
	print("You sent out "+list(myleaguepokemon.keys())[0]+"!\n")
	currentpokemon = list(myleaguepokemon.keys())[0]
	currentpokemonhp = myleaguepokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 and opponent != lastopponent:
			print(opponent+" has fainted!")
			opponent = leaguepokemon[currentleaguetrainer][leaguepokemon[currentleaguetrainer].index(opponent)+1]
			mymainpokemon[currentpokemon][1] += 50
			myleaguepokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			print(currentleaguetrainer+" sent out "+opponent)
			opponenthp = pokemonhp[opponent]
		elif opponent == lastopponent and opponenthp <= 0:
			print("Congratulations!, you won the battle!\n")
			print("You earned $50 and are moving on to the next match!\n")
			mymainpokemon[currentpokemon][1] += 50
			mymainpokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			if currentleaguetrainer == "James":
				currentleaguetrainer = "Ethan"
			elif currentleaguetrainer == "Ethan":
				currentleaguetrainer = "Kevin"
			elif currentleaguetrainer == "Kevin":
				currentleaguetrainer = "Holt"
			elif currentleaguetrainer == "Holt":
				currentleaguetrainer= "Ray"
			for i in mymainpokemon.keys():
				mymainpokemon[i][0] = pokemonhp[i]
			money += 50
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in myleaguepokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle and the pokemon league is over!\n")
				shop()
				return
			while myleaguepokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in myleaguepokemon.keys():
					if myleaguepokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in myleaguepokemon.keys():
					if myleaguepokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = myleaguepokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
		
		print("\nWould you like to attack or switch your pokemon?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				myleaguepokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			print(str(list(myleaguepokemon.keys())))
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in myleaguepokemon.keys():
				currentpokemon = c
				currentpokemonhp = myleaguepokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")
			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			myleaguepokemon[currentpokemon][0] = currentpokemonhp

		else:
			print("Please enter your input correctly!")

def ethanbattle():
	global money
	global mymainpokemon
	global currentgym
	global myleaguepokemon
	global currentleaguetrainer
	global myleaguepokemon
	print("Your matchup is Ethan!\n")
	print("You have to pick 3 pokemon for the first few rounds to fight with you and each pokemon will be recharged fully after each battle!")
	print(str(list(mymainpokemon.keys())))
	lp = input("Please type in the name of the first pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your second pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the second pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your third pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the third pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now battle Ethan\n!")
	else:
		print("Please enter your input correctly!\n")
	acc = 0
	opponent = leaguepokemon[currentleaguetrainer][0]
	lastopponent = leaguepokemon[currentleaguetrainer][len(leaguepokemon[currentleaguetrainer])-1]
	opponenthp = pokemonhp[opponent]
	print("\nYou are going to battle "+currentleaguetrainer+"!")
	print(currentleaguetrainer+" sent out "+opponent)
	print("You sent out "+list(myleaguepokemon.keys())[0]+"!\n")
	currentpokemon = list(myleaguepokemon.keys())[0]
	currentpokemonhp = myleaguepokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 and opponent != lastopponent:
			print(opponent+" has fainted!")
			opponent = leaguepokemon[currentleaguetrainer][leaguepokemon[currentleaguetrainer].index(opponent)+1]
			mymainpokemon[currentpokemon][1] += 50
			myleaguepokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			print(currentleaguetrainer+" sent out "+opponent)
			opponenthp = pokemonhp[opponent]
		elif opponent == lastopponent and opponenthp <= 0:
			print("Congratulations!, you won the battle!\n")
			print("You earned $50 and are moving on to the next match!\n")
			mymainpokemon[currentpokemon][1] += 50
			mymainpokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			if currentleaguetrainer == "James":
				currentleaguetrainer = "Ethan"
			elif currentleaguetrainer == "Ethan":
				currentleaguetrainer = "Kevin"
			elif currentleaguetrainer == "Kevin":
				currentleaguetrainer = "Holt"
			elif currentleaguetrainer == "Holt":
				currentleaguetrainer= "Ray"
			for i in mymainpokemon.keys():
				mymainpokemon[i][0] = pokemonhp[i]
			money += 50
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in myleaguepokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle and the pokemon league is over!\n")
				shop()
				return
			while myleaguepokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in myleaguepokemon.keys():
					if myleaguepokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in myleaguepokemon.keys():
					if myleaguepokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = myleaguepokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
		
		print("\nWould you like to attack or switch your pokemon?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				myleaguepokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			print(str(list(myleaguepokemon.keys())))
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in myleaguepokemon.keys():
				currentpokemon = c
				currentpokemonhp = myleaguepokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")
			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			myleaguepokemon[currentpokemon][0] = currentpokemonhp

		else:
			print("Please enter your input correctly!")

def kevinbattle():
	global money
	global mymainpokemon
	global currentgym
	global myleaguepokemon
	global currentleaguetrainer
	global myleaguepokemon
	print("Your matchup is Kevin!\n")
	print("You have to pick 3 pokemon for the first few rounds to fight with you and each pokemon will be recharged fully after each battle!")
	print(str(list(mymainpokemon.keys())))
	lp = input("Please type in the name of the first pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your second pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the second pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your third pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the third pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now battle Kevin\n!")
	else:
		print("Please enter your input correctly!\n")
	acc = 0
	opponent = leaguepokemon[currentleaguetrainer][0]
	lastopponent = leaguepokemon[currentleaguetrainer][len(leaguepokemon[currentleaguetrainer])-1]
	opponenthp = pokemonhp[opponent]
	print("\nYou are going to battle "+currentleaguetrainer+"!")
	print(currentleaguetrainer+" sent out "+opponent)
	print("You sent out "+list(myleaguepokemon.keys())[0]+"!\n")
	currentpokemon = list(myleaguepokemon.keys())[0]
	currentpokemonhp = myleaguepokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 and opponent != lastopponent:
			print(opponent+" has fainted!")
			opponent = leaguepokemon[currentleaguetrainer][leaguepokemon[currentleaguetrainer].index(opponent)+1]
			mymainpokemon[currentpokemon][1] += 50
			myleaguepokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			print(currentleaguetrainer+" sent out "+opponent)
			opponenthp = pokemonhp[opponent]
		elif opponent == lastopponent and opponenthp <= 0:
			print("Congratulations!, you won the battle!\n")
			print("You earned $50 and are moving on to the next match!\n")
			mymainpokemon[currentpokemon][1] += 50
			mymainpokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			if currentleaguetrainer == "James":
				currentleaguetrainer = "Ethan"
			elif currentleaguetrainer == "Ethan":
				currentleaguetrainer = "Kevin"
			elif currentleaguetrainer == "Kevin":
				currentleaguetrainer = "Holt"
			elif currentleaguetrainer == "Holt":
				currentleaguetrainer= "Ray"
			for i in mymainpokemon.keys():
				mymainpokemon[i][0] = pokemonhp[i]
			money += 50
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in myleaguepokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle and the pokemon league is over!\n")
				shop()
				return
			while myleaguepokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in myleaguepokemon.keys():
					if myleaguepokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in myleaguepokemon.keys():
					if myleaguepokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = myleaguepokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
		
		print("\nWould you like to attack or switch your pokemon?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				myleaguepokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			print(str(list(myleaguepokemon.keys())))
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in myleaguepokemon.keys():
				currentpokemon = c
				currentpokemonhp = myleaguepokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")
			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			myleaguepokemon[currentpokemon][0] = currentpokemonhp

		else:
			print("Please enter your input correctly!")

def holtbattle():
	global money
	global mymainpokemon
	global currentgym
	global myleaguepokemon
	global currentleaguetrainer
	global myleaguepokemon
	print("Your matchup is Holt!\n")
	print("You have to pick 3 pokemon for the first few rounds to fight with you and each pokemon will be recharged fully after each battle!")
	print(str(list(mymainpokemon.keys())))
	lp = input("Please type in the name of the first pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your second pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the second pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now choose your third pokemon!")
	else:
		print("Please enter your input correctly!\n")
	lp = input("Please type in the name of the third pokemon you chose:")
	p = lp.split(" ")
	for i in p:
		p[p.index(i)] = i[0].upper()+i[1:len(i)]
	p = " ".join(p).strip()
	if p in mymainpokemon.keys():
		myleaguepokemon[p] = [pokemonhp[p], mymainpokemon[p][1]]
		print("You may now battle Holt\n!")
	else:
		print("Please enter your input correctly!\n")
	acc = 0
	opponent = leaguepokemon[currentleaguetrainer][0]
	lastopponent = leaguepokemon[currentleaguetrainer][len(leaguepokemon[currentleaguetrainer])-1]
	opponenthp = pokemonhp[opponent]
	print("\nYou are going to battle "+currentleaguetrainer+"!")
	print(currentleaguetrainer+" sent out "+opponent)
	print("You sent out "+list(myleaguepokemon.keys())[0]+"!\n")
	currentpokemon = list(myleaguepokemon.keys())[0]
	currentpokemonhp = myleaguepokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 and opponent != lastopponent:
			print(opponent+" has fainted!")
			opponent = leaguepokemon[currentleaguetrainer][leaguepokemon[currentleaguetrainer].index(opponent)+1]
			mymainpokemon[currentpokemon][1] += 50
			myleaguepokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			print(currentleaguetrainer+" sent out "+opponent)
			opponenthp = pokemonhp[opponent]
		elif opponent == lastopponent and opponenthp <= 0:
			print("Congratulations!, you won the battle!\n")
			print("You earned $50 and are moving on to the next match!\n")
			mymainpokemon[currentpokemon][1] += 50
			mymainpokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			if currentleaguetrainer == "James":
				currentleaguetrainer = "Ethan"
			elif currentleaguetrainer == "Ethan":
				currentleaguetrainer = "Kevin"
			elif currentleaguetrainer == "Kevin":
				currentleaguetrainer = "Holt"
			elif currentleaguetrainer == "Holt":
				currentleaguetrainer= "Ray"
			for i in mymainpokemon.keys():
				mymainpokemon[i][0] = pokemonhp[i]
			money += 50
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in myleaguepokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle and the pokemon league is over!\n")
				shop()
				return
			while myleaguepokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in myleaguepokemon.keys():
					if myleaguepokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in myleaguepokemon.keys():
					if myleaguepokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = myleaguepokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
		
		print("\nWould you like to attack or switch your pokemon?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				myleaguepokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			print(str(list(myleaguepokemon.keys())))
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in myleaguepokemon.keys():
				currentpokemon = c
				currentpokemonhp = myleaguepokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")
			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			myleaguepokemon[currentpokemon][0] = currentpokemonhp

		else:
			print("Please enter your input correctly!")

def raybattle():
	global money
	global mymainpokemon
	global currentgym
	global myleaguepokemon
	global currentleaguetrainer
	global myleaguepokemon
	print("Your matchup is Ray!\n")
	acc = 0
	myleaguepokemon = mymainpokemon
	print("You have reached the Semi-Finals!")
	print("You can now battle with all of your pokemon!")
	opponent = leaguepokemon[currentleaguetrainer][0]
	lastopponent = leaguepokemon[currentleaguetrainer][len(leaguepokemon[currentleaguetrainer])-1]
	opponenthp = pokemonhp[opponent]
	print("\nYou are going to battle "+currentleaguetrainer+"!")
	print(currentleaguetrainer+" sent out "+opponent)
	print("You sent out "+list(myleaguepokemon.keys())[0]+"!\n")
	currentpokemon = list(myleaguepokemon.keys())[0]
	currentpokemonhp = myleaguepokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 and opponent != lastopponent:
			print(opponent+" has fainted!")
			opponent = leaguepokemon[currentleaguetrainer][leaguepokemon[currentleaguetrainer].index(opponent)+1]
			mymainpokemon[currentpokemon][1] += 50
			myleaguepokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			print(currentleaguetrainer+" sent out "+opponent)
			opponenthp = pokemonhp[opponent]
		elif opponent == lastopponent and opponenthp <= 0:
			print("Congratulations!, you won the battle!\n")
			print("You earned $50 and are moving on to the next match!\n")
			mymainpokemon[currentpokemon][1] += 50
			mymainpokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			currentleaguetrainer = "Gray"
			money += 50
			for i in mymainpokemon.keys():
				mymainpokemon[i][0] = pokemonhp[i]
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in myleaguepokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle and the pokemon league is over!\n")
				shop()
				return
			while myleaguepokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in myleaguepokemon.keys():
					if myleaguepokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in myleaguepokemon.keys():
					if myleaguepokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = myleaguepokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
		
		print("\nWould you like to attack or switch your pokemon?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				myleaguepokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			print(str(list(myleaguepokemon.keys())))
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in myleaguepokemon.keys():
				currentpokemon = c
				currentpokemonhp = myleaguepokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")
			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			myleaguepokemon[currentpokemon][0] = currentpokemonhp

		else:
			print("Please enter your input correctly!")

def graybattle():
	global money
	global mymainpokemon
	global currentgym
	global myleaguepokemon
	global currentleaguetrainer
	global myleaguepokemon
	print("Your matchup is Gray!\n")
	acc = 0
	myleaguepokemon = mymainpokemon
	print("You have reached the Finals!")
	opponent = leaguepokemon[currentleaguetrainer][0]
	lastopponent = leaguepokemon[currentleaguetrainer][len(leaguepokemon[currentleaguetrainer])-1]
	opponenthp = pokemonhp[opponent]
	print("\nYou are going to battle "+currentleaguetrainer+"!")
	print(currentleaguetrainer+" sent out "+opponent)
	print("You sent out "+list(myleaguepokemon.keys())[0]+"!\n")
	currentpokemon = list(myleaguepokemon.keys())[0]
	currentpokemonhp = myleaguepokemon[currentpokemon][0]
	print(opponent+" has "+str(opponenthp)+"HP left.")
	print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
	while 1==1:
		if opponenthp <= 0 and opponent != lastopponent:
			print(opponent+" has fainted!")
			opponent = leaguepokemon[currentleaguetrainer][leaguepokemon[currentleaguetrainer].index(opponent)+1]
			mymainpokemon[currentpokemon][1] += 50
			myleaguepokemon[currentpokemon][1] += 50
			print(currentpokemon+" earned 50 XP!\n")
			print(currentleaguetrainer+" sent out "+opponent)
			opponenthp = pokemonhp[opponent]
		elif opponent == lastopponent and opponenthp <= 0:
			print("Congratulations!, you won the battle and the Pokemon League!\n")
			print("You earned $1000 and are the new champion!\n")
			mymainpokemon[currentpokemon][1] += 500
			mymainpokemon[currentpokemon][1] += 500
			print(currentpokemon+" earned 500 XP!\n")
			money += 1000
			for i in mymainpokemon.keys():
				mymainpokemon[i][0] = pokemonhp[i]
			return
		elif currentpokemonhp <= 0:
			print(currentpokemon+" has fainted!!!\n")
			for i in myleaguepokemon.values():
				if i[0] <= 0:
					acc+=1
			if acc == len(list(mymainpokemon.keys())):
				print("All your pokemon have fainted!")
				print("You lost the battle and the pokemon league is over!\n")
				shop()
				return
			while myleaguepokemon[currentpokemon][0] <= 0:
				print("What pokemon do you choose?\n")
				for i in myleaguepokemon.keys():
					if myleaguepokemon[i][0] > 0:
						print(i)
				p = input("\nPlease type in the name of the pokemon:")
				p = p.split(" ")
				for i in p:
					p[p.index(i)] = i[0].upper()+i[1:len(i)]
				p = " ".join(p).strip()
				if p in myleaguepokemon.keys():
					if myleaguepokemon[p][0] <= 0:
						print(p+" has fainted already!\n")
					else:
						currentpokemon = p
						currentpokemonhp = myleaguepokemon[currentpokemon][0]
						print("You sent out "+currentpokemon+"!\n")
				else:
					print("Please enter your input correctly!\n")
		
		print("\nWould you like to attack or switch your pokemon?\n")
		play = input("Type 1 to attack and 2 to switch your pokemon:")
		if play == "1":
			print("What move would you like to use?\n")
			print(str(pokemonmoves[currentpokemon]))
			p = input("\nPlease type in the name of the move you want to use, for example, "+str(pokemonmoves[currentpokemon][0])+":")
			p = p.split(" ")
			for i in p:
				p[p.index(i)] = i[0].upper()+i[1:len(i)]
			p = " ".join(p).strip()
			if p in moveattackpower.keys():
				print(currentpokemon+" used "+p+"!")
				if pokemontype[opponent] in typeadvantages[movetype[p]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp += moveattackpower[p]*2
						print("It was super effective!")
						print("You gained "+str(moveattackpower[p]*2)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*2
						currentpokemonhp = 0
						print("It was super effective!")
					else:
						opponenthp -= moveattackpower[p]*2
						print("It was super effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			
				elif movetype[p] in typeadvantages[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp += moveattackpower[p]*0.5
						print("It was not effective!")
						print("You gained "+str(moveattackpower[p]*0.5)+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]*0.5
						currentpokemonhp = 0
						print("It was not effective!")
					else:
						opponenthp -= moveattackpower[p]*0.5
						print("It was not effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")
						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				elif movetype[p] in noadvantagetypes[pokemontype[opponent]]:
					if p == "Absorb":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == "Mega Drain":
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Giga Drain':
						opponenthp -= moveattackpower[p]
						currentpokemonhp += moveattackpower[p]
						print("It was effective!")
						print("You gained "+str(moveattackpower[p])+"HP!\n")
					elif p == 'Explosion':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					elif p == 'Self-Destruct':
						opponenthp -= moveattackpower[p]
						currentpokemonhp = 0
						print("It was effective!")
					else:
						opponenthp -= moveattackpower[p]
						print("It was effective!\n")

					if opponenthp > 0:
						opponentmove = random.choice(pokemonmoves[opponent])

						print(opponent+" used "+opponentmove+"!")

						if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp += moveattackpower[opponentmove]*0.5
								print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*0.5
							print("It was not effective!\n")
								
						elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp += moveattackpower[opponentmove]*2
								print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]*2
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]*2
							print("It was super effective!\n")

						else:
							if opponentmove == "Absorb":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == "Mega Drain":
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Giga Drain':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp += moveattackpower[opponentmove]
								print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

							elif opponentmove == 'Explosion':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0

							elif opponentmove == 'Self-Destruct':
								currentpokemonhp -= moveattackpower[opponentmove]
								opponenthp = 0
								
							else:
								currentpokemonhp -= moveattackpower[opponentmove]
							print("It was effective!\n")
						print(opponent+" has "+str(opponenthp)+"HP left.")
						print("Your "+currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
					else:
						pass
				else:
					print("Please enter your input correctly!\n")
				myleaguepokemon[currentpokemon][0] = currentpokemonhp
			else:
				print("Please type in your input correctly\n")

		elif play == "2":
			print("Here are your pokemon:\n")
			print(str(list(myleaguepokemon.keys())))
			print("\nType in the name of the pokemon that you want to send out! \n")
			c = input("Please type in the name of the pokemon:")
			c = c.split(" ")
			for i in c:
				c[c.index(i)] = i[0].upper()+i[1:len(i)]
			c = " ".join(c).strip()
			if c in myleaguepokemon.keys():
				currentpokemon = c
				currentpokemonhp = myleaguepokemon[currentpokemon][0]
				print("You sent out "+currentpokemon+"!\n")
			else:
				print("Please enter your input correctly!\n")

			print(opponent+" has "+str(opponenthp)+"HP left.")
			print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")

			if opponenthp > 0:
				opponentmove = random.choice(pokemonmoves[opponent])

				print(opponent+" used "+opponentmove+"!\n")
				
				if movetype[opponentmove] in typeadvantages[pokemontype[currentpokemon]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp += moveattackpower[opponentmove]*0.5
						print(opponent+" gained "+str(moveattackpower[opponentmove]*0.5)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*0.5
					print("It was not effective!\n")
						
				elif pokemontype[currentpokemon] in typeadvantages[movetype[opponentmove]]:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp += moveattackpower[opponentmove]*2
						print(opponent+" gained "+str(moveattackpower[opponentmove]*2)+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]*2
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]*2
					print("It was super effective!\n")

				else:
					if opponentmove == "Absorb":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == "Mega Drain":
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Giga Drain':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp += moveattackpower[opponentmove]
						print(opponent+" gained "+str(moveattackpower[opponentmove])+"HP!\n")

					elif opponentmove == 'Explosion':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0

					elif opponentmove == 'Self-Destruct':
						currentpokemonhp -= moveattackpower[opponentmove]
						opponenthp = 0
						
					else:
						currentpokemonhp -= moveattackpower[opponentmove]
					print("It was effective!\n")

				print(opponent+" has "+str(opponenthp)+"HP left.")
				print(currentpokemon+" has "+str(currentpokemonhp)+"HP left.\n")
			else:
				pass
			
			myleaguepokemon[currentpokemon][0] = currentpokemonhp

		else:
			print("Please enter your input correctly!")
			



while len(mymainpokemon.keys()) <= 5:
	if len(gymbadges) == 8 and currentgym == "Pokemon League":
		print("\nYou are eligible for the Pokemon League!\n")
		pri = input("If you want to register type 'y', if you don't want to register type 'n':")
		if pri=="y":
			jamesbattle()
			ethanbattle()
			kevinbattle()
			holtbattle()
			raybattle()
			graybattle()
		else:
			pass

	firstevolution()
	finalevolution()
	x = input("If you want to go into the wilderness, type '1', if you want to go to the pokemon center, type '2', if you want to view your data, type '3', if you want to leave one of your pokemon, type '4' and if you want to challenge the local gym type '5':")
	if x=="1":
		battle()
	elif x=="2":
		shop()
	elif x=="3":
		data()
	elif x=="4":
		print("\n"+str(list(mymainpokemon.keys()))+"\n")
		i = input("What pokemon would you like to let go, please type in the name of the pokemon, if you want to quit type 'q':")
		p = i.split(" ")
		for i in p:
			p[p.index(i)] = i[0].upper()+i[1:len(i)]
		p = " ".join(p).strip()
		if p in mymainpokemon.keys():
			if len(mymainpokemon.keys()) > 0:
				mymainpokemon.pop(p)
				print("You let go of "+p+" and it was released back into the wilderness!\n")
			else:
				print("You cannot let go of your last pokemon!\n")
		elif p == 'q':
			pass
		else:
			print("Please enter your input correctly!\n")
	elif x=="5":
		gymbattle()
	else:
		print("Please enter your input correctly!\n")

input("\n\nAt Professors Oak's lab...\n\n")

input("Professor Oak: Since you came back, I wanted you to have this...\n")

input("Professor Oak: I wanted you to have one of these evolution stones...\n")

input("Professor Oak: I have a Thunder Stone, a Moon Stone, a Leaf Stone, a Fire Stone and a Water Stone, with me and I want you to have one of them!\n")

freep = input("If you choose the Thunder Stone, type '1', if you choose the Moon Stone, type '2', if you choose the Leaf Stone, type '3', if you choose the Fire Stone, type '4', if you choose the Water Stone, type '5':")

if freep == '1':
	inventory.append("Thunder Stone")
	print("You got a Thunder Stone!\n")
	time.sleep(2)

elif freep == '2':
	inventory.append("Moon Stone")
	print("You got a Moon Stone!\n")
	time.sleep(2)

elif freep == '3':
	inventory.append("Leaf Stone")
	print("You got a Leaf Stone!\n")
	time.sleep(2)

elif freep == '4':
	inventory.append("Fire Stone")
	print("You got a Fire Stone!\n")
	time.sleep(2)

elif freep == '5':
	inventory.append("Water Stone")
	print("You got a Water Stone!\n")
	time.sleep(2)

input("Professor Oak: That was a good choice, now you may continue your journey!\n")


while len(pokemon1) != len(mypokedex):
	if len(gymbadges) == 8 and currentgym == "Pokemon League":
		print("\nYou are eligible for the Pokemon League!\n")
		pri = input("If you want to register type 'y', if you don't want to register type 'n':")
		if pri=="y":
			jamesbattle()
			ethanbattle()
			kevinbattle()
			holtbattle()
			raybattle()
			graybattle()
		else:
			pass
	firstevolution()
	finalevolution()
	x = input("If you want to go into the wilderness, type '1', if you want to go to the pokemon center, type '2', if you want to view your data, type '3', if you want to leave one of your pokemon, type '4' and if you want to challenge the local gym type '5':")
	if x=="1":
		battle()
	elif x=="2":
		shop()
	elif x=="3":
		data()
	elif x=="4":
		print("\n"+str(list(mymainpokemon.keys()))+"\n")
		i = input("What pokemon would you like to let go, please type in the name of the pokemon, if you want to quit type 'q':")
		p = i.split(" ")
		for i in p:
			p[p.index(i)] = i[0].upper()+i[1:len(i)]
		p = " ".join(p).strip()
		if p in mymainpokemon.keys():
			mymainpokemon.pop(p)
			print("You let go of "+p+"!\n")
		elif p=="q":
			pass
		else:
			print("Please enter your input correctly!\n")
	elif x=="5":
		gymbattle()
	else:
		print("Please enter your input correctly!\n")
print("\n\nAt Professor Oak's Lab...\n\n")
time.sleep(2)
print("Professor Oak: "+name+" you have succesfully collected data on every first evolution pokemon which means that I can take them in for observation.\n")
time.sleep(3)
print("Professor Oak: You have been a great help! Thank you.\n\n")
time.sleep(2)
print("GAME OVER")
exit()