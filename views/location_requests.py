LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]


def get_all_locations():
    '''Function that returns all locations'''
    return LOCATIONS


def get_single_location(id: str):
    '''Function that returns a single location, based on the provided id string'''
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location


def create_location(location):
    '''Function that creates a new location'''
    # crete new id by incrementing the last id in LOCATIONS
    new_id = LOCATIONS[-1]['id'] + 1
    # add the new id to the location given in the parameters
    location['id'] = new_id
    # append the new location to the end of the LOCATIONS list
    LOCATIONS.append(location)
    # return the new location
    return location
