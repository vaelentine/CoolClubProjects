
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
import logging
from .forms import PronounForm, UploadCSVForm
from .models import Pronouns, Background, Species, Skill, CharClass, ClassAbility, Character
import csv


# index view
def index(request):
    return render(request, 'index.html', {})


def pronouns(request):

    if request.method == 'POST':
        pronouns_form = PronounForm(request.POST)
        if pronouns_form.is_valid():
            gender_name = pronouns_form.cleaned_data['gender_name']
            subject_pronoun = pronouns_form.cleaned_data['subject_pronoun']
            object_pronoun = pronouns_form.cleaned_data['object_pronoun']
            possessive_adj = pronouns_form.cleaned_data['possessive_adj']
            possessive_pronoun = pronouns_form.cleaned_data['possessive_pronoun']
            reflexive_pronoun = pronouns_form.cleaned_data['reflexive_pronoun']

            print(f'Validated! {gender_name}: {subject_pronoun}/{object_pronoun}/{possessive_adj}/{possessive_pronoun}/{reflexive_pronoun}')
            pronouns_form.save()
    pronoun_objects = Pronouns.objects.all()
    pronouns_form = PronounForm
    return render(request, 'pronouns_form.html', {'pronouns_form': pronouns_form, 'pronoun_objects': pronoun_objects})


def bulk_upload(request, model, *args):
    if request.method == 'POST':
        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split(",")
            created = model.objects.update_or_create(*args)
    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)


def pronouns_bulk_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split(",")
            created = Pronouns.objects.update_or_create(
                gender_name =fields[0],
                subject_pronoun=fields[1],
                object_pronoun=fields[2],
                possessive_adj=fields[3],
                possessive_pronoun=fields[4],
                reflexive_pronoun=fields[5],
            )

    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)


def background_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split(",")
            created = Background.objects.update_or_create(
                name=fields[0],
                header=fields[1],
                description=fields[2],
            )

    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)


def species_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split(",")
            created = Species.objects.update_or_create(
                name=fields[0],
                header=fields[1],
                description=fields[2],
            )

    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)


def char_class_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split(",")
            created = CharClass.objects.update_or_create(
                name=fields[0],
                header=fields[1],
                description=fields[2],
            )

    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)


def class_ability_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split(",")
            created = ClassAbility.objects.update_or_create(
                name=fields[0],
                header=fields[1],
                description=fields[2],
            )

    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)


def character_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split(",")
            created = Character.objects.update_or_create(
                name=fields[0],
                header=fields[1],
                description=fields[2],
            )

    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)


def skill_upload(request):
    print("post post post post")
    if request.method == 'POST':

        csv_file = request.FILES["Upload_A_Bulk_CSV"]
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")
        for i in csv_data:
            fields = i.split("\t")
            print(fields)
            created = Skill.objects.update_or_create(
                name=fields[0],
                description=fields[1],
                psychic=fields[2],
            )

    upload_csv_form = UploadCSVForm()
    data = {'upload_csv_form': upload_csv_form}
    return render(request, 'UploadCSV.html', data)

