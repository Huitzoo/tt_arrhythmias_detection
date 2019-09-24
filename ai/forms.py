from django import forms
import json
from . import models as m

class DatosMedicosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DatosMedicosForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["sexo"].label = "Sexo"

            self.fields["edad"].label = "Edad"
            self.fields["height_centimeters"].label = "Altura (cm)"
            self.fields["weight_kilograms"].label = "Peso (kg)"
            self.fields["heart_rate"].label = "LPM"
            
    class Meta:
        model = m.DatosMedicos
        fields = (
            'sexo',
            'edad',
            'height_centimeters',
            'heart_rate',
            'weight_kilograms',

        )

class GeneralForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GeneralForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields['qrs_duration_msec'].label= "Duración de QRS (ms)"
            self.fields['p_r_interval_msec'].label= "Duración de PR (ms)"
            self.fields['q_t_interval_msec'].label= "Duración de QT (ms)"
            self.fields['t_interval_msec'].label= "Duración de T (ms)"
            self.fields['p_interval_msec'].label= "Duración de P (ms)"
            self.fields['qrs_vector_angles'].label= "Vector de QRS (angulo)"
            self.fields['t_vector_angles'].label= "Vector de T (angulo)"
            self.fields['p_vector_angles'].label= "Vector de P (angulo)"
            self.fields['qrst_vector_angles'].label= "Vector de QRST (angulo)"
            self.fields['j_vector_angles'].label= "Vector de J (angulo)"
    class Meta:
        model = m.GeneralData
        fields = (
            'qrs_duration_msec',
            'p_r_interval_msec',
            'q_t_interval_msec',
            't_interval_msec',
            'p_interval_msec',
            'qrs_vector_angles',
            't_vector_angles',
            'p_vector_angles',
            'qrst_vector_angles',
            'j_vector_angles'
        )
    

class DIForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DIForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.DI
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )

class DIIForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DIIForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.DII
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class DIIIForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DIIIForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.DIII
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AVRForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AVRForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AVR
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AVFForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AVFForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AVF
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AVLForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AVLForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AVL
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AV1Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AV1Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AV1
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AV2Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AV2Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AV2
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AV3Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AV3Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AV3
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AV4Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AV4Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AV4
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )
class AV5Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AV5Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AV5
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )

class AV6Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AV6Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            self.fields["average_width_q_msec"].label = "Promedio del ancho de la onda Q en ms"
            self.fields["average_width_r_msec"].label = "Promedio del ancho de la onda R en ms"
            self.fields["average_width_s_msec"].label = "Promedio del ancho de la onda S en ms"
            self.fields["jj_amplitude_milivolts"].label = "Amplitud promedio la onda J en mV"
            self.fields["q_amplitude_milivolts"].label = "Amplitud promedio la onda Q en mV"
            self.fields["r_amplitude_milivolts"].label = "Amplitud promedio la onda R en mV"
            self.fields["s_amplitude_milivolts"].label = "Amplitud promedio la onda S en mV"
            self.fields["p_amplitude_milivolts"].label = "Amplitud promedio la onda P en mV"
            self.fields["t_amplitude_milivolts"].label = "Amplitud promedio la onda T en mV"

    class Meta:
        model = m.AV6
        fields = (
            'average_width_q_msec',
            'average_width_r_msec',
            'average_width_s_msec',
            'jj_amplitude_milivolts',
            'q_amplitude_milivolts',
            'r_amplitude_milivolts',
            's_amplitude_milivolts',
            'p_amplitude_milivolts',
            't_amplitude_milivolts'
        )

#["QRSTA v5","QRSA v5","T v5","T DI","P","S v3","Heart rate","QRS duration","Number of intrinsic deflections linear v1","R wave avr"]

class RFDataModelFirstForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RFDataModelFirstForm, self).__init__(*args, **kwargs)
        self.data_values = []
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'step':'0.01'
            }
            self.fields["QRSA_v5"].label = "QRSA derivación V5"
            self.fields["QRSTA_v5"].label = "QRSTA derivación v5"
            self.fields["T_v5"].label = "El producto de la amplitud de la onda T en la derivación v5 con 0.1mv"
            self.fields["T_DI"].label = "El producto de la amplitud de la onda T en la derivación DI con 0.1mv"
            self.fields["P"].label = "Angulo del vector en el plano frontal de la onda P"
            self.fields["S_v3"].label = "El producto de la amplitud de la onda S en la derivación v3 con 0.1mv"
            self.fields["Heart_rate"].label = "Ritmo cardíaco (lpm)"
            self.fields["QRS_duration"].label = "Promedio de la duración del segmento QRS en milisegundos"
            self.fields["Number_of_intrinsic_deflections_linear_v1"].label = "Número de deflexiones intrínsecas lineales en la derivación v1"
            self.fields["R_wave_avr"].label = "Tamaño promedio de la onda R en la derivación avr"
    
    def values(self,data):
        data = list(dict(data).values())        
        
        st = float(data[1][0])-float(data[0][0])-float(data[2][0])
        for i in range(0,3):
            del data[0]
        
        for i in range(len(data)):
            self.data_values.append(float(data[i][0]))
        
        self.data_values.append(11)
        
        #self.data_values = [float(d[0]) for k,d in form.items()]

    class Meta:
        model = m.RFDataModelFirst
        fields = '__all__'
    

class RFDataModelSecondForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RFDataModelSecondForm, self).__init__(*args, **kwargs)
        self.data_values = []
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'step':'0.01'
            }

            self.fields["Q_v3"].label = "El producto del promedio de las amplitudes de la onda Q en la derivación v3 con 0.1mv"
            self.fields["Q_DII"].label = "El producto del promedio de las amplitudes de la onda Q en la derivación DII con 0.1mv"
            self.fields["R_prima_v2"].label = "El producto del promedio de las amplitudes de la onda R' en la derivación v2 con 0.1mv"
            self.fields["R_prima_R_v1"].label = "Promedio del tamaño de las Onda R', (pico pequeño justo después de R) en v1"
            self.fields["T_v5"].label = "El producto del promedio las amplitudes de la onda T en la derivación v5 con 0.1mv"
            self.fields["T_v4"].label = "El producto del promedio las amplitudes de la onda T en la derivación v4 con 0.1mv" 
            self.fields["Heart_rate"].label = "Ritmo cardíaco (lpm)"
            self.fields["QRS_duration"].label = "Promedio de la duración del segmento QRS en milisegundos"
            self.fields["Numero_de_deflexiones_intrinsecas_en_v1"].label = "Número de deflexiones intrínsecas en v1"
        
    def values(self,data):
        data = list(dict(data).values())        
        print(data)
        for i in range(len(data)):
            self.data_values.append(float(data[i][0]))
        
        #self.data_values.append(11)
        print(self.data_values)

        self.data_values =json.dumps({
                "data":{
                    "rf":self.data_values
                }
            }
        )
        #self.data_values = [float(d[0]) for k,d in form.items()]

    class Meta:
        model = m.RFDataModelSecond
        fields = '__all__'


class FileUploadForm(forms.Form):
    ecg = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'name':'ecg',
                'class':'input-file'
            }
        )
    )