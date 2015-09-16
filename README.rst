PyCriteo
=========

PyCriteo is a simple Python library to access the Criteo API.
It uses Python convenient built in dictionaries to make API requests.

Basic usage:
-----------
Get all running campaigns

    >>> from pycriteo import Client
    >>> c = Client('username', 'password', 'token')
    >>> campaigns = c.getCampaigns({'campaignStatus': 'RUNNING'})
    >>> dict(campaigns.campaign[0]).keys()
    ['status',
     'campaignID',
     'categoryBids',
     'budgetID',
    'campaignName',
     'remainingDays',
     'campaignBid']
     
Schedule a report job

    >>> job = c.scheduleReportJob(
                {'reportType': 'Category',
                 'reportSelector': {
                        'CampaignIDs': [i.campaignID for i in campaigns.campaign]},
                'startDate': '2014-01-01',
                'endDate': '2014-30-01',
                'isResultGzipped': False,
                'aggregationType': 'Daily'
                }
            )

Save the report job as csv

    >>> c.downloadReport(job.jobID, 'my_report.csv')

Installation
--------------


    pip install pycriteo


License
----

Apache 2.0

