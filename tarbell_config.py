# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "hooks31"

# Descriptive title of project
TITLE = "asdlkj"

# Google spreadsheet key
#SPREADSHEET_KEY = "None"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "apps.chicagotribune.com/hooks31",
    "staging": "apps.beta.tribapps.com/hooks31",
}

# Default template variables
DEFAULT_CONTEXT = {
    'data': [   {   'column1': u'row1, column1',
                    'column2': u'row1, column2'},
                {   'column1': u'row2, column1',
                    'column2': u'row2, column2'}],
    'headline': u'Test headline',
    'keyed_data': {   'key1': {   'column1': u'key1, column1',
                                  'column2': u'key1, column2',
                                  'key': u'key1'},
                      'key2': {   'column1': u'key2, column1',
                                  'column2': u'key2, column2',
                                  'key': u'key2'}},
    'name': 'hooks31',
    'title': 'asdlkj'
}