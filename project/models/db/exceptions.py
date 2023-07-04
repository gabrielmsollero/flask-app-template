class UnitNotFoundException(Exception):
    '''
    Raised when there's an attempt to create a DB object with
    a non-existent unit ID.
    '''
    
    def __init__(self, unit_id: str):
        self.code = 404
        self.description = f'Unit {unit_id} does not exist.'
        super().__init__(self.description)