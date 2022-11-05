from ticket import Ticket


class Main:
    """ Ticket number initial count """
    ticket_number = 2000

    """ All tickets list """
    tickets = []

    """ 
    Ticket statuses count
    
    Open: All tickets count with status 'Open'
    Closed: All tickets count with status 'Closed'
    Total: All tickets count
    """
    stats = {
        "open": 0,
        "closed": 0,
        "total": 0,
    }

    """ Menus """
    menus = {
        "s": """Help Desk Ticketing System - Staff
    1. Create Ticket
    2. Ticket Status """,
        "i": """Help Desk Ticketing System - IT Team
    1. Stats
    2. Resolve
    3. Reopen
    4. List All"""
    }

    """ Choices dictionary to match option with an specific function for staff and IT Team"""
    choices = {}

    def __init__(self):
        self.choices = {
            "i": {
                "1": self.show_stats,
                "2": self.ticket_resolve,
                "3": self.ticket_reopen,
                "4": self.list_all
            },
            "s": {
                "1": self.create_ticket,
                "2": self.ticket_status
            }
        }

    def calc_stats(self):
        """ Re-Calculate Stats """
        open_tickets = 0
        closed_tickets = 0
        total_ticket = 0

        for ticket in self.tickets:
            total_ticket += 1
            if ticket.status == "Open" or ticket.status == "Reopened":
                open_tickets += 1
            elif ticket.status == "Closed":
                closed_tickets += 1

        self.stats.update({
            "open": open_tickets,
            "closed": closed_tickets,
            "total": total_ticket
        })

    def show_stats(self):
        print("")
        print("Ticket Statistics.")
        print("----------------")
        print("""
        Tickets Created: {}
        Tickets Resolved: {}
        Tickets To Solve: {}
        """.format(self.stats["total"], self.stats["closed"], self.stats["open"]))
        print("----------------")

    def find_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket.number == int(ticket_number):
                return ticket
            else:
                return None

    def ticket_resolve(self):
        ticket_number = input("Ticket Number? ")
        ticket = self.find_ticket(ticket_number)
        if ticket:
            ticket.resolve()
            self.calc_stats()
        else:
            print("Ticket not found")

    def ticket_reopen(self):
        ticket_number = input("Ticket Number? ")
        ticket = self.find_ticket(ticket_number)
        if ticket:
            ticket.reopen()
            self.calc_stats()
        else:
            print("Ticket not found")

    def list_all(self):
        for ticket in self.tickets:
            self.print_ticket(ticket)

    def ticket_status(self):
        ticket_number = input("Ticket Number? ")
        ticket = self.find_ticket(ticket_number)
        if ticket:
            if ticket.status == "Closed":
                print(f"\nTicket number {ticket.number} status is '{ticket.status}. Response: {ticket.response}'\n")
            else:
                print(f"\nTicket number {ticket.number} status is '{ticket.status}'\n")

    def create_ticket(self):
        t = Ticket()

        # Increment ticket number by 1
        self.ticket_number += 1

        # Assign already incremented number (First will be 2001)
        t.number = self.ticket_number

        name = input("Name? ")
        t.creator = name

        staff_id = input("Staff ID? ")
        t.staff_id = staff_id.upper()

        email = input("Email? ")
        t.email = email

        description = input("Description? ")
        t.description = description

        # If 'change password' is in the ticket description
        # generate a new password, close the ticket and update the response
        # and include the new password (just debug propose)
        if 'change password' in description.lower():
            password = staff_id[:2]+name[:3]
            t.status = "Closed"
            t.response = "Password changed successfully '{}'".format(password)
            self.calc_stats()

        # Add the created ticket to App tickets list
        self.tickets.append(t)

        # Re-Calculate stats
        self.calc_stats()

        print("")
        print("Your ticket was successfully created.")
        self.print_ticket(t)

    def print_ticket(self, ticket):
        print("\n----------------")
        print("""
Ticket Number: {}
Ticket Creator: {}
Staff ID: {}
Email Address: {}
Description: {}
Response: {}
Ticket Status: {}\n""".format(
            ticket.number,
            ticket.creator,
            ticket.staff_id,
            ticket.email,
            ticket.description,
            ticket.response,
            ticket.status
        ))

    def run(self):
        # ask for role (staff or help desk)
        print("-----------------------------------------")
        print("| Welcome to Help Desk Ticketing System |")
        print("-----------------------------------------")
        staff_or_it = input("Use as (s) Staff, (i) IT Team or (e) Exit: ")
        if staff_or_it == "e":
            exit(0)

        print(self.menus.get(staff_or_it))

        actions = self.choices.get(staff_or_it)
        choice = input("Enter an option: ")
        action = actions.get(choice)

        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))

        self.run()


app = Main()
app.run()
