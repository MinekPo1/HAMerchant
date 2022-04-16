import csv
import base_types as _
from items import items
import merchants

with open('dump.csv', 'w', newline='') as csvfile:
	field_names = ["name", *[i.__name__ for i in merchants.all_merchants]]
	dumper = csv.DictWriter(csvfile, fieldnames=field_names)
	dumper.writeheader()

	for name,item in items.items():
		row = {
			"name": name
		}
		row.update({m.__name__: m.get_chance(item) for m in merchants.all_merchants})

		dumper.writerow(row)
