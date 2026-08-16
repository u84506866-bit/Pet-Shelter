import re

class Adopter:
    
    def __init__(self, name, phone, national_id, adopted_animals):
        self.name = name
        self.phone = phone
        self.national_id = national_id
        self.adopted_animals = adopted_animals

    def validate_format(self):
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
