import scrapy
import pandas as pd

class ApiScraper(scrapy.Spider):
	name = "apiscraper"
	
	def dfopp(r):
		return r[0:]
		
	# Replace with your actual JSON file of API links
	def start_requests(self):
		# Load your JSON list of API links
		df = pd.read_csv('api_links.json')
		df = df.drop_duplicates(subset=['link'])
		
		for i,r in df.iterrows():
			link = r['link']
			try:
				yield scrapy.Request(url=link, callback=self.parse)
			except:
				continue
		
	def parse(self, response):
		# Extract the response data you need
		data = response.json()
		ans = {}
		try:
			ans['name'] = data['college_name']
		except:
			ans['name'] = pd.NA
		try:
			ans['institute type'] = data['page_type']
		except:
			ans['institute type'] = pd.NA
		try:
			ans['basic_info'] = data['basic_info']
		except:
			ans['basic_info'] = pd.NA
		try:
			ans['facilities'] = data['college_facilities']['facility']
		except:
			ans['facilities'] = pd.NA
		try:
			ans['faculty'] = data['faculty']
		except:
			ans['faculty'] = pd.NA
		try:
			ans['course'] = data['course_data']['courses']
		except:
			ans['course'] = pd.NA
		# Save or process the data as per your requirements
		# Example: Print the response
		#self.log(f"Data from {response.url}: {data}")
		
		df = pd.read_csv('main.csv', index_col=False)
		df2 = pd.DataFrame([ans])
		#df2.to_csv('main.csv')
		df = pd.concat([df,df2])
		df.to_csv('main.csv',index=False)
		yield ans

