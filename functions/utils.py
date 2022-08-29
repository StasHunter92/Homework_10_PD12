import json


def load_json(file: str) -> list[dict]:
	"""Return list with dicts of candidates from JSON file"""
	with open(file, 'r', encoding='utf-8') as f:
		data = json.load(f)
		return data


def get_by_pk(pk: int, data: list[dict]) -> dict | None:
	"""Return candidate by pk"""
	for candidate in data:
		if pk == candidate['pk']:
			return candidate
		else:
			return None


def get_by_skill(skill_name: str, data: list[dict]) -> list[dict] | list:
	"""Return candidates by skill name"""
	candidates_list = []
	for candidate in data:
		if skill_name.lower() in candidate['skills'].lower().split(', '):
			candidate_dict = {
				'name': candidate['name'],
				'position': candidate['position'],
				'skills': candidate['skills'],
			}
			candidates_list.append(candidate_dict)
	return candidates_list
