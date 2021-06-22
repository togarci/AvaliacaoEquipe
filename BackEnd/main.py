from src import app, db
from src.model.answer_user import Answer_User
from src.model.question import Question
from src.model.type_skill import Type_Skill
from src.model.user import User
from src.model.user_groups import User_Groups

from src.views import ViewUser, ViewQuestion, ViewAnswerUser

from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix

Migrate(app, db)

app.wsgi_app = ProxyFix(app.wsgi_app)
app.register_blueprint(ViewUser.bp)
app.register_blueprint(ViewQuestion.bp)
app.register_blueprint(ViewAnswerUser.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)