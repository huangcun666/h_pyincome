# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
import torndb
from settings import settings
from urls import url_patterns
import ui_methods
import sys


class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, ui_methods=ui_methods,

         **settings)
        self.db = torndb.Connection(
            host=options.mysql_host,
            database=options.mysql_database,
            user=options.mysql_user,
            password=options.mysql_password,
            connect_timeout=0)
        self.db_customer = torndb.Connection(
            host=options.mysql_host,
            database=options.mysql_database_customer,
            user=options.mysql_user,
            password=options.mysql_password,
            connect_timeout=0)

        self.db_company = torndb.Connection(
            host=options.mysql_host,
            database=options.mysql_database_company,
            user=options.mysql_user,
            password=options.mysql_password,
            connect_timeout=0)

        self.db_building = torndb.Connection(
            host=options.mysql_host_building,
            database=options.mysql_database_building,
            user=options.mysql_user,
            password=options.mysql_password,connect_timeout=0)


def main(mode):
    app = TornadoBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":

    mode = sys.argv[1]
    if mode=="product":
        options.mysql_host = "127.0.0.1"
        options.port = 9000
        options.mysql_database = "db_income2"
        options.mysql_database_customer = "db_customer"
    elif mode=="dev":
        options.mysql_host = "192.168.2.169"
        # options.mysql_host = "127.0.0.1"
        options.port = 9999
        options.mysql_database = "db_income_test1"
        options.mysql_database_customer = "db_customer_test"
    elif mode=="dev1":
        options.mysql_host = "192.168.2.168"
        # options.mysql_host = "127.0.0.1"
        options.port = 9999
        options.mysql_database = "db_income2"
        options.mysql_database_customer = "db_customer"

    else:
        print "please write app.py product/dev to run"

    print "visit http://localhost:{0} database: {1} mode:{2} mysql:{3} dbname:{4}".format(
        options.port, options.mysql_database, mode, options.mysql_host,
        options.mysql_database)
    main(mode)
