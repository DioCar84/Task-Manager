from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # limits number of chars to 25, does not allow for same name twice or blank value
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    #establishes link between this table and Task
    #will delete any task linked to a category that is deleted
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    # limits number of chars to 50, does not allow for same name twice or blank value
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # if time is needed, use db.Datetime or db.Time
    due_date = db.Column(db.Date, nullable=False)
    # links this to the Category table using the id field 
    # ondelete deletes any tasks associated with the deleted category
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )