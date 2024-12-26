import json
auto = {
    'car': 'Kia',
    'stamp': 'Seltos',
    'state_number': 42442
}
result = json.dumps(auto)
print(result)
print(type(result))