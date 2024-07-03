
from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .dbt_models import dbt_manifest_path, wd


@dbt_assets(manifest=dbt_manifest_path)
def dbt_transformation_models(context: AssetExecutionContext):
    dbt = DbtCliResource(project_dir=wd)
    yield from dbt.cli(["build"], context=context).stream()