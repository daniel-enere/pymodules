def report_status(scheduled_time, estimated_time):
    '''
    (number, number) -> str
    
    Return arrival status of plane based on difference
    between estimated_time and scheduled_time

    Precondition: 0.0 <= scheduled_time + estimated_time < 24
    
    >>> report_status(14.3,14.3)
    'on time'
    >>> report_status(12.5, 11.5)
    'early'
    >>> report_status(9, 9.5)
    'delayed'
    '''
    if estimated_time == scheduled_time:
        return 'On Time'

    if estimated_time <= scheduled_time:
        return 'Early'

    if estimated_time >= scheduled_time:
        return 'Delayed'
