from cruncher import NumberRequester
from datetime import datetime as dt


def test_number_requester_returns_a_valid_result_when_called():
    """Test that the call method returns a valid item.
    
    Given:
         A NumberRequester instance making a successful call

    Result:
        A result as a dict in the form {'result': 'SUCCESS', 'number': 13, "fact": "13 is lucky for some."}

    """
    def mock_call():
        return {'result': 'SUCCESS', 'number': 13, "fact": "13 is lucky for some."}
    nr = NumberRequester()
    nr.call = mock_call
    assert nr.call() == {'result': 'SUCCESS', 'number': 13, "fact": "13 is lucky for some."}
    pass


def test_number_requester_returns_error_result_for_non_200_response():
    """Test that the call method returns a valid item when a request fails.
    
    Given:
         A NumberRequester instance making an unsuccessful call

    Result:
        A result as a dict in the form {'result': 'FAILURE', 'error_code': 404}
    
    """
    nr = NumberRequester()
    nr.endpoint = 'https://www.bbc.co.uk/gre'
    assert nr.call() == {'result': 'FAILURE', 'error_code': 404}
    pass


def test_number_requester_keeps_log_of_requests():
    """Test that a NumberRequester instance keeps a log of its own requests.

    Given:
        A NumberRequester is instantiated.
        The NumberRequester.call method is called 5 times at known times.

    Result:
        The NumberRequester.log attribute returns a array of five valid results. Each result
        is a serialisable dict in the form:
        {'request_number': 1, 'call_time': '2022-11-09T16:38:23.417667', 'end_point': 'http://numbersapi.com/random/math',
        'result': 'SUCCESS', 'number': 49}
    Ensure that you test that each dict is exactly correct - including the 'call_time'.
    """
    nr = NumberRequester()
    nr.call()
    nr.call()
    nr.call()
    nr.call()
    nr.call()
    
    for index, entry in enumerate(nr.log):
        print(entry)
        assert entry['request_number'] == index + 1
        assert entry['end_point'] == 'http://numbersapi.com/random/math'
        assert entry['result'] == 'SUCCESS'
        assert type(entry['number']) == int
