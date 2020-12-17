def check_if_feature_value_match(expected_feature_values: dict, list_of_data: list):
    matching_rows = []
    for data_row in list_of_data:
        if all(data_row.get(
                exp_feature_name) == exp_feature_value for exp_feature_name, exp_feature_value in
               expected_feature_values.items()):
            matching_rows.append(data_row)
    return matching_rows
