import json
import pkgutil



def get_json(json_path):
	try:
		data = pkgutil.get_data(__name__, json_path)
		return json.loads(data.decode("utf-8"))
	except Exception as e:
		print(e)
		return None


