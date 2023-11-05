from sqlalchemy import create_engine, text

engine = create_engine('mariadb+mariadbconnector://admin:password@127.0.0.1:3306/dbname', echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello, World"'))

    print(result.all())
