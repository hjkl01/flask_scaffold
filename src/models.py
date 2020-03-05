from uuid import uuid4
from datetime import datetime

from app import db


class Project(db.Model):
    __tablename__ = 'project_project'

    id = db.Column(db.String, primary_key=True)
    project_number = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String(10), nullable=False, default="进行中")
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    end_time = db.Column(db.DateTime)
    messages = db.Column(db.Text)
    delete = db.Column(db.Boolean, nullable=False, default=False)

    created = db.Column(db.DateTime,
                        nullable=False,
                        server_default=db.func.current_timestamp())

    __mapper_args__ = {"order_by": created.desc()}

    def __repr__(self):
        return self.project_number

    def save(self, _dict):
        p = Project(
            id=str(uuid4()),
            project_number=_dict.get('project_number'),
            status=_dict.get('status'),
            start_time=_dict.get('start_time'),
            end_time=_dict.get('end_time'),
            messages=_dict.get('messages'),
        )
        db.session.add(p)
        db.session.commit()
        print('project save success %s' % _dict.get('project_number'))

    def to_json(self):
        result = {
            "id": self.id,
            "project_number": self.project_number,
            "status": self.status,
            "start_time": self.start_time.strftime('%Y-%m-%d'),
            "end_time": self.end_time.strftime('%Y-%m-%d'),
            "messages": self.messages,
        }
        return result

