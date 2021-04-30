import yaml
import os
"""
PillarName: Economy
NSDPIndicatorID: ECO 1.1.1
IndicatorShortName: Underlying Inflation Rate
Definition: Total rate of change of CPI from previouse year
Calculation/Formulation:
Range:
Assumptions:
Limitations:
IntendedDirection:
Purpose/Rationale:
PolicyLinkage:
PreferredDataSource:
AlternativeDataSource:
SourceTag: "Table 1 CPI December Quarter"
PrimaryCollectionSystem:
FrequencyofCollection:
OtherDemandSources:
ResponsibleAgency:
RelatedLinks:
graph_type: bar
computation_units:
source_active_1: true
source_organisation_1: "December Quarter Statistical Update 2017 : CPI, VNSO"
source_active_2: true
source_organisation_2: "December Quarter Statistical Update 2013 : CPI, VNSO"
source_active_3: true
source_organisation_3: "December Quarter Statistical Update 2015 : CPI, VNSO"
source_active_4: true
source_organisation_4: "December Quarter Statistical Update 2016 : CPI, VNSO"
source_active_5: true
source_organisation_5: "December Quarter Statistical Update 2014 : CPI, VNSO"
source_active_6: true
source_organisation_6: "December Quarter Statistical Update 2018 : CPI, VNSO"
data_non_statistical: false
graph_title: Change in underlying inflation rate (CPI analysis)
"""
config_keys = [
    'graph_title',
    'data_non_statistical',
    'graph_type',
    'computation_units',
    'reporting_status',
]


for meta_file in os.listdir('meta'):
    meta_path = os.path.join('meta', meta_file)
    config_path = os.path.join('indicators', meta_file)
    with open(meta_path, 'r') as stream:
        meta = yaml.load(stream, Loader=yaml.FullLoader)
    new_config = {}
    new_meta = {}
    for key in meta:
        if key in config_keys:
            new_config[key] = meta[key]
        else:
            new_meta[key] = meta[key]
    with open(meta_path, 'w') as stream:
        yaml.dump(new_meta, stream)

    old_config = {}
    if os.path.isfile(config_path):
        with open(config_path, 'r') as stream:
            old_config = yaml.load(stream, Loader=yaml.FullLoader)
    for key in old_config:
        new_config[key] = old_config[key]

    with open(config_path, 'w') as stream:
        yaml.dump(new_config, stream)
