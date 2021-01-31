# 초대장
class Invitation:
    def __init__(self):
        self.date = None


# 티켓
class Ticket:
    def __init__(self):
        self.fee = 0
    
    def get_fee(self):
        return self.fee


# 가방
class Bag:
    def __init__(self, amount=0, invitation=None, ticket=None):
        self.amount = amount
        self.invitation = invitation
        self.ticket = ticket
    
    def has_invitation(self):
        return self.invitation != None
    
    def set_ticket(self, ticket):
        self.ticket = ticket
    
    def minus_amount(self, amount):
        self.amount = self.amount - amount
    
    def plus_amount(self, amount):
        self.amount = self.amount + amount


# 관람객
class Audience:
    def __init__(self, bag):
        self.bag = bag
    
    def buy(self, ticket):
        if self.bag.has_invitation():
            self.bag.set_ticket(ticket)
            return 0
        else:
            self.bag.set_ticket(ticket)
            self.bag.minus_amount(ticket.get_fee())
            return ticket.get_fee()

# 매표소
class TicketOffice:
    def __init__(self, amount, tickets):
        self.amount = amount
        self.tickets = tickets

    def get_ticket(self):
        return self.tickets.pop(0)

    def minus_amount(self, amount):
        self.amount = self.amount - amount
    
    def plus_amount(self, amount):
        self.amount = self.amount + amount


# 티켓 판매원
class TicketSeller:
    def __init__(self, ticket_office):
        self.ticket_office = ticket_office
    
    def sell_to(self, audience):
        self.ticket_office.plus_amount(audience.buy(self.ticket_office.get_ticket()))
            


# 소극장
class Theater:
    def __init__(self, ticket_seller):
        self.ticket_seller = ticket_seller
    
    def enter(self, audience):
        self.ticket_seller.sell_to(audience)