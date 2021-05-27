import pysql 


user = os.getenv("username")
password = os.getenv('password')

connection = pysql.connection(
    user=user,
    password=password
)


