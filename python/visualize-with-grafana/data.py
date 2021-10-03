import math

from datetime import datetime
from calendar import timegm

FUNCTIONS = {'series A': math.sin, 'series B': math.cos}

def convert_to_time_ms(timestamp):
    """Convert a Grafana timestamp to unixtimestamp in milliseconds

        Args:
            timestamp (str): the request contains ``'range': {'from':
                '2019-06-16T08:00:05.331Z', 'to': '2019-06-16T14:00:05.332Z', ...``
        """
    return 1000 * timegm(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())

def create_data_points(func, start, end, length=1020):
    """
        A dummy function to produce sine and cosine data

        You should replace this with your SQL, CQL or Mongo Query language.
        Also, make sure your database has the correct indecies to increase perfomance

        Args:
          func (object) - A callable that accepts a number and returns a number
            start (str) - timestamp
            end (str) - timestamp
            length (int) - the number of data points

        """
    lower = convert_to_time_ms(start)
    upper = convert_to_time_ms(end)
    return [[func(i), int(i)] for i in [lower + x*(upper-lower)/length for x in range(length)]]
