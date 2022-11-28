from marshmallow import Schema


class StudentSchema(Schema):
    class Meta:
        fields = ('StudentId', 'Firstname', 'Surname', 'GroupId')


class MarkSchema(Schema):
    class Meta:
        fields = ('MarkId', 'StudentId', 'SubjectId', 'TeacherId', 'Date', 'Value')


class TeacherSchema(Schema):
    class Meta:
        fields = ('TeacherId', 'Firstname', 'Surname', 'SubjectId')


teachers_schema = TeacherSchema(many=True)
marks_schema = MarkSchema(many=True)
