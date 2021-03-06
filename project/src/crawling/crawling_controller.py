from crawling_common import *
from crawling_stack import *
from crawling_google import *

def search(query, type = ''):
	'''
	@query : 키워드
	@type : 코드의 종류, CODE_TYPE 참조
	'''
	stack = CandidatesStack(query, type)
	google = CandidatesGoogle(query, type)

	results = stack + google

	return [i.content for i in results.codes]