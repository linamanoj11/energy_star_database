

def check_if_feature_value_match(expected_feature_values: dict, list_of_data:list):
    matching_rows=[]
    for data_row in list_of_data:
        for exp_feature_name, exp_feature_value in expected_feature_values.items():
            if data_row.get(exp_feature_name) == exp_feature_value:
                matching_rows.append(data_row)
    return matching_rows