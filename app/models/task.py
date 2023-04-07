from datetime import datetime
from sqlalchemy.event import listen

from . import db

class Task(db.Model):
    __tablename__ = 'tareas'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=db.func.current_timestamp()) 
    #server_default=db.func.current_timestamp(),
    #updated_at = db.Column(db.DateTime, nullable=False, 
    #                       server_default=datetime.utcnow,
    #                       onupdate=datetime.utcnow)
    
    @classmethod
    def new(cls, title, description, deadline):
        return Task(title=title, description=description, deadline=deadline)
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
    
    def __str__(self):
        return self.title
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline,
            'created_at': self.created_at,
        }

def insert_tasks(*args, **kwargs):
    db.session.add(
        Task(title='Tarea 1', description='Descripción 1', 
             deadline='2023-04-10 16:28')
    )
    db.session.add(
        Task(title='Tarea 2', description='Descripción 2', 
             deadline='2023-04-12 19:10')
    )
    #db.session.commit()

listen(Task.__table__, 'after_create', insert_tasks)