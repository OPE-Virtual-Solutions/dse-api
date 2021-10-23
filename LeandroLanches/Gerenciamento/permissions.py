from .models import *
from rest_framework import permissions


class GrupoAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        queryset = AuthUserGroups.objects.all()
        r = request.data
        print("olhaaa",r)
        #print(dir(request))
        if request.method == "POST":
            if request.user.id in AuthUserGroups.objects.get(request.user.id):
                print("está aqui")
                return True
            print("ta aqui não")    
            return False
        return True