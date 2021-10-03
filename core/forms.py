from django import forms
from .models import Course, Assignment,AssignmentResult, AssignmentSubmission
from django.utils.decorators import method_decorator

# FORM FOR CREATE A COURSE
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_image', 'teacher_name', 'teacher_details', 'course_description', 'end_date']

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].label = "Course Name"
        self.fields['course_image'].label = "Image"
        self.fields['teacher_name'].label = "Teacher Name"
        self.fields['teacher_details'].label = "Teacher Details"
        self.fields['course_description'].label = "Description"
        self.fields['end_date'].label = "End Date"

        self.fields['course_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Course Name',
            }
        )

        self.fields['course_image'].widget.attrs.update(
            {
                'placeholder': 'Image',
            }
        )

        self.fields['teacher_name'].widget.attrs.update(
            {
                'placeholder': 'Teacher Name',
            }
        )

        self.fields['teacher_details'].widget.attrs.update(
            {
                'placeholder': 'Teacher Details',
            }
        )

        self.fields['course_description'].widget.attrs.update(
            {
                'placeholder': 'Description',
            }
        )

    def is_valid(self):
        valid = super(CourseCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(CourseCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course


# ASSIGNMENT CREATE FORM
class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'content', 'marks', 'duration']

    def __init__(self, *args, **kwargs):
        super(AssignmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Assignment Name"
        self.fields['content'].label = "Content"
        self.fields['marks'].label = "Marks"
        self.fields['duration'].label = "Duration"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Enter A Name',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Content',
            }
        )

        self.fields['marks'].widget.attrs.update(
            {
                'placeholder': 'Enter Marks',
            }
        )

        self.fields['duration'].widget.attrs.update(
            {
                'placeholder': '3 hour, 2 hour etc ...',
            }
        )

    def is_valid(self):
        valid = super(AssignmentCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        assignment = super(AssignmentCreateForm, self).save(commit=False)
        if commit:
            assignment.save()
        return assignment


# # EXAM CREATE FORM
# class ExamCreateForm(forms.ModelForm):
#     class Meta:
#         model = Exam
#         fields = ['title', 'content', 'marks', 'duration']

#     def __init__(self, *args, **kwargs):
#         super(ExamCreateForm, self).__init__(*args, **kwargs)
#         self.fields['title'].label = "Assignment Name"
#         self.fields['content'].label = "Content"
#         self.fields['marks'].label = "Marks"
#         self.fields['duration'].label = "Duration"

#         self.fields['title'].widget.attrs.update(
#             {
#                 'placeholder': 'Enter A Name',
#             }
#         )

#         self.fields['content'].widget.attrs.update(
#             {
#                 'placeholder': 'Content',
#             }
#         )

#         self.fields['marks'].widget.attrs.update(
#             {
#                 'placeholder': 'Enter Marks',
#             }
#         )

#         self.fields['duration'].widget.attrs.update(
#             {
#                 'placeholder': '3 hour, 2 hour etc ...',
#             }
#         )

#     def is_valid(self):
#         valid = super(ExamCreateForm, self).is_valid()

#         # if already valid, then return True
#         if valid:
#             return valid
#         return valid

#     def save(self, commit=True):
#         course = super(ExamCreateForm, self).save(commit=False)
#         if commit:
#             course.save()
#         return course

#Assignment marks

# ASSIGNMENT SUBMISSION FORM

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['name', 'university_id', 'file']

    def __init__(self, *args, **kwargs):
        super(AssignmentSubmissionForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].label = " Name"
        self.fields['university_id'].label = "University Id"
        # self.fields['content'].label = "Answer"
        self.fields['file'].label = "Or Upload File" 

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['university_id'].widget.attrs.update(
            {
                'placeholder': 'Write Your Id',
            }
        )

       
        self.fields['file'].widget.attrs.update(
            {
                'placeholder': 'Upload Your FILE Here', 
            }
        )

    def is_valid(self):
        valid = super(AssignmentSubmissionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentSubmissionForm, self).save(commit=False)
        if commit:
            # AssignmentSubmission.save(self,commit=False)
            course.save()
        return course

# class AssignmentResultForm(forms.ModelForm):
#     class Meta:
#         model = AssignmentResult
#         fields = ['marks','comments']
#         marks = forms.IntegerField( required=False)
        # comments = forms.CharField(max_length=50, required=False)

    # def clean_reg_no(self): # Validates the Student reg Field
    #     reg_no = self.cleaned_data.get('reg_no')
    #     if (reg_no == 0):
    #         raise forms.ValidationError("Reg No can't be 0")
    #     for instance in Student.objects.all():
    #         if instance.reg_no == reg_no:
    #             print('already added',reg_no)
    #             raise forms.ValidationError(str(reg_no) + ' is already added')
    #     return reg_no 

class AssignmentResultForm(forms.ModelForm):
    class Meta:
        model = AssignmentResult
        fields = ['marks','comments','file']

    def __init__(self, *args, **kwargs):
        super(AssignmentResultForm, self).__init__(*args, **kwargs)
        self.fields['marks'].label = " Marks"

        self.fields['marks'].widget.attrs.update(
            {
                'placeholder': 'marks',
            }
        )
        self.fields['file'].widget.attrs.update(
            {
                'placeholder': 'Upload Report',
            }
        )
    def is_valid(self):
        valid = super(AssignmentResultForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentResultForm, self).save(commit=False)
        if commit:
            course.save()
        return course
# EXAM SUBMISSION FORM
# class ExamSubmissionForm(forms.ModelForm):
#     class Meta:
#         model = ExamSubmission
#         fields = ['name', 'university_id', 'content', 'file']

#     def __init__(self, *args, **kwargs):
#         super(ExamSubmissionForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = " Name"
#         self.fields['university_id'].label = "University Id"
#         self.fields['content'].label = "Answer"
#         self.fields['file'].label = "Or Upload File"

#         self.fields['name'].widget.attrs.update(
#             {
#                 'placeholder': 'Write Your Name',
#             }
#         )

#         self.fields['university_id'].widget.attrs.update(
#             {
#                 'placeholder': 'Write Your Id',
#             }
#         )

#         self.fields['content'].widget.attrs.update(
#             {
#                 'placeholder': 'Write Your Answer Here',
#             }
#         )

#         self.fields['file'].widget.attrs.update(
#             {
#                 'placeholder': 'Upload Your FILE Here',
#             }
#         )

#     def is_valid(self):
#         valid = super(ExamSubmissionForm, self).is_valid()

#         # if already valid, then return True
#         if valid:
#             return valid
#         return valid

#     def save(self, commit=True):
#         course = super(ExamSubmissionForm, self).save(commit=False)
#         if commit:
#             course.save()
#         return course
