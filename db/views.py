from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count

from . models import Product, Pc, Laptop

from statistics import mean 


def task_1():
    q = Product.objects.values('maker').annotate(Count('model'))
    q_count = [i.get('model__count') if 1 != i.get('model__count') else 0 for i in q]

    k = Product.objects.values('type').annotate(Count('maker'))
    k_count = [i.get('maker__count') if 1 == i.get('maker__count') else 0 for i in k]

    position = []

    for i in range(len(k_count)):
        if k_count[i] == 1:
            position.append(i)

    result = []

    for i in position:
        if q_count[i] > 1:
            result.append(q_count[i])
    
    result_maker = []

    for i in result:
        for j in q:
            if j.get('model__count') == i:
                result_maker.append(j.get('maker'))
    
    maker_type = Product.objects.values('maker', 'type')

    product = []

    for i in result_maker:
        for j in maker_type:
            if j.get('maker') == i:
                product.append([j.get('maker'), j.get('type')])
                break
    
    return product


def Task2():
    q = Product.objects.values('model', 'type')
    q_pc = [i.get('model')  for i in q if i.get('type') == 'PC']  # [1,2]

    pc_speed = Pc.objects.values('model', 'speed')  # <QuerySet [{'model': '2', 'speed': 125}, {'model': '1', 'speed': 120}]>
    laptop_speed = Laptop.objects.values('model', 'speed')  # <QuerySet [{'model': '4', 'speed': 123}, {'model': '5', 'speed': 3}, {'model': '6', 'speed': 300}]>

    result = []

    for i in laptop_speed:
        for j in pc_speed:
            if i.get('speed') < j.get('speed'):
                result.append([i.get('model'), i.get('speed'), 'laptop'])
    
    return result

def task3():

    q = Product.objects.values('model', 'type', 'maker')
    new_q = [i.get('model') for i in q if i.get('maker') == 'IBM' and i.get('type') == 'PC']  # [1,2]
    pcs = Pc.objects.values('model','speed')  # <QuerySet [{'model': '2', 'speed': 125}, {'model': '1', 'speed': 120}, {'model': '7', 'speed': 123}]>

    result_pc = []

    for i in new_q:
        for j in pcs:
            if j.get('model') == i:
                result_pc.append(j.get('speed'))
                
    return mean(result_pc)

class IndexView(ListView):
    template_name = 'db/index.html'
    context_object_name = 'task1'
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['product'] = task_1()
        context['result'] = Task2()
        context['mean'] = task3()
        return context
