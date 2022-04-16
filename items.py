import csv
import base_types as types

csv.DictReader(open('items.csv'))

items = {
	row["Name"]: types.Item.subclass_factory(
		row["Name"], int(row["Price"]),
		types.ItemCategory[row["Category"].replace(" ", "_")],
		row["Paintable"] == "True", int(row["MaxStack"]))
	for row in csv.DictReader(open('items.csv'))
}
