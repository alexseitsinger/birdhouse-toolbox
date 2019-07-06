import os
import json
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

from ..controller import BirdhouseToolbox


class Analytics(BirdhouseToolbox):
    """
    Get data from the analytics api.

    For API syntax, see:
    https://developers.google.com/analytics/devguides/reporting/core/v4/rest/v4/reports/batchGet
    """

    config_key = "analytics"
    scopes = ["https://www.googleapis.com/auth/analytics.readonly"]
    api_name = "analytics"
    api_version = "v4"
    credentials = None
    service = None

    def get_service(self):
        credentials = self.get_credentials()
        if self.service is None:
            self.service = build(
                self.api_name, self.api_version, credentials=credentials
            )
        return self.service

    def get_credentials(self):
        if self.credentials is None:
            self.credentials = Credentials.from_service_account_info(
                self.config["service_account"], scopes=self.scopes
            )
        return self.credentials

    def send_report_requests(self, report_requests):
        return (
            self.get_service()
            .reports()
            .batchGet(body={"reportRequests": report_requests})
            .execute()
        )

    def make_report_request(self, dates, metrics, dimensions=[]):
        return {
            "viewId": self.config["view_id"],
            "dateRanges": [{"startDate": x[0], "endDate": x[1]} for x in dates],
            "metrics": [{"expression": "ga:{}".format(x)} for x in metrics],
            "dimensions": [{"name": "ga:{}".format(x)} for x in dimensions],
        }

    def get_reports(self, dates):
        dates = [dates]
        audience_overview = self.make_audience_overview_report_request(dates)
        acquisitions_overview = self.make_acquisitions_overview_report_request(dates)
        acquisitions_search = self.make_acquisitions_search_console_queries_report_request(
            dates
        )
        behavior_overview = self.make_behavior_overview_report_request(dates)
        conversions_goals = self.make_conversions_goals_overview_report_request(dates)
        response = self.send_report_requests(
            [
                audience_overview,
                acquisitions_overview,
                acquisitions_search,
                behavior_overview,
                conversions_goals,
            ]
        )
        return {
            "audience": {"overview": response["reports"][0]},
            "acquisitions": {
                "overview": response["reports"][1],
                "search": {"queries": response["reports"][2]},
            },
            "behavior": {"overview": response["reports"][3]},
            "conversions": {"goals": {"overview": response["reports"][4]}},
        }

    def make_audience_overview_report_request(self, dates):
        metrics = [
            "users",
            "newUsers",
            "pageviewsPerSession",
            "avgSessionDuration",
            "bounceRate",
        ]
        return self.make_report_request(dates, metrics)

    def make_acquisitions_overview_report_request(self, dates):
        metrics = ["users"]
        dimensions = ["channelGrouping"]
        return self.make_report_request(dates, metrics, dimensions)

    def make_acquisitions_search_console_queries_report_request(self, dates):
        metrics = ["organicSearches"]
        dimensions = ["keyword"]
        return self.make_report_request(dates, metrics, dimensions)

    def make_behavior_overview_report_request(self, dates):
        metrics = ["uniquePageviews"]
        dimensions = ["pagePath"]
        return self.make_report_request(dates, metrics, dimensions)

    def make_conversions_goals_overview_report_request(self, dates):
        metrics = ["goalCompletionsAll"]
        dimensions = ["goalCompletionLocation"]
        return self.make_report_request(dates, metrics, dimensions)
