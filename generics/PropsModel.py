import json


class PropsModel:

    def __init__(self, ip, username, password, *args, **kwargs):
        self.ip = ip
        self.username = username
        self.password = password

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __str__(self):
        return "ip : %s, username : %s with password : %s" % (self.ip, self.username, self.password)