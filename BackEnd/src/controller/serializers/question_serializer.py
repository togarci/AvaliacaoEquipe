from src.model.question import Question
from src.model.type_skill import Type_Skill

class Question_Serializer:
    def serializerAll(self):
        data = []
        questions = Question.query.all()
        for question in questions:
            type_skill = Type_Skill.query.filter_by(id=question.fk_id_type_skill).first()
            
            data.append({
                "id": question.id,
                "type_skill_description": type_skill.type_skill,
                "question": question.question
            })
        
        return data


    def serializerById(self, id):
        question = Question.query.filter_by(id=id).first()
        type_skill = Type_Skill.query.filter_by(id=question.fk_id_type_skill).first()

        data = {
            "id": question.id,
            "type_skill_description": type_skill.type_skill,
            "question": question.question
        }

        return data