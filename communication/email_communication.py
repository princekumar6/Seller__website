from background_task import background


@background(queue='email',schedule=1)
def send(*args,**kwargs):
    print(args,kwargs)
