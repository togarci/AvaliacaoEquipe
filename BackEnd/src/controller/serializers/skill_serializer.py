from src.model.skill import Skill
from src.model.answer import Answer

class Skill_serializer:
    def serializerAll(self):
        data = []
        answers = Answer.query.all()
        for answer in answers:
            skill = Skill.query.filter_by(id=answer.id_skill).first()
            data.append({
                "id": answer.id,
                "skill": skill.name,
                "description": answer.description
            })
        
        return data