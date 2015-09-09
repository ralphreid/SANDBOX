class Source:
    def __init__(self, name,
                 monthly=0,
                 per_lease=0,
                 percentage_per_lease=0,
                 per_lead=0,
                 free=False,):
        self.name = name
        self.monthly = monthly
        self.per_lease = per_lease
        self.percentage_per_lease = percentage_per_lease
        self.per_lead = per_lead
        self.free = free

