'''Test fault resilence of API connection code '''

from connections.connect import connect


def test_connect():
    ''' Test that the connection method successfully connects to the
    Company house API using an environemtn variable
    '''
    timepoint = None
    response = connect(timepoint)
    assert response.status_code == 200
