import json


with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for entry in data:
    dn = entry['DN']
    description = entry.get('Description', '')
    speed = entry.get('Speed', 'inherit')
    mtu = entry.get('MTU', '')
    print("{:<50} {:<20} {:<8} {:<8}".format(dn, description, speed, mtu))
