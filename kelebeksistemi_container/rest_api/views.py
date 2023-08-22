from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions
from program.models import LicenseKey
from django.shortcuts import render
import json, datetime, uuid


# Create your views here.
def test_view(request):
    return render(request, "rest_api/test.html")


class ValidateView(APIView):
    def get(self, request, dsn, key, *args, **kwargs):
        try:
            licence_key = LicenseKey.objects.get(key=key)
            dsn1 = licence_key.disk_serial_number1.__str__()
            dsn2 = licence_key.disk_serial_number2.__str__()
            dsn_message = "CORRECT DSN"
            is_dsn_registered = False
            
            now = datetime.datetime.now()
            year, month, day = [int(i) for i in str(licence_key.end_date).split("-")]
            end_date = datetime.datetime(year, month, day)
            
            if end_date > now:
                licence_type = licence_key.key_type
                # Standart ve UUID kaydi olmayan
                if licence_type == "STD" and dsn1 == "None":
                    print(0)
                    licence_key.disk_serial_number1 = dsn
                    uuid_message = "REGISTERED DSN1"
                    is_dsn_registered = True
                        
                    # Standart ve UUID kaydı eşleşmeyen
                elif licence_type == "STD" and not (dsn == dsn1):
                    data = {"Status-Code": 901,
                            "Key-Message": "",
                            "End-Date": "",
                            "Is-DSN-Registered": is_dsn_registered,
                            "DSN-Message": "WRONG DSN",
                            "Error-Message": ""
                            }
                    return JsonResponse(data=data, status=status.HTTP_200_OK)

                # Pro ve UUID1 kaydi olmayan
                elif licence_type == "PRO" and dsn1 == "None":
                    licence_key.disk_serial_number1 = dsn
                    uuid_message = "REGISTERED DSN1"
                    is_dsn_registered = True
                    
                # Pro ve UUID2 kaydi olmayan
                elif licence_type == "PRO" and dsn2 == "None":
                    licence_key.disk_serial_number2 = dsn
                    uuid_message = "REGISTERED DSN2"
                    is_dsn_registered = True

                # Pro ve UUID kaydi eşleşmeyen
                elif licence_type == "PRO" and not ((dsn == dsn1) or (dsn == dsn2)):
                    data = {"Status-Code": 901, 
                            "Key-Message": "", 
                            "End-Date": "",
                            "Is-DSN-Registered": is_dsn_registered, 
                            "DSN-Message": "WRONG DSN",
                            "Error-Message": ""
                            }
                    return JsonResponse(data=data, status=status.HTTP_200_OK)

                data = {"Status-Code": 900, 
                        "Key-Message": "VERIFIED",
                        "End-Date": licence_key.end_date.strftime("%Y-%m-%d"),
                        "Is-DSN-Registered": is_dsn_registered,
                        "DSN-Message": dsn_message,
                        "Error-Message": ""
                        }
                licence_key.save()
                return JsonResponse(data=data, status=status.HTTP_200_OK)
            
            else:
                data = {"Status-Code": 910, 
                        "Key-Message": "EXPIRED", 
                        "End-Date": "",
                        "Is-DSN-Registered": False, 
                        "DSN-Message": "",
                        "Error-Message": ""
                        }
                return JsonResponse(data=data, status=status.HTTP_200_OK)
            
        except Exception as e:
            data = {"Status-Code": 904, 
                    "Key-Message": "", 
                    "End-Date": "",
                    "Is-DSN-Registered": False, 
                    "DSN-Message": "", 
                    "Error-Message": str(e)
                    }
            return JsonResponse(data=data, status=status.HTTP_200_OK)
        