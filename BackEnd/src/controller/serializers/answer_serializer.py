from src.model.answer_user import Answer_User
from src.model.user import User
from src.model.type_skill import Type_Skill
from src.model.question import Question

class Answer_Serializer:
    def serial(self, answer):
        user = User.query.filter_by(id=answer.fk_id_user).first()
        question = Question.query.filter_by(id=answer.fk_id_question).first()
        type_skill = Type_Skill.query.filter_by(id=question.fk_id_type_skill).first()

        data = {
            "user": {
                "id_user": user.id,
                "name": user.name,
            },
            "question": {
                "id_question": question.id,
                "question": question.question
            },
            "type_skill": type_skill.type_skill,
            "answer": answer.answer,
            "created_at": answer.created_at
        }

        return data

    def serializerAll(self):
        data = []
        answers = Answer_User.query.all()

        for answer in answers:
            data.append(self.serial(answer))
        
        return data

    def serializerByUser(self, id_user):
        data = []
        answers = Answer_User.query.filter_by(fk_id_user=id_user).all()

        for answer in answers:
            data.append(self.serial(answer))

        return data
            
            
        