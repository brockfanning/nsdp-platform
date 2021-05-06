from sdg.open_sdg import open_sdg_build
from alter_meta import alter_meta
from alter_data import alter_data

open_sdg_build(config='config_data.yml', alter_meta=alter_meta, alter_data=alter_data)
