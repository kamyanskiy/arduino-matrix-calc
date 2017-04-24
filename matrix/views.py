# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    result = []
    if request.POST:
        items = request.POST.dict()
        for table in range(1, 5):
            table_result =[]
            for row in range(1, 9):
                row_str = ''
                for col in range(1,9):
                    row_str += items.get("{0}-{1}-{2}-input".format(table,
                                                                    row, col))
                table_result.append(row_str)
            result.append(table_result)
        request.POST = None
    return render(request, 'matrix/index.html', {'range': range(1, 9),
                                                 'table_numbers': range(1, 5),
                                                 'result': result})
