class Ticket:
    number = None
    creator = ""
    staff_id = ""
    email = ""
    description = ""
    response = "Not Yet Provided"
    status = "Open"

    def resolve(self):
        response = input("Please provide a response: ")
        self.response = response
        self.status = "Closed"
        return self

    def reopen(self):
        self.status = "Reopened"
        self.response = "Not Yet Provided"
        return self
