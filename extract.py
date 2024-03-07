import requests
import pandas as pd
from collections.abc import Iterator
from requests.exceptions import ConnectionError
from logzero import logger


class Extract:
	"""
	Extract data from API
	"""
	def __init__(self, url: str):
		self.url = url

	def get_resquest(self, page: str) -> dict:
		url_page = self.url + page
		try:
			response = requests.get(url_page).json()
		except ConnectionError:
			logger.error(f"URL {url_page} is wrong")
		return response

	def fetch_record(self) -> Iterator[dict]:
		page = f"line/"
		response = self.get_resquest(page)
		line_id = [i for i in response.keys()]

		for i, id in enumerate(line_id):
			page = f"line/{id}"
			response = self.get_resquest(page)
			print(response)
			yield response

	def create_dataframe(self) -> pd.DataFrame:
		df = pd.DataFrame()
		for record in self.fetch_record():
			for id, r in record.items():
				for key, val in r["Actuals"].items():
					val.update({"ActualID": key, "LineID": id})
					df = pd.concat([df, pd.DataFrame(val, index=[0])])

		return df
