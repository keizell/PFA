from sqlalchemy import create_engine ,text

db_connection_string = "mysql+pymysql://tb140zyw6f6kbvnqbjdz:pscale_pw_S81oBfbKMETAFLLfCDF2gOLmmaTpCALTDhnGS1NCceh@aws.connect.psdb.cloud/catravel?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)


