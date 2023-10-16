# Eve Online Profile Copier
A simple python script for replicating the UI profile settings -- which are stored locally -- from one character to other characters, on the same or different accounts.

## Prerequisites
The script is written in Python, therefore you will need a Python interpreter on your system.  There are very few requirements, since this is just doing simple local file copying.  Best practice is to instantiate a new virtual environment, and install dependencies there rather than system wide -- documentation for creating and managing virtual environments is readily googleable.

```bash
python3 -m pip install -r requirements.txt
```

## Usage
```bash
python copier.py [--path ABSOLUTE_PATH_TO_EVE_PROFILE_SETTINGS_FOLDER] [--config RELATIVE_PATH_TO_CONFIG_YAML_FILE]
```

`--path` is optional, but if it not specified, it will expect an environment variable named `EVE_ONLINE_SETTINGS_FOLDER` to be populated instead. When running on a Windows machine, the backslashes in the path must be escaped. This is why you see `\\` in the example above. YMMV for the appropriate way to reference file paths in your system.

`--config` is optional, and if not specified, the script will assume `config.yaml` exists in the working directory.

### Example
```bash
python copier.py --path C:\\Users\\mywindowsusername\\AppData\\Local\\CCP\\EVE\\c_ccp_eve_online_tq_tranquility\\settings_Default --config config.yaml
```

## Configuration
A YAML config file is expected by the script, and its structure should look like this:
```yaml
source:
  # Walayden Obsidia
  char_id: 742818745
  user_id: 1234
targets:
  # Tony Stark
  - char_id: 98765432
    user_id: 1234
  # Bruce Wayne
  - char_id: 24681012
    user_id: 4567
```

**To identify your user_id**, log out of all eve clients, then open a client for a single account.  Now check the settings folder and look for the `core_user_########.dat` file that should have just modified just now.  That number is your user_id.  Repeat this process for each account you wish to sync from or to.

**To get your user_ids**, there are a few different options:
* Log into each user, one at a time, and look for the modified `core_char_##########.dat` file.  The number is your user_id.
* Check **zkillboard** for your character.  The URL for your character includes a number.  This number is your user_id.  This will not work if you've never involved in a killmail (on either end).
* Use **ESI**.  Visit https://esi.evetech.net/ui/, and scroll down to the information about /universe/ids.  Click on "Try it out".  You should then see a form with a textarea called `names` and a default value of:
    ```json
    [
        "CCP Zoetrope"
    ]
    ```
    Modify this to be a list of your character names, e.g.:
    ```json
    [
        "CCP Zoetrope",
        "Walayden Obsidia"
    ]
    ```
    ESI will respond with a JSON object containing whatever it was able to map, to its ID.  This works for Characters, NPC Structures, Items, Systems, Regions, and basically everything else that exists.
    ```json
    {
        "characters": [
            {
            "id": 2112625428,
            "name": "CCP Zoetrope"
            },
            {
            "id": 742818745,
            "name": "Walayden Obsidia"
            }
        ]
    }
    ```

Happy Syncing!