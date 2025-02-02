from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

ISO8601 = '%Y-%m-%dT%H:%M:%SZ'

@app.get('/')
def show_info():
    """ Return some basic """
    return {'email': 'joseph4hacking@gmail.com',
            'current_datetime': datetime.utcnow().strftime(ISO8601),
            'github_url': 'https://github.com/jossyboy2580/hng-be-stage0.git'
    }
