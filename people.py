# Using the re library we will use regex methods
import re

# In class Adopter there is every information about the 
# person that is adopting the pet
# and here also there is a method that will validate the 
# person's Phone and national id 
class Adopter:
    # each person has a name a phone number and national id
    # and most importantly how many pets do they have
    def __init__(self, name, phone, national_id, adopted_animals):
        self.name = str(name)
        self.phone = str(phone)
        self.national_id = str(national_id)
        self.adopted_animals = int(adopted_animals)

    # Here we will use regex to determine wheter or not they 
    # are giving correct information before they can adopt 
    # a pet
    def validate_format(self):
        # This part uses regex and find valid numbers that 
        # starts with 0 and 98 and +98 at the start and 
        # after wards it take 9 other digits
        phone_pattern = r'^(?:0|98|\+98)?9\d{9}$'
        phone_valid = bool(re.fullmatch(phone_pattern, str(self.phone).strip()))

        national_id = str(self.national_id).strip()


        if not re.fullmatch(r'^\d{10}$', national_id):
            return False

        if len(set(national_id)) == 1:
            return False

        # Checksum algorithm
        check = int(national_id[9])
        s = sum(int(national_id[i]) * (10 - i) for i in range(9))
        r = s % 11

        if r < 2:
            national_id_valid = (check == r)
        else:
            national_id_valid = (check == 11 - r)

        return phone_valid and national_id_valid
