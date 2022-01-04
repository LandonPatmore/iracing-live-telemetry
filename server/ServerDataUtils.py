import math

"""
Filters out the pace car from the list of competitors.
"""


# TODO: Remove this at some point and do it client side to save data over the wire
def filter_pace_car(competitor_info):
    return list(filter(lambda competitor: competitor['userId'] != -1, competitor_info))


"""
Scrubs general info and converts pit speed limit to kph to be standardized when
sending to db.
"""


def general_info_scrub(general_info):
    general_info['pitSpeedLimit'] = math.ceil(float(general_info['pitSpeedLimit'].split()[0]))
    if general_info['displayUnits'] == 1:
        return general_info
    else:
        # convert to kph
        mph = math.ceil(general_info['pitSpeedLimit'] * 1.609)
        print(mph)
        general_info['pitSpeedLimit'] = mph
        return general_info
