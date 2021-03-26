from background_task import background


@background(queue='notification')
def send(*args,**kwargs):
    print(args,kwargs)
