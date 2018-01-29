class GitObj:
    unix_permission = 000000
    type = "none"
    sha1_hash = "0000000000000000000000000000000000000000"
    filename = "no_name_nick"

    def __init__(self, unix_permission, type, sha1_hash, filename):
        self.unix_permission = unix_permission
        self.type = type
        self.sha1_hash = sha1_hash
        self.filename = filename
        self.child_objects = []

    def add_object(object):
        self.objects.append(object)
