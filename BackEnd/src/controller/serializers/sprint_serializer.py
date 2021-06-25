from src.model.sprint import Sprint

class Sprint_serializer:
    def serializerAll(self):
        data = []
        sprints = Sprint.query.all()
        for sprint in sprints:
            data.append({
                "id": sprint.id,
                "name": sprint.name,
                "created_at": sprint.created_at,
                "start_date": sprint.start_date,
                "end_date": sprint.end_date
            })
        
        return data

    def serialzerSprintById(self, id):
        sprint = Sprint.query.filter_by(id=id).first()
        return {
            "id": sprint.id,
            "name": sprint.name,
            "created_at": sprint.created_at,
            "start_date": sprint.start_date,
            "end_date": sprint.end_date
        }