import requests
from .models import Unit, Thread, Task


def check_units():
    def fix_tasks_for_dropped_unit(unit):
        threads = Thread.objects.filter(unit=unit)
        for thread in threads:
            if thread.task != None:
                task = thread.task
                task.status = 0
                task.save()
            thread.delete()

    print('=======================================\nCHECK UNITS\n=======================================')
    units = Unit.objects.all()

    for unit in units:
        try:
            requests.get(f'http://{unit.ip}:{unit.port}/isavailable')
        except:
            fix_tasks_for_dropped_unit(unit)
            unit.delete()



def give_tasks():
    def get_idle_threads():
        return Thread.objects.filter(task=None)

    def send_task(unit, task):
        return requests.post(f'http://{unit.ip}:{unit.port}/task/add', json={'id':task.id, 'input':task.input})

    def get_task_from_queue():
        tasks = Task.objects.filter(status=0)
        if len(tasks) == 0:
            return None
        else:
            return tasks[0]

    try:
        print('GIVE TASKS')
        print('GET IDLE THREADS')
        threads = get_idle_threads()
        for thread in threads:
            print('GET TASK FROM QUEUE')
            task = get_task_from_queue()
            if task != None:
                print('TASK!!!!!!!!!!')
                if send_task(thread.unit, task).status_code == 200:
                    print('TASK ADDED')
                    task.status = 1
                    task.save()
                    thread.task = task
                    thread.save()
    except:
        check_units()

def complete_task(completed_task):
    def get_thread_by_task(task):
        return Thread.objects.get(task=task)

    def release_thread(thread):
        thread.task = None
        thread.save()

    task = Task.objects.get(id=completed_task.id)
    task.status = 2
    task.output = float(completed_task.output)
    task.save()
    release_thread(get_thread_by_task(task))
    give_tasks()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
