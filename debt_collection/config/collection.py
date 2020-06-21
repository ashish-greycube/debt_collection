from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
        {
			"label": _("Doctype"),
			"items": [
				{
					"type": "doctype",
					"name": "Client Debt",
					"description": "Client Debt"
				}
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"name": "Debt Collection Detail",
					"is_query_report": True,
					"doctype": "Client Debt"
				}
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Client Debt Status",
					"description": "Client Debt Status"
				},
                {
					"type": "doctype",
					"name": "Debt Service Type",
					"description": "Debt Service Type"
				}

			]
		}
		]
	return config
	
