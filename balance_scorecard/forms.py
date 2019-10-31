from .models import Indicador, Info_kpi, Acumulado_kpi, Incidentes, Compromisos, Reunion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django import forms
import datetime

class IndicadorForm(BSModalForm):
    class Meta:
        model = Indicador
        fields =['nombre_kpi','unidad_medida','categoria','meta_kpi','descripcion_kpi']
        labels = {
            'nombre_kpi': 'Nombre del Indicador',
            'unidad_medida':'Unidad de medicion',
            'meta_kpi': 'Meta del Indicador',
            'descripcion_kpi': 'Descripcion Indicador',
        }
        widgets = {
            'descripcion_kpi':forms.Textarea(),
        }


#class IndicadorForm2(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    #class Meta:
        #model= Indicador
        #fields = ['nombre_kpi','meta_kpi','descripcion_kpi']
    #def save(self, commit=False):
        #if not self.request.is_ajax():
            #instance = super(CreateUpdateAjaxMixin, self).save(commit=commit)
            #instance.responsable = User.objects.get(id=self.request.user.pk)
            #instance.save()
        #else:
            #instance = super(CreateUpdateAjaxMixin,self).save(commit=False)
        #return instance
    #def __init__(self, *args, **kwargs):
        #self.responsable = kwargs['initial']['responsable']
        #super(IndicadorForm, self).__init__(*args, **kwargs)

    #def save(self, commit=True):
        #obj = super(IndicadorForm, self).save(False)
        #obj.responsable = self.responsable
        #commit and obj.save()
        #return obj

class InformacionForm(BSModalForm):
    class Meta:
        model = Info_kpi
        fields = [
            'valor_kpi',
            'observacion',
            
        ]
        labels = {
            'indicador':'Seleccione Indicador',
            'valor_kpi':'Valor del Indicador',
            'observacion':'Observaciones',

        }
        widgets ={
            'observacion': forms.Textarea()
        }


class InformacionActualizarForm(BSModalForm):
    class Meta:
        model = Info_kpi
        fields = [
            'valor_kpi',
            'observacion',
            'indicador',
            
        ]
        labels = {
            'valor_kpi':'Valor del Indicador',
            'observacion':'Observaciones',
            'indicador':'Codigo Indicador',
        }
        widgets ={
            'valor_kpi': forms.NumberInput(),
            'observacion': forms.Textarea()
        }


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AcumuladoForm(forms.ModelForm):
    class Meta:
        model = Acumulado_kpi
        fields = ['acumulado','indicador']


class IncidentesForm(BSModalForm, forms.ModelForm):
    #titulo_incidente= forms.TextInput()
    #causa_incidente = forms.Textarea()
    #indicadores_afectados= forms.ModelMultipleChoiceField(
     #   queryset=Indicador.objects.all().order_by(), 
      #  widget=forms.CheckboxSelectMultiple(attrs={'class':'form-class'}), 
       # required=False)

    class Meta:
        model = Incidentes
        fields = ['titulo_incidente','causa_incidente','indicadores_afectados']
        

        
class CompromisosForm(BSModalForm):
    class Meta:
        model = Compromisos
        fields= ['correcion_incidente','fecha_plazo','estado_compromiso','responsable','id_incidente']
        labels = {
            'correcion_incidente':'Accion correctiva',
            'fecha_plazo':'Fecha plazo',
            'estado_compromiso':'Estado del compromiso',
            'responsable':'Responsable',
            'id_incidente':'Incidente asociado',

        }
        widgets ={
            'fecha_plazo': forms.SelectDateWidget()
        }


class ReunionForm(BSModalForm):
    class Meta:
        model = Reunion
        fields = ['fecha_reunion','participantes']
        widgets ={
            'fecha_reunion': forms.SelectDateWidget()
        }
        
