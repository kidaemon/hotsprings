from flask_frozen import Freezer
from app import app, Hotspring

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def hotspring():
    for hotspring in Hotspring.query.all():
        yield { 'ZIP': hotspring.ZIP }

if __name__ == '__main__':
    freezer.freeze()