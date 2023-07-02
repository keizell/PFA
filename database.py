from sqlalchemy import create_engine ,text

db_connection_string = "mysql+pymysql://vsgd9abvd0kzuxq27tbq:pscale_pw_OnHi1S2vRRLWPswijVNPRnaCpa1Tw9Keoa1qEbwORHW@aws.connect.psdb.cloud/catravel?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)


