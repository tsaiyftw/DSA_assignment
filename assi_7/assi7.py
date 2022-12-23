class StudentMListNode:
    def __init__(self, data):
        self.data = data
        self.nextById = None
        self.nextByName = None


class StudentMList:
    def __init__(self):
        self.listByName = None
        self.listById = None

    def insert(self, data):
        node = StudentMListNode(data)
        self._insert_by_id(node)
        self._insert_by_name(node)

    def _insert_by_id(self, node):
        dummy = StudentMListNode({"id": -1000000})
        dummy.nextById = self.listById
        p = dummy
        id = node.data["id"]
        # insert by id in decending order
        prev = None
        while p:
            if id > p.data["id"]:
                prev = p
                p = p.nextById
            else:
                break
        prev.nextById = node
        node.nextById = p
        self.listById = dummy.nextById

    def _insert_by_name(self, node):
        dummy = StudentMListNode({"name": "ZZZZZZZZZZ"})
        dummy.nextByName = self.listByName

        p = dummy
        name = node.data["name"]
        # insert name by descending order
        prev = None
        while p:
            if name < p.data["name"]:
                prev = p
                p = p.nextByName
            else:
                break
        prev.nextByName = node
        node.nextByName = p
        self.listByName = dummy.nextByName

    def print_by(self, method):
        if method == "id":
            p = self.listById
            while p:
                print(p.data)
                p = p.nextById
        elif method == "name":
            p = self.listByName
            while p:
                print(p.data)
                p = p.nextByName


s1 = {"id": 10015, "name": "Smith John", "address": "14 East Main StSomewhereVA2330"}
s2 = {"id": 10142, "name": "Roberts Susan", "address": "231 Quarry RdNowhereTX99155"}
s3 = {"id": 10175, "name": "Smith Jane", "address": "279 Rock RdValley ViewMD11333"}
s4 = {"id": 10210, "name": "Brown Steve", "address": "653 22nd StOcean CityGA21110"}

mylist = StudentMList()
mylist.insert(s2)
mylist.insert(s3)
mylist.insert(s1)
mylist.insert(s4)
print("print by Id")
mylist.print_by("id")
print("print by Name")
mylist.print_by("name")

