from . import exceptions, utils

class Model(object):
    '''
    Sample model.
    
    :param query (dict): User defined values for specific keys. Supports
    mongo filters like $lt, $lte, $gt, $gte;
    
    :param limit (int): Will limit the number of documents in the query
    result to <limit>, starting from the most recent one.
    
    :param start (float): Serves as the minimum unix timestamp of documents
    to be included in the query result.
    
    :param stop (float): Serves as the minimum unix timestamp of documents
    to be included in the query result.
    
    :param fields (dict): Specifies all fields that should be extracted OR
    all fields that should be ignored from each document. e.g.:
        
        fields = { 'foo': 1, 'bar': 1 } -> will get only 'foo' and 'bar'
                                           fields of each document;
                                           
        fields = { 'foo': 0, 'bar': 0 } -> will get all fields except 'foo'
                                           and 'bar' of each document;
    
    :param granularity (int): Valid only for numeric fields. If the number
    of documents in the query result is greater than this parameter, then the
    numeric fields will be averaged so that the final result has <granularity>
    elements. Non-numeric fields will hold the value of the first element in
    each averaged group.
    '''
    
    VALID_PARAMS = {
        'query': [dict],
        'limit': [int],
        'start': [float, int],
        'stop': [float, int],
        'fields': [dict],
        'granularity': [int]
    }
    
    def __init__(self, **kwargs):
        self._params = {}
        self._mongo_query = []
        
        for key, value in kwargs.items():
            self.set_param(key, value)
    
    def __repr__(self) -> str:
        return f'<class db.Model>\n{dict(self._params)}'
    
    def get_param(self, key):
        if key not in Model.VALID_PARAMS.keys():
            raise NameError
        
        return self._params.get(key)
    
    def set_param(self, key, value):
        if key not in Model.VALID_PARAMS.keys():
            raise NameError
        
        if not value:
            return
        
        if type(value) not in Model.VALID_PARAMS[key]:
            raise TypeError(f'Parameter <{key}> must be of one of types {Model.VALID_PARAMS[key]}, not {type(value)}.')
        
        if key == 'fields':
            if any([v not in [0, 1] for v in value.values()]):
                raise NameError
        
        self._params[key] = value
        
    def mongo_query(self) -> dict:
        general = {}
        fields = {}
        query = ()
        
        limit = self._params.get('limit')
        
        general['$orderby'] = {'$natural' : -1}
        general['$query'] = self._params.get('query') or {}
        
        # Timestamp restrictions defined by user in query will override
        # parameters start and stop.
        
        if not 'timestamp' in general['$query'].keys():
            if 'start' in self._params:
                general['$query'].setdefault('timestamp', {})
                general['$query']['timestamp']['$gte'] = self._params['start']
                
            if 'stop' in self._params:
                general['$query'].setdefault('timestamp', {})
                general['$query']['timestamp']['$lt'] = self._params['stop']
        
        fields = self._params.get('fields')
        granularity = self._params.get('granularity')
        
        if fields:
            query = (general, fields)
            
        else:
            query = (general,)
            
        self._mongo_query = {
            'query': query,
            'limit': limit,
            'granularity': granularity
        }
        
        return self._mongo_query