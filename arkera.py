import unittest
import copy


def increment_dictionary_values(d, i):
    x = copy.deepcopy(d)
    for k, v in x.items():
        x[k] = v + i
    return x


class TestIncrementDictionaryValues (unittest.TestCase):
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)


####################################################################################################


class TestLoss(unittest.TestCase):
    def check_loss(self):
        pricesLst = [1, 12341, 62456, 25256, 26526, 265265, 25462]
        self.assertLessEqual(pricesLst[2], pricesLst[1])


####################################################################################################

def read(table, **kwargs):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s " % table)
    if kwargs:
        sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)


def upsert(table, **kwargs):
    """ update/insert rows into objects table (update if the row already exists)
        given the key-value pairs in kwargs """
    keys = ["%s" % k for k in kwargs]
    values = ["'%s'" % v for v in kwargs.values()]
    sql = list()
    sql.append("INSERT INTO %s (" % table)
    sql.append(", ".join(keys))
    sql.append(") VALUES (")
    sql.append(", ".join(values))
    sql.append(") ON DUPLICATE KEY UPDATE ")
    sql.append(", ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)


def delete(table, **kwargs):
    """ deletes rows from table where **kwargs match """
    sql = list()
    sql.append("DELETE FROM %s " % table)
    sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)


# >>> upsert("tbl", LogID=500, LoggedValue=5)
# "INSERT INTO tbl (LogID, LoggedValue) VALUES ('500', '5') ON DUPLICATE KEY UPDATE LogID = '500', LoggedValue = '5';"

# >>> read("tbl", **{"username": "morten"})
# "SELECT * FROM tbl WHERE username = 'morten';"

# >>> read("tbl", **{"user_type": 1, "user_group": "admin"})
# "SELECT * FROM tbl WHERE user_type = '1' AND user_group = 'admin';"