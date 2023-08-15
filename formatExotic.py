import json
import sys
import os

def format_exotic_data(player):
    # Read the raw API JSON file
    api_json_path = f'static/data/playerExoticData/{player}Exotics.json'
    
    if not os.path.exists(api_json_path):
        print(f"Error: {api_json_path} not found.")
        return
    
    with open(api_json_path, 'r') as api_file:
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
    formatted_json_path = f'static/data/formattedPlayerExoticData/formatted{player.capitalize()}Exotics.json'
    existing_exotic_data = {}

    if os.path.exists(formatted_json_path):
        with open(formatted_json_path, 'r') as exotic_file:
            existing_exotic_data = json.load(exotic_file)

    # Update the existing exotic data with the new values
    for exotic in existing_exotic_data.get('exoticWeapons', []):
        reference_id = exotic.get('referenceID')
        updated_entry = updated_exotic_data.get(reference_id)
        if updated_entry:
            exotic['kills'] = updated_entry['kills']
            exotic['precision'] = updated_entry['precision']

    # Write the updated exotic data back to the JSON file
    with open(formatted_json_path, 'w') as exotic_file:
        json.dump(existing_exotic_data, exotic_file, indent=2)

    print(f"Exotic data updated for {player}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python formatExotic.py <player>")
    else:
        player = sys.argv[1]
        format_exotic_data(player)
