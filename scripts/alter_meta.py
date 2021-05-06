def alter_meta(meta):
    if 'NSDPIndicatorID' in meta:
        # Auto-calculate settings based on 'NSDPIndicatorID'.
        open_sdg_id = meta['NSDPIndicatorID'].replace(' ', '').replace('.', '-')
        meta['indicator_number'] = open_sdg_id
        meta['goal_number'] = open_sdg_id.split('-')[0]
        meta['goal_name'] = 'global_goals.' + meta['goal_number'] + '-title'
        meta['target_number'] = open_sdg_id.split('-')[0] + '-' + open_sdg_id.split('-')[1]
        meta['target_name'] = 'global_targets.' + meta['target_number'] + '-title'
        meta['indicator_name'] = 'indicators.' + open_sdg_id + '-title'
        meta['national_geographical_coverage'] = 'Vanuatu'
    return meta
