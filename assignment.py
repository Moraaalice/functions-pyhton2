def concatenate_args(*classes):
    answer = " "
    for c in classes:
        answer += (f"My class is{c}")
    return answer    


def concatenate_kwargs(**kwargs):
    results = (" ")
    for key,value in kwargs.items():
        results+= (f"{key,value}")
    return results    
