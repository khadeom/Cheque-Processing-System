from django import forms
from .models import User, Cheque, ChequeDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
# from crispy_forms import Layout4
class CrispForm(forms.Form):
    cheque_image = forms.ImageField(required=True)

class VerifyForm(forms.ModelForm):
    PayeeName = forms.CharField()
    accNo= forms.CharField(label="AC/NO")
    ifsc = forms.CharField(label="IFSC")
    amount = forms.CharField(label="Amount")
    micr = forms.CharField(label="MICR")

    class Meta:
        model = ChequeDetail
        fields = ("PayeeName","accNo","ifsc","amount","micr")
    

        
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        # self.helper = FormHelper()  
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-6'
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        # self.helper.form_method = 'post'
        # self.helper.form_action = 'done'
        self.helper.form_tag = False
        




        # self.helper.add_input(Submit('submit', 'Done'))




class ChequeForm(forms.ModelForm):
    


    class Meta:
        model = Cheque
        fields = ("title", "bank","cheque_image")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_class = 'form-inline'
    #     self.helper.field_template = 'bootstrap3/layout/inline_field.html'
    #     self.helper.layout = Layout(
    #         'title',
    #         'bank',
    #         'cheque_image',
            
    #     )
        # self.helper.form_id = 'id-exampleForm'
        # self.helper.form_class = 'blueForms'
        # self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

        # self.helper.add_input(Submit('submit', 'Submit'))x









