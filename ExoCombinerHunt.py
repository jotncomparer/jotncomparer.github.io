import json

# Read the raw API JSON file
with open('hunterExotics.json', 'r') as api_file:
    raw_api_data = json.load(api_file)

# Create a dictionary to hold the updated exotic data
updated_exotic_data = {}

# Iterate through each weapon in the raw API data
for response_item in raw_api_data['Response']:
    for weapon in response_item['weapons']:
        reference_id = str(weapon['referenceId'])
        kills = weapon['values']['uniqueWeaponKills']['basic']['value']
        precision = weapon['values']['uniqueWeaponPrecisionKills']['basic']['value']
        
        if reference_id in updated_exotic_data:
            updated_exotic_data[reference_id]['kills'] += kills
            updated_exotic_data[reference_id]['precision'] += precision
        else:
            name = "Unknown"  # You might need to map referenceId to names if available
            updated_exotic_data[reference_id] = {
                'name': name,
                'kills': kills,
                'precision': precision
            }

# Read the existing exotic data JSON file
with open('formattedHunterExotics.json', 'r') as exotic_file:
    existing_exotic_data = json.load(exotic_file)

# Update the existing exotic data with the new values
for exotic in existing_exotic_data['exoticWeapons']:
    reference_id = exotic['referenceID']
    updated_entry = updated_exotic_data.get(reference_id)
    if updated_entry:
        exotic['kills'] = updated_entry['kills']
        exotic['precision'] = updated_entry['precision']

# Write the updated exotic data back to the JSON file
with open('formattedHunterExotics.json', 'w') as exotic_file:
    json.dump(existing_exotic_data, exotic_file, indent=2)

print("Exotic data updated.")
