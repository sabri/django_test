from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, request
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions
import re
from django_csai.models import User, Dictionary
from django_csai.serializers import UserSerializer, GroupSerializer, DictionarySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
@api_view(['GET'])
def get_json(request):
    cotext = []
    document = """Bachelors degree in Computer Science or related field, 
    or equivalent industry experience 5+ years of experience delevering
    solutions and support to enterprise customers. 
    2+ years of experience managing and leading highly technical teams in fast-paced environrment. Demonstrated hands-on 
    experience on me or more of the Dynamics 365 products e.g. Dynamics Customer Engagement ( CRM ), Dynamics Finance & 
    Operations ( ERP ) Preferred : MBA Understanding of cloud computing technologies is diserd - Azure Core Platform ;
    Data Platform: SQL, Azure DB; Application development & debugging experience; Power BI,
    PowerApps Strong passion ad focus on delivered the right customer experience Demonstrated ability to recruit and 
    develop global teams Ability to innovate and drive change Ability to build a deep technical relationship with internal
    teams and customers Microsoft cloud Background Check: this position wil be required to pass the microsoft cloud Background check upon 
    hire/transfer and every two years thereafter. leave this section."""
    dictionaries = Dictionary.objects.all()
    for d in dictionaries:
        z = str(getattr(d, 'label'))
        x = str(getattr(d, 'word'))
        prog = re.compile(x)
        result = prog.match(document)
        cotext.append({'start': result.start(), 'end': result.end(), 'text': result.group(0), 'label': z})
    return Response({'text': document, 'Annotations': cotext})
