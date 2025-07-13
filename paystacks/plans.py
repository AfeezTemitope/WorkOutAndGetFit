from paystacks import utils
from paystacks.baseapi import BaseAPI


class Plan(BaseAPI):

    def create(self, name, amount, interval, description=None,
               send_invoices=False, send_sms=False, hosted_page=False, hosted_page_url=None, hosted_page_summary=None, currency=None):
        """
        Creates a new plan. Returns the plan details created

        args:
        name -- Name of the plan to create
        amount -- Amount to attach to this plan
        interval -- 'hourly', 'daily', 'weekly', 'monthly', 'annually'
        description -- Plan Description (optional)

        """
        interval = utils.validate_interval(interval)
        amount = utils.validate_amount(amount)