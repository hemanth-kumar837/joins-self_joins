from django.shortcuts import render
from django.db.models import Q,F
# Create your views here.
from app.models import *


def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal=800)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__gt=300)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gte=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=3000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lte=3000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__range=[2000,5000])
    EMPOBJECTS=Emp.objects.select_related('deptno').all()

    d={"EMPOBJECTS":EMPOBJECTS}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    MGREMPOBJECTS=Emp.objects.select_related('mgr').all()
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(sal=800)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(comm__gt=300)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(sal__lt=3000)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(sal__lte=3000)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(sal__range=[2000,5000])
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(comm=None)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(deptno=10)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(deptno=20)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(deptno=30)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(deptno=40)
    MGREMPOBJECTS=Emp.objects.select_related('mgr').filter(comm=300)
    



    d={'MGREMPOBJECTS':MGREMPOBJECTS}
    return render(request,'selfjoins.html',d)                                   


def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(emp__job='CLERK')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=F('mgr__deptno'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno=7782)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gt=F('mgr__sal'))
    emd=Emp.objects.select_related('deptno','mgr').filter(sal=800)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__gt=300)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lt=3000)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lte=3000)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__range=[2000,5000])
    emd=Emp.objects.select_related('deptno','mgr').filter(comm=None)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=10)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=30,comm=None)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='CLERK',deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2500,deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=500,__location='NEW YORK')
    
   
   

    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d) 