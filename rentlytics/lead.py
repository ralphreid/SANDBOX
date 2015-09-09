class Lead:
    def __init__(self, id,
                 first_seen=None,
                 expected_move_in=None,
                 shown_unit=None,
                 agent_id=None,
                 marketing_source=None,
                 application_submitted=None,
                 application_approved=None,
                 application_denied=None,
                 application_canceled=None,
                 lease_signed=None,
                 resident_rent=None,
                 unit_name=None,):
        self.id = id
        self.first_seen = first_seen
        self.expected_move_in = expected_move_in
        self.shown_unit = shown_unit
        self.agent_id = agent_id
        self.marketing_source = marketing_source
        self.application_submitted = application_submitted
        self.application_approved = application_approved
        self.application_denied = application_denied
        self.application_canceled = application_canceled
        self.lease_signed = lease_signed
        self.resident_rent = resident_rent
        self.unit_name = unit_name



