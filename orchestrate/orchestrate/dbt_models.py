import os, subprocess
from pathlib import Path

from dagster import AssetExecutionContext, asset
from dagster_dbt import DbtCliResource, dbt_assets
# from .extract import download_and_extract_from_blob
import time

import platform

if platform.system() == 'Windows':
    python_version = 'python'
else:
    python_version = 'python3'


# download_and_extract_from_blob()
time.sleep(10)
wd = os.path.join(os.getcwd(), "loadcsv")
# wd = os.path.join(
#             dir_path, "home/runner/work/data_transformation/UH-DataTransformation/data_transformation"
#         )


# subprocess.run([python_version,'prerequisites.py'],cwd=wd,
#             check=True,)

if os.path.exists(os.path.join(wd,'dbt_packages')):
    dbt = DbtCliResource(project_dir=wd)
else:
    dbt = DbtCliResource(project_dir=wd)
    dbt.cli(['deps']).wait().target_path.joinpath("dbt_packages")

dbt_manifest_path = (
        dbt.cli(
            ["--quiet", "parse"],
            target_path=Path("target"),
        )
        .wait()
        .target_path.joinpath("manifest.json")
    )

if os.path.exists(os.path.join(wd,'target','manifest.json')):
    dbt_manifest_path = os.path.join(wd,"target", "manifest.json")
else:
    dbt_manifest_path = (
        dbt.cli(
            ["--quiet", "parse"],
            target_path=Path("target"),
        )
        .wait()
        .target_path.joinpath("manifest.json")
    )
# print()

# dbt_manifest_path = os.path.join(wd,"target", "manifest.json")