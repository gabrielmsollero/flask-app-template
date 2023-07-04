import pytest

from project.models import db

def test_validate_reefdbquery_nominal(new_model: db.Model, timestamp: float):
    """
    GIVEN a helper class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    assert new_model.get_param('query') == {'a': 1, 'b': {'$gte': 2}}
    assert new_model.get_param('limit') == 5
    assert new_model.get_param('stop') == timestamp
    assert new_model.get_param('start') == timestamp - 60*60*24
    assert new_model.get_param('fields') == {'_id': 0}
    
    new_model.set_param('limit', 10)
    assert new_model.get_param('limit') == 10
    
    assert new_model.mongo_query() == {
        'query': (
            {
                '$orderby': {'$natural': -1},
                '$query': {'a': 1, 'b': {'$gte': 2},
                           'timestamp': {'$gte': timestamp - 60*60*24, '$lt': timestamp}}
            },
            {'_id': 0}),
        'limit': 10,
        'granularity': None
    }
    
    
def test_validate_reefdbquery_invalid_field(new_model: db.Model):
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data is passed in (unexpected field)
    THEN check that the validation raises NameError
    """
    with pytest.raises(NameError):
        new_model.set_param('invalid_param', 1)
        
def test_validate_reefdbquery_invalid_type(new_model: db.Model):
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data is passed in (expected field with value of unexpected type)
    THEN check that the validation raises TypeError
    """
    with pytest.raises(TypeError):
        new_model.set_param('limit', 'a')
        
    assert new_model.get_param('limit') == 10
    
def test_validate_reefdbquery_bad_fields(new_model: db.Model):
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data is passed in (bad conditioned fields param)
    THEN check that the validation raises NameError
    """
    with pytest.raises(NameError):
        new_model.set_param('fields', {'a': 2})
        
    assert new_model.get_param('fields') == {'_id': 0}
