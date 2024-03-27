from .models import *
from pymongo import MongoClient
import socket
from bson.objectid import ObjectId
from bson.json_util import dumps
import time
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import django.core.serializers
import json
import requests
import xmltodict
from django.shortcuts import render, redirect

#
# what he searched for
# how many request he made to the partner API
# and the data we sent, like userIP, brand,....
# and lastly the reply from the API

@csrf_exempt
def welcome(request):
    return JsonResponse({ 'status': ':) I am alive! :)' })

@csrf_exempt
def volteCRX(request):
    ip = None
    ua = None
    brand = None
    brandsrc = None
    sid = None
    userx_id = None
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            ip = data.get('ip')
            ua = data.get('ua')
            brand = data.get('brand')
            brandsrc = data.get('brandsrc')
            sid = data.get('sid')
            userx_id = data.get('userxId')
        except e:
            return JsonResponse({'status': -1})
    else:
        return JsonResponse({'status': -1})

    if ip == None or ua == None or brand == None or brandsrc == None or sid == None:
        return JsonResponse({'status': -1})

    log = ModelUerxLog(
        url=f'http://iphosxpym7pu50.rp.lowtide.fun/api/v1/srtb?sid={sid}&ua={ua}&ip={ip}&brand={brand}&brandct=5&brandsrc={brandsrc}&to=120&li=1',
        userx_id=userx_id,
        ip=ip,
        ua=ua,
        brand=brand,
        brandsrc=brandsrc,
        to='120',
        li='1',
        sid=sid,
        created_at=datetime.now()
    )

    try:
        headers = {
            'Content-Type': f'application/json'
        }
        # response = requests.post(f'https://volte.earth/api/crx', headers=headers, json={
        #     'ip': ip, 'ua': ua, 'brand': brand
        # })
        response = requests.get(
            f'http://iphosxpym7pu50.rp.lowtide.fun/api/v1/srtb?sid={sid}&ua={ua}&ip={ip}&brand={brand}&brandct=5&brandsrc={brandsrc}&to=120&li=1')
        response_data = response.json()  # Assuming the API returns JSON data

        log.result = response_data; log.save()

        return JsonResponse({'status': True, 'data': response_data})
    except requests.exceptions.RequestException as e:
        log.result = 'Error'; log.save()

        print('Excepting error in calling the API')
        print(str(e))
        return JsonResponse({'status': -1, 'error': str(e)})


@csrf_exempt
def installedCRX(request):
    ip = None
    ua = None
    eid = None
    pid = None
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            ip = data.get('ip')
            ua = data.get('ua')
            eid = data.get('eid')
            pid = data.get('pid')
        except e:
            return JsonResponse({'status': False})
    else:
        return JsonResponse({'status': False})

    if ip == None or ua == None or eid == None or pid == None:
        return JsonResponse({'status': False})

    try:
        newModel = ModelUserx(extension_id=eid, project_id=pid, user_agent=ua,
                              ip=ip, installed_at=datetime.now(), lastseen_at=datetime.now())
        newModel.save()

        object = {'id': newModel.pk}
        return JsonResponse({'status': True, 'data': object})
    except requests.exceptions.RequestException as e:
        print('Excepting error in calling the API')
        print(str(e))
        return JsonResponse({'status': False, 'error': str(e)})


@csrf_exempt
def lastSeen(request):
    id = None
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
        except e:
            return JsonResponse({'status': False})
    else:
        return JsonResponse({'status': False})

    if id == None:
        return JsonResponse({'status': False})

    try:
        newModel = ModelUserx.objects.get(pk=id)
        newModel.lastseen_at = datetime.now()
        newModel.save()

        return JsonResponse({'status': True})
    except requests.exceptions.RequestException as e:
        print('Excepting error in calling the API')
        print(str(e))
        return JsonResponse({'status': False, 'error': str(e)})


@csrf_exempt
def uninstalledCRX(request):
    id = None
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
        except e:
            return redirect("https://volte.earth/uninstall")
    else:
        return redirect("https://volte.earth/uninstall")

    if id == None or id == 'undefined':
        return redirect("https://volte.earth/uninstall")

    try:
        newModel = ModelUserx.objects.get(pk=id)
        newModel.uninstalled_at = datetime.now()
        newModel.save()

        return redirect("https://volte.earth/uninstall")
        # return JsonResponse({'status': True})
    except Exception as e:
        print('Excepting error in calling the API')
        print(str(e))

        return redirect("https://volte.earth/uninstall")
        # return JsonResponse({'status': False, 'error': str(e)})


@csrf_exempt
def getActiveProjects(request):
    try:
        models = ModelProject.objects.filter(status=1)
        projects_list = list(models.values())
        # projects_json = serialize('json', projects_list)

        return JsonResponse({'status': True, 'data': projects_list})
    except requests.exceptions.RequestException as e:
        print('Excepting error in calling the API')
        print((e))

        return JsonResponse({'status': False, 'error': (e)})


@csrf_exempt
def selectProject(request):
    id = None
    project = None
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            project = request.GET.get('project')
        except e:
            return JsonResponse({'status': False})
    else:
        return JsonResponse({'status': False})

    if id == None or project == None:
        return JsonResponse({'status': False})

    try:
        newModel = ModelUserx.objects.get(pk=id)
        newModel.project_id = project
        newModel.uninstalled_at = datetime.now()
        newModel.save()

        return JsonResponse({'status': True})
    except requests.exceptions.RequestException as e:
        print('Excepting error in calling the API')
        print(str(e))

        return JsonResponse({'status': False, 'error': str(e)})
