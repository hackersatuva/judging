import json

from django.shortcuts import render

from .api.user import *
from .api.organization import *
from .api.event import *
from .api.team import *
from .api.category import *
from .api.criteria import *
from .api.criteria_label import *
from .api.demo import *
from .api.demo_score import *
from . import testpage


def test_page(request):
    return render(request, 'micro/api.html', testpage.context)
