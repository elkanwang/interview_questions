class Database:
    def __init__(self):
        self.db = {}
        self.index = {}
    def get(self, key):
        return self.db[key]

    def remove(self, key):
        if key in self.db:
            value = self.db[key]
            for indexName, columnValue in value.iteritems():
                if indexName in self.index and columnValue in self.index[indexName]:
                    self.index[indexName][columnValue].remove(key)
            del self.db[key]

    def put(self, key, value):
        self.remove(key)
        self.db[key] = value
        for indexName, columnValue in value.iteritems():
            if indexName in self.index:
                if columnValue in self.index[indexName]:
                    self.index[indexName][columnValue].append(key)
                else:
                    self.index[indexName][columnValue] = [key]

    def create_index(self, indexName):
        tmpIndex = {}
        for k, v in self.db.iteritems():
            columnValue = v[indexName]
            if columnValue in tmpIndex:
                tmpIndex[columnValue].append(k)
            else:
                tmpIndex[columnValue] = [k]
        self.index[indexName] = tmpIndex

    def fetch_by_index(self, indexName, columnValue):
        if indexName in self.index and columnValue in self.index[indexName]:
            return self.index[indexName][columnValue]
        else:
            return []

d = Database()
d.put("1", {"user":"john", "age":13})
d.put("2", {"user":"park", "age":13})
print d.get("1")

d.create_index("user")
print d.fetch_by_index("user","john")
d.remove("1")
print d.fetch_by_index("user", "john")
d.put("2", {"user":"john", "age":13})
print d.fetch_by_index("user", "john")
print d.fetch_by_index("user", "park")
