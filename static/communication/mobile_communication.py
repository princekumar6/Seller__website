from background_task import background


@background(queue='mobile')
def send(*args,**kwargs):
    print(args,kwargs)
