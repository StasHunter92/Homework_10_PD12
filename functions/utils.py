import json


def load_candidates(file: str) -> list[dict]:
	"""Return list with dicts of candidates from JSON file"""
	with open(file, encoding='utf-8') as f:
		data = json.load(f)
		return data


def get_all(data: list[dict]) -> list:
	"""Return list with candidate names"""
	candidate_list = [candidate['name'] for candidate in data]
	return candidate_list


def get_by_pk(pk: int, data: list[dict]) -> dict:
	"""Return candidate by pk"""
	for candidate in data:
		if pk == candidate['pk']:
			return candidate


def get_by_skill(skill_name: str, data: list[dict]) -> list[dict]:
	"""Return candidates by skill name"""
	candidate_list = []
	for candidate in data:
		if skill_name.lower() in candidate['skills'].lower().split(', '):
			candidate_dict = {
				'name': candidate['name'],
				'position': candidate['position'],
				'skills': candidate['skills'],
			}
			candidate_list.append(candidate_dict)
	return candidate_list
