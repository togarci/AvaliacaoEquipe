from src.model.answer_user import Answer_User
from src.model.user import User
from src.model.skill import Skill
from src.model.answer import Answer

class Answer_Serializer:
    def serial(self, answer):
        user_owner = User.query.filter_by(id=answer.id_user_owner).first()
        user_answer = User.query.filter_by(id=answer.id_user_answer).first()
        answerDescription = Answer.query.filter_by(id=answer.id_answer).first()
        skill = Skill.query.filter_by(id=answerDescription.id_skill).first()

        data = {
            "user_owner": {
                "id_user": user_owner.id,
                "name": user_owner.name,
            },
            "user_answer": {
                "id_user": user_answer.id,
                "name": user_answer.name,
            },
            "skill": skill.name,
            "answer": answerDescription.description,
            "created_at": answer.created_at
        }

        return data

    def serializerAllBySprint(self, fk_id_sprint):
        data = []
        answers = Answer_User.query.filter_by(id_sprint=fk_id_sprint).all()

        for answer in answers:
            data.append(self.serial(answer))
        
        return data

    def serializerByUser(self, id_user):
        data = []
        answers = Answer_User.query.filter_by(id_user_answer=id_user).all()

        for answer in answers:
            data.append(self.serial(answer))

        return data
            
            
        