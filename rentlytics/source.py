class Source:
    def __init__(self, name,
                 monthly=None,
                 per_signed_lease=None,
                 percentage_per_lease=None,
                 per_lead=None,
                 free=False,):
        self.name = name
        if monthly is None:
            monthly = ""
        self.monthly = monthly
