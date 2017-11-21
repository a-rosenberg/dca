#!/usr/bin/env python
import logging


def generate_http_request(keywords, start=0, records=50, api_key='DONORSCHOOSE', **kwargs):
    """
    Generates the URL request to send to the HTTP endpoint. A lot of the complexity of the
    request handling will have to be incorporated into this function (or subfunctions of it).
    Right now it only takes keywords and searches the entire database. The start and records
    parameters are there to allow you to iterate through the JSON response. The API is set
    up with a buffer of 50 records max per request :/.

    EDITED:  I added a kwargs tool so that you can add additional arguments to the url.  
    There will need to be some control to make sure that the additional paramters are on the 
    API list of value arguments.
    """
    VALID_PARAMETERS = ['subject1', 'subject2', 'subject3', 'subject4', 'subject5', 'subject6', 
    					'subject7', 'partiallyFunded', 'highLevelPoverty', 'highestLevelPoverty',
    					'teacherNotFunded', 'proposalType', 'proposalTypeFunded', 'gradeType', 
    					'teacherType'] # add all valid params

    if records > 50:
        raise ValueError('Error: records must be <= 50 per API')
    http_keywords = '+'.join(keywords.split())
    base_url = 'https://api.donorschoose.org/common/json_feed.html?' \
               'APIKey={api_key}' \
               '&keywords="{keywords}"' \
               '&index={index}' \
               '&max={max}'
    url = base_url.format(keywords=http_keywords, index=start, max=records, api_key=api_key)
    for params in kwargs.iteritems():
    	if params[0] in VALID_PARAMETERS:
    		url += '&%s=%s' % params
    	else:
    		raise ValueError('Parameter (%s) not valid' % params[0])
    return url


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	print generate_http_request('Hawaii')
	print generate_http_request('Hawaii', subject6=-6, partiallyFunded='yes')
