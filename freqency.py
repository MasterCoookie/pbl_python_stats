from datetime import datetime
def calculate_mean_time_period(filename:str)->float:
    with open(f"logi/{filename}",'r') as f:
        lines=f.readlines()
    previous=datetime.strptime(lines[0][0:12],"%H:%M:%S:%f")
    all_periods:float=0
    number_of_periods:int=0
    for i in range(1,len(lines)):
        if len(lines[i])!=78:
            continue
        current = datetime.strptime(lines[i][0:12],"%H:%M:%S:%f")
        if len(lines[i-1])==78:
            all_periods+=float((current-previous).microseconds)
            number_of_periods+=1
        previous=current
    in_micro= all_periods/number_of_periods
    in_seconds=in_micro/1000000
    
    return 1/in_seconds
print(calculate_mean_time_period("test.txt"),"Hz")
        
        