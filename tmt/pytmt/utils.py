import json
import os



def get_json(json_path):
	if os.path.isfile(json_path):
		with open(json_path) as f:
			jo = json.load(f)
		return jo
	else:
		return None


