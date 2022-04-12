

class CatApiVote:

    def __init__(self, initialize_dict):
        self.id = initialize_dict.get("id")
        self.image_id = initialize_dict.get("image_id")
        self.sub_id = initialize_dict.get("sub_id")
        self.created_at = initialize_dict.get("created_at")
        self.value = initialize_dict.get("value")
        self.country_code = initialize_dict.get("country_code")

    def __eq__(self, other):
        if self.id != other.id:
            return False
        if self.image_id != other.image_id:
            return False
        if self.sub_id != other.sub_id:
            return False
        if self.created_at != other.created_at:
            return False
        if self.value != other.value:
            return False
        if self.country_code != other.country_code:
            return False
        return True
