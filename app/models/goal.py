from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal")
    
    def to_dict(self):
        tasks_list = [task.to_dict() for task in self.tasks]
        goal_dict = {
            "id": self.goal_id,
            "title": self.title,
        }

        return goal_dict