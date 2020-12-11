# Google Public Cloud
import wcommon as wc
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GCP():
	def __init__(self, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, SCOPES, PICKLE_TOKEN_FILE):
		self.SAMPLE_SPREADSHEET_ID = SAMPLE_SPREADSHEET_ID
		self.SAMPLE_RANGE_NAME = SAMPLE_RANGE_NAME
		self.SCOPES = SCOPES
		self.PICKLE_TOKEN_FILE = PICKLE_TOKEN_FILE
		self.__name__ = 'GCP'

	def Connect(self):
		connect = wc.timer_index_start()
		creds = None
		if os.path.exists(self.PICKLE_TOKEN_FILE):
			with open(self.PICKLE_TOKEN_FILE, 'rb') as token:
				creds = pickle.load(token)
		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
				creds = flow.run_local_server(port=0)
			# Save the credentials for the next run
			with open(self.PICKLE_TOKEN_FILE, 'wb') as token:
				pickle.dump(creds, token)

		service = build('sheets', 'v4', credentials=creds)
		wc.pairprint('GCP:  Connect', str(wc.timer_index_since(connect)) + ' ms')
		# Call the Sheets API
		return(service.spreadsheets().values())

	def GET(self,handle):
		getTime = wc.timer_index_start()
		out = []
		result = handle.get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range=self.SAMPLE_RANGE_NAME).execute()
		wc.pairprint('GCP:  GET', str(wc.timer_index_since(getTime)) + ' ms')
		return(result.get('values',[]))

	def SET(self,handle,cell,value):
		setTime = wc.timer_index_start()
		body = {'values':[[value]]}
		rangeName = self.SAMPLE_RANGE_NAME + '!' + cell
		try:
			result = handle.update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
				range=rangeName, valueInputOption='RAW', body=body).execute()
			wc.pairprint(cell,value)
		except Exception as err:
			print('\n\n' + str(err))
		wc.pairprint('GCP:  SET', str(wc.timer_index_since(setTime)) + ' ms')
		return()

	def CONVERT_JSON_BY_HEADER(self,sheet,headIndex):
		self.headers = sheet.pop(0)
		ipIndex = self.headers.index(headIndex)
		asset = {}
		r = 2; # 2=because there's no 0 and 1 is headers.pop(0)
		for row in sheet:
			# wc.pairprint(row,ipIndex)
			if len(row)-1 < ipIndex:
				continue
			ip = row[ipIndex]
			asset[ip] = {'Row':r}
			i = 0
			for colum in row:
				# wc.pairprint('\t' + self.headers[i],colum)
				asset[ip][self.headers[i]] = colum
				i += 1
			r += 1
		return(asset)


