from typing import List, Dict, Callable, Any


def aggregate_data(
    data: List[Dict[str, Any]], key: str, aggregator: Callable
) -> Dict[str, Any]:
    aggregated_result = {}

    for item in data:
        key_value = item.get(key)

        if key_value is not None:
            if key_value not in aggregated_result:
                aggregated_result[key_value] = []

            aggregated_result[key_value].append(item)

    final_result = {k: aggregator(v) for k, v in aggregated_result.items()}

    return final_result


data = [
    {"category": "A", "value": 10},
    {"category": "B", "value": 20},
    {"category": "A", "value": 30},
    {"category": "B", "value": 40},
]


def sum_values(group: List[Dict[str, Any]]) -> int:
    return sum(item["value"] for item in group)


# Aggregate the data by 'category' and sum the 'value'
result = aggregate_data(data, "category", sum_values)

print(result)  # Output: {'A': 40, 'B': 60}
