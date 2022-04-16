from base_types import ItemCategory as IC, Merchant
from typing import Type


class BoneJuice(Merchant):
	sell_percent = 0.26

	buy = "Bone Juice"


class SellOnly(Merchant):
	sell_percent = 0.03


class SellOnly2(Merchant):
	sell_percent = 0.12


class Clothing(Merchant):
	sell_percent = 0.26

	buy = "Loom"
	buy = IC.Clothing[1:999]
	buy = IC.Clothing[1:999]

	buy = IC.Clothing[1:999]
	buy = IC.Clothing[1:999]
	buy = IC.Clothing[1:999]

	buy = IC.Clothing_Materials[1:200]
	buy = IC.Clothing_Materials[1:200]
	buy = "Armor Display"


class Clothing2(Merchant):
	sell_percent = 0.26

	buy = "Loom"
	buy = IC.Clothing[1:5000]
	buy = IC.Clothing[1:5000]

	buy = IC.Clothing[1:5000]
	buy = IC.Clothing[1:5000]
	buy = IC.Clothing[1:5000]

	buy = IC.Clothing_Materials[1:200]
	buy = IC.Clothing_Materials[1:200]
	buy = "Armor Display"


class Eggs(Merchant):
	sell_percent = 0.26

	buy = "Egg Fuser"
	buy = "Uranium Bar"
	buy = "Egg"

	buy = "Egg"
	buy = "Egg"
	buy = "Egg"


class Food(Merchant):
	sell_percent = 0.26

	buy = IC.Food_Accessories[1:700]
	buy = IC.Food[1:200]
	buy = IC.Food[1:200]

	buy = IC.Food[1:200]
	buy = IC.Food[1:200]
	buy = IC.Harvested_Item[1:200]


class Furniture(Merchant):
	sell_percent = 0.26

	buy = "Builder Tools"
	buy = IC.Houses[1:100]
	buy = IC.Houses[1:1500]

	buy = "Basic Rug"
	buy = IC.Furniture[1:350]
	buy = IC.Furniture[1:350]

	buy = IC.Furniture[1:350]
	buy = IC.Furniture[1:350]
	buy = IC.Furniture[1:350]

	buy = IC.Paintbrushes[1:150]
	buy = IC.Stamps[1:100]


class Furniture2(Merchant):
	sell_percent = 0.26

	buy = "Builder Tools"
	buy = IC.Houses[1:5500]
	buy = IC.Houses[1:5500]

	buy = "Basic Rug"
	buy = IC.Furniture[1:5000]
	buy = IC.Furniture[1:5000]

	buy = IC.Furniture[1:5000]
	buy = IC.Furniture[1:5000]
	buy = IC.Furniture[1:5000]

	buy = IC.Paintbrushes[1:500]
	buy = IC.Stamps[1:300]


class Mining(Merchant):
	sell_percent = 0.26

	buy = IC.Mining_Tools[1:400]
	buy = IC.Mining_Tools[1:400]
	buy = IC.Ores[1:300]

	buy = IC.Ores[1:300]
	buy = IC.Ores[1:300]
	buy = IC.Ores[1:300]

	buy = IC.Refined_Materials[1:350]
	buy = IC.Mining_Accessories[1:2000]


class Mining2(Merchant):
	sell_percent = 0.26

	buy = IC.Mining_Tools[1:2000]
	buy = IC.Mining_Tools[1:2000]
	buy = IC.Ores[1:1000]

	buy = IC.Ores[1:1000]
	buy = IC.Ores[1:1000]
	buy = IC.Ores[1:1000]

	buy = IC.Refined_Materials[1:1000]
	buy = IC.Mining_Accessories[1:5000]


class Organic(Merchant):
	sell_percent = 0.26

	buy = IC.Farm_Tools[1:500]
	buy = IC.Farmable[1:400]
	buy = IC.Farmable[1:400]

	buy = IC.Harvested_Item[1:350]
	buy = IC.Harvested_Item[1:350]
	buy = IC.Harvested_Item[1:350]

	buy = IC.Mob_Drops[1:200]
	buy = IC.Uprooted_Trees[1:200]


class PaintbrushesAndStamps(Merchant):
	sell_percent = 0.26

	buy = "Paint Thinner"
	buy = IC.Paintbrushes[1:200]
	buy = IC.Paintbrushes[1:200]

	buy = IC.Paintbrushes[1:200]
	buy = IC.Stamps[1:100]
	buy = IC.Stamps[1:100]

	buy = IC.Paintbrush_Accessories[1:500]
	buy = "Stamp Maker"


class PaintbrushesAndStamps2(Merchant):
	sell_percent = 0.26

	buy = "Paint Thinner"
	buy = IC.Paintbrushes[1:600]
	buy = IC.Paintbrushes[1:600]

	buy = IC.Paintbrushes[1:600]
	buy = IC.Stamps[1:400]
	buy = IC.Stamps[1:400]

	buy = IC.Paintbrush_Accessories[1:3000]
	buy = "Stamp Maker"


class Paintings(Merchant):
	sell_percent = 0.26

	buy = "Painting Easel"
	buy = "Blank Canvas"
	buy = "Painting"

	buy = "Painting"
	buy = "Painting"
	buy = "Painting"


class Potions(Merchant):
	sell_percent = 0.26

	buy = IC.Potion_Accessories[1:500]
	buy = IC.Potions[1:700]
	buy = IC.Potions[1:700]

	buy = IC.Potions[1:700]
	buy = IC.Food[1:200]
	buy = IC.Food[1:200]

	buy = IC.Harvested_Item[1:500]


class Random(Merchant):
	sell_percent = 0.06

	buy = IC.Random[1:1000]
	buy = IC.Random[1:1000]
	buy = IC.Random[1:1000]

	buy = IC.Random[1:1000]
	buy = IC.Random[1:1000]
	buy = IC.Random[1:1000]


class Random2(Merchant):
	sell_percent = 0.06

	buy = IC.Random[1:5000]
	buy = IC.Random[1:5000]
	buy = IC.Random[1:5000]

	buy = IC.Random[1:5000]
	buy = IC.Random[1:5000]
	buy = IC.Random[1:5000]


class Ranger(Merchant):
	sell_percent = 0.26

	buy = IC.Ranger_Accessories[1:400]
	buy = IC.Food[1:200]
	buy = IC.Food[1:200]

	buy = IC.Mob_Drops[1:99]
	buy = IC.Mob_Drops[1:99]
	buy = IC.Harvested_Item[1:99]


class Records(Merchant):
	sell_percent = 0.26

	buy = "Music Box"
	buy = "Blank Record"
	buy = "Saved Record"

	buy = "Saved Record"
	buy = "Saved Record"
	buy = "Saved Record"


class Traps(Merchant):
	sell_percent = 0.26

	buy = IC.Traps[1:3000]
	buy = IC.Traps[1:3000]
	buy = IC.Traps[1:3000]


class WeaponsAndArmor(Merchant):
	sell_percent = 0.26

	buy = IC.Weapons[1:3000]
	buy = IC.Weapons[1:3000]
	buy = IC.Weapons[1:3000]

	buy = IC.Armor[1:3000]
	buy = IC.Armor[1:3000]
	buy = IC.Armor[1:3000]

	buy = IC.Refined_Materials[1:200]
	buy = IC.Refined_Materials[1:200]
	buy = IC.Weapon_Accessories[1:700]

	buy = IC.Armor_Accessories[1:700]


class WeaponsAndArmor2(Merchant):
	sell_percent = 0.26

	buy = IC.Weapons[500:40000]
	buy = IC.Weapons[500:40000]
	buy = IC.Armor[500:40000]

	buy = IC.Armor[500:40000]
	buy = IC.Refined_Materials[1:1000]
	buy = IC.Weapon_Accessories[1:2000]

	buy = IC.Armor_Accessories[1:2000]


all_merchants: list[Type[Merchant]] = [
	BoneJuice, SellOnly, SellOnly2, Clothing, Clothing2, Eggs, Food, Furniture,
	Furniture2, Mining, Mining2, Organic, PaintbrushesAndStamps,
	PaintbrushesAndStamps2,Paintings, Potions, Random, Random2, Ranger, Records, Traps, WeaponsAndArmor, WeaponsAndArmor2
]
"all of the merchants (defined above)"
