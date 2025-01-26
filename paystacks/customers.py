from paystacks.baseapi import BaseAPI


class Customer(BaseAPI):
    def create(self, email, first_name=None, last_name=None, phone=None):
        """
        Create a new paystack customer account.

        args:
        email -- Customer's email address
        first_name-- Customer's first name (Optional)
        last_name-- Customer's last name (Optional)
        phone -- optional
        """

        url = self._url('customers')
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
        }

        return self._handle_request("POST", url, json=payload)

