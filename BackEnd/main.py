from src import app, db
from src.model.answer_user import Answer_User
from src.model.answer import Answer
from src.model.skill import Skill
from src.model.sprint import Sprint
from src.model.user import User

from src.views import ViewUser, ViewSkillAnswer, ViewSprint, ViewAnswerUser

from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix

Migrate(app, db)

app.wsgi_app = ProxyFix(app.wsgi_app)
app.register_blueprint(ViewUser.bp)
app.register_blueprint(ViewSkillAnswer.bp)
app.register_blueprint(ViewSprint.bp)
app.register_blueprint(ViewAnswerUser.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)