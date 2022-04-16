from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass
from typing import ClassVar, Mapping, Type, Any
import random
items: dict[str,Item] | None = None


class ItemCategory(Enum):
	Armor                  = auto()
	Armor_Accessories      = auto()
	Clothing               = auto()
	Clothing_Materials     = auto()
	Farm_Accessories       = auto()
	Farm_Tools             = auto()
	Farmable               = auto()
	Food                   = auto()
	Food_Accessories       = auto()
	Furniture              = auto()
	Harvested_Item         = auto()
	Houses                 = auto()
	Mining_Accessories     = auto()
	Mining_Tools           = auto()
	Mob_Drops              = auto()
	Ores                   = auto()
	Paintbrush_Accessories = auto()
	Paintbrushes           = auto()
	Potion_Accessories     = auto()
	Potions                = auto()
	Ranger_Accessories     = auto()
	Refined_Materials      = auto()
	Stamps                 = auto()
	Traps                  = auto()
	Uprooted_Trees         = auto()
	Weapon_Accessories     = auto()
	Weapons                = auto()
	Any                    = auto()
	DevOnly                = auto()
	Random = Any

	def __getitem__(self, v: slice):
		return ItemCategoryPeek(
			self, range(*(i for i in (v.start, v.stop, v.step) if i is not None))
		)


class ItemCategoryPeek:
	def __init__(self, category: ItemCategory, range: range):
		self.category = category
		self.range = range

	def get(self):
		if self.category == ItemCategory.Any:
			items = filter(lambda i: i.category != ItemCategory.DevOnly and i.price in self.range, Item.subclasses)
		else:
			items = filter(
				lambda i: i.category == self.category and i.price in self.range,
				Item.subclasses
			)
		return random.choice(list(items)).get()

	def get_chance(self,item: type[Item] | Item) -> float:
		if isinstance(item, Item):
			item = type(item)
		if self.category == ItemCategory.Any:
			items = filter(lambda i: i.price in self.range, Item.subclasses)
		else:
			items = filter(
				lambda i: i.category == self.category and i.price in self.range,
				Item.subclasses
			)
		l = list(items)
		if item in l:
			return 1/len(l)
		return 0


class Paint(Enum):
	Basic_Brown     = auto()
	Basic_White     = auto()
	Basic_Cyan      = auto()
	Pinewood        = auto()
	Basic_Yellow    = auto()
	Basic_Blue      = auto()
	Basic_Green     = auto()
	Basic_Red       = auto()
	Basic_Pink      = auto()
	Olive_Green     = auto()
	Spirit_Grey     = auto()
	Basic_Orange    = auto()
	Basic_Black     = auto()
	Basic_Purple    = auto()
	Banana_Bruise   = auto()
	Winter_Pastel   = auto()
	Banana_Dessert  = auto()
	Storm_Grey      = auto()
	Royal_Red       = auto()
	Candycane       = auto()
	Nomad_Red       = auto()
	Royal_Sage      = auto()
	Gold_Leaf       = auto()
	Lavender_Bloom  = auto()
	Lavender_Plum   = auto()
	Mystic_Dusk     = auto()
	Forest_Green    = auto()
	Mystic_Dawn     = auto()
	Marble_White    = auto()
	Lumberjack      = auto()
	Scottish_Green  = auto()
	Titanium_Trim   = auto()
	Black_n_Gold    = auto()
	Flaming_Orange  = auto()

	def __add__(self, other: Stamp) -> PaintAndStamp:
		return PaintAndStamp(self, other)


class Stamp(Enum):
	Food_Stamp      = auto()
	Paw_Stamp       = auto()
	Feather_Stamp   = auto()
	Sun_Stamp       = auto()
	Swords_Stamp    = auto()
	Coins_Stamp     = auto()
	Fashion_Stamp   = auto()
	Potion_Stamp    = auto()
	Egg_Stamp       = auto()
	Flower_Stamp    = auto()
	Crown_Stamp     = auto()
	Furniture_Stamp = auto()
	Skull_Stamp     = auto()
	Snowflake_Stamp = auto()
	Dragon_Stamp    = auto()

	def __add__(self, other: Paint) -> PaintAndStamp:
		return PaintAndStamp(other, self)


@dataclass
class PaintAndStamp:
	paint: Paint | None = None
	stamp: Stamp | None = None


class Item:
	subclasses: ClassVar[list[Type[Item]]] = []
	name:      ClassVar[str]
	price:     ClassVar[int]
	category:  ClassVar[ItemCategory]
	max_stack: ClassVar[int]  = 1
	paintable: ClassVar[bool] = False

	paint_and_stamp: PaintAndStamp | None = None
	count: int

	def __init__(
		self, count: int = 1,
		paint_and_stamp: Paint | Stamp | PaintAndStamp | None = None
	):
		self.count = count
		if isinstance(paint_and_stamp, PaintAndStamp):
			self.paint_and_stamp = paint_and_stamp
		elif isinstance(paint_and_stamp, Paint):
			self.paint_and_stamp = PaintAndStamp(paint_and_stamp, None)
		elif isinstance(paint_and_stamp, Stamp):
			self.paint_and_stamp = PaintAndStamp(None, paint_and_stamp)

	@classmethod
	def get(cls):
		if cls.paintable:
			paint = random.choice(list(filter(
				lambda i: isinstance(i,Paint),
				Paint.__dict__.values()
			)))
		else:
			paint = None
		return cls(random.randint(1, cls.max_stack), paint)

	@classmethod
	def __init_subclass__(cls) -> None:
		Item.subclasses.append(cls)

	@classmethod
	def subclass_factory(
		cls, i_name: str, i_price: int, i_category: ItemCategory,
		i_paintable: bool = False, i_max_stack: int = 1
	):
		class Subclass(cls):  # type:ignore
			name = i_name
			price = i_price
			category = i_category
			paintable = i_paintable
			max_stack = i_max_stack
		Subclass.__name__ = i_name.replace(" ","_")
		Subclass.__qualname__ = i_name.replace(" ","_")
		return Subclass

	def __repr__(self) -> str:
		out = f"{self.__class__.__name__}"
		if self.max_stack != 1:
			out = f"{self.count} {out}"
		if self.paint_and_stamp:
			out += f":{self.paint_and_stamp}"
		return f"<{out}>"


class MerchantMeta(type):
	@classmethod
	def __prepare__(cls, __name: str, __bases: tuple[type, ...], **kwds: Any)\
			-> Mapping[str, object]:
		# don't do anything if we're not a subclass of Merchant
		if cls.__name__ == "Merchant":
			return {}
		buys = 0

		class Namespace(dict):
			def __setitem__(self, __k: str, __v: Any) -> None:
				global items
				nonlocal buys
				if items is None:
					from items import items

				if __k == "buy":
					__k = f"__buy_{buys}"
					buys += 1
					if isinstance(__v, str):
						__v = items[__v]  # type:ignore
				super().__setitem__(__k, __v)

		return Namespace()


class Merchant(metaclass=MerchantMeta):
	sell_percent: ClassVar[float]
	sell_category: ClassVar[ItemCategory | None]
	__buy_slots__: ClassVar[tuple[ItemCategoryPeek | Type[Item]]]

	@classmethod
	def __init_subclass__(cls, final:bool = True) -> None:
		if not final:
			return
		if not hasattr(cls, 'sell_percent'):
			cls.sell_percent = 0.26
		if not hasattr(cls, 'sell_category'):
			cls.sell_category = None
		buy_slots = tuple(filter(
			lambda i: isinstance(i, ItemCategoryPeek)  # type:ignore
				or isinstance(i,type) and issubclass(i, Item),
			cls.__dict__.values()
		))
		cls.__buy_slots__ = buy_slots  # type:ignore

	def __init__(self) -> None:
		self.buy_slots = [i.get() for i in self.__buy_slots__]

	def __repr__(self) -> str:
		return f'<Merchant {self.__class__.__name__}>'

	@classmethod
	def get_chance(cls,item: type[Item] | Item) -> float:
		if isinstance(item, Item):
			item = type(item)
		chance = 0.0
		for i in cls.__buy_slots__:
			if isinstance(i, ItemCategoryPeek):
				chance += i.get_chance(item) * (1 - chance)
			elif isinstance(i, type) and issubclass(i, Item):
				if item == i:
					chance += 1 * (1 - chance)
		return chance
