from app import create_app, db
from app.models import User, Story, Chapter, Prompts
# from app.blueprints.shop.models import Product

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Story': Story, 'Chapter': Chapter, 'Prompts': Prompts}