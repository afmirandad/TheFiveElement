from BusinessTradding.appFirst import appFirst
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
appFirst.config["MYSQL_DATABASE_USER"] = "root"
appFirst.config["MYSQL_DATABASE_PASSWORD"] = "usbw"
appFirst.config["MYSQL_DATABASE_DB"] = "bustrading"
appFirst.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(appFirst)