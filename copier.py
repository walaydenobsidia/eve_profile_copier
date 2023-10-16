import yaml
import shutil
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, dest="path", default=os.environ.get("EVE_ONLINE_SETTINGS_FOLDER"))
    parser.add_argument("--config", type=str, dest="config", default="config.yaml")
    args = parser.parse_args()
    return args

def backup_config(cfg):
    original_filename = f"{args.path}/core_user_{cfg['user_id']}.dat"
    new_filename = f"{args.path}/core_user_{cfg['user_id']}.dat.bkp"
    if original_filename != new_filename:
        print(f"Backing up {original_filename} to {new_filename}")
        shutil.copyfile(original_filename, new_filename)

    original_filename = f"{args.path}/core_char_{cfg['char_id']}.dat"
    new_filename = f"{args.path}/core_char_{cfg['char_id']}.dat.bkp"
    if original_filename != new_filename:
        print(f"Backing up {original_filename} to {new_filename}")
        shutil.copyfile(original_filename, new_filename)

def copy_config(source, target):
    original_filename = f"{args.path}/core_user_{source['user_id']}.dat"
    new_filename = f"{args.path}/core_user_{target['user_id']}.dat"
    if original_filename != new_filename:
        print(f"Copying {original_filename} to {new_filename}")
        shutil.copyfile(original_filename, new_filename)

    original_filename = f"{args.path}/core_char_{source['char_id']}.dat"
    new_filename = f"{args.path}/core_char_{target['char_id']}.dat"
    if original_filename != new_filename:
        print(f"Copying {original_filename} to {new_filename}")
        shutil.copyfile(original_filename, new_filename)

def main():
    with open(args.config, "r") as cfg_file:
        cfg = yaml.full_load(cfg_file)
    source = cfg["source"]

    backup_config(source)
    for target in cfg["targets"]:
        backup_config(target)
        copy_config(source, target)

if __name__ == "__main__":
    args = parse_args()
    assert args.path is not None
    main()