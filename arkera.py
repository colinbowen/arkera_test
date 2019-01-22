import unittest
import copy
import random


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

pricesLst = random.sample(range(1, 10000), 1000)

class TestLoss(unittest.TestCase):
    def check_loss(self):
        self.assertLessEqual(pricesLst[2], pricesLst[1])


####################################################################################################


def date(table, date1, date2):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s" % table)
    if date1 and date2:
        sql.append("WHERE date BETWEEN " + date1 + " AND " + date2)
    elif date1:
        sql.append("WHERE date BETWEEN " + date1 + " < CURRENT_DATE()")
    elif date2:
        sql.append("WHERE date BETWEEN " + "01/01/2001 " + date2)
    sql.append(";")
    return "".join(sql)


def id(table, id_number1, id_number2):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s" % table)
    if operator.equals("/"):
        sql.append("WHERE ID BETWEEN " + id_number1 + " AND " + id_number2)
    elif operator.equals(">"):
        sql.append("WHERE ID > " + id_number1)
    elif operator.equals("<"):
        sql.append("WHERE ID < " + id_number2)
    elif operator.equals("IN"):
        sql.append("WHERE ID < " + id_number2)
    elif operator.equals("NOTIN"):
        sql.append("WHERE ID IN " + id_number2)
    sql.append(";")


def url(table, urlLink):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s " % table)
    if urlLink:
        sql.append("WHERE URL = " + urlLink )
    sql.append(";")
    return "".join(sql)

def rating(table, rating1, rating2, operator):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s" % table)
    if operator.equals( "/"):
        sql.append("WHERE RATING BETWEEN " + rating1 + " AND " + rating2)
    elif operator.equals( ">"):
        sql.append("WHERE RATING > " + rating1)
    elif operator.equals( "<"):
        sql.append("WHERE RATING < "  + rating2)
    sql.append(";")
