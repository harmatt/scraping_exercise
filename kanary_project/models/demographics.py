from pydantic import BaseModel, validator


class Name(BaseModel):
    name: str

    @validator('name')
    def name_must_be_at_least_one_character(cls, v):
        if len(v) == 0:
            raise ValueError('Name must be at least 1 character.')
        return v


class Location(BaseModel):
    state: str

    @validator('state')
    def name_must_be_at_least_one_character(cls, v):
        states = ["All States", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                  "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                  "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                  "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
                  "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
                  "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                  "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        if v not in states:
            raise ValueError('State must be \"All States\", \"District of Columbia\" or a valid US state with proper '
                             'spacing and capitalization.')
        return v


class Person(BaseModel):
    first_name: Name
    last_name: Name
    location: Location
