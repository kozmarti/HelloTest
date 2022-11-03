import datetime


def create_time_list(start, end):
    list_index_time = {}
    delta = datetime.timedelta(minutes=5)
    start = datetime.datetime.strptime(start, '%H:%M:%S')
    end = datetime.datetime.strptime(end, '%H:%M:%S')
    t = start
    index = 0
    while t <= end:
        list_index_time[str(datetime.datetime.strftime(t, '%H:%M:%S'))] = index
        t += delta
        index += 1
    return list_index_time


def get_item_for_hour(hour):
    time_list = create_time_list("05:00:00", "21:00:00")
    time = hour[11:19]
    return time_list[time]


def list_of_previsions(data) -> list:
    return [d["fields"]["bm_prevision"] for d in data["records"]]


def prevision_for_hour(data, hour) -> int:
    index = get_item_for_hour(hour)
    return data["records"][index]["fields"]["bm_prevision"]


def min_estimation_and_hour(data):
    previsions_list = list_of_previsions(data)
    minimum_estimation = min(previsions_list)
    minimum_times = [d["fields"]["bm_heure"] for d in data["records"] if d["fields"]["bm_prevision"] == minimum_estimation]
    return [minimum_estimation, minimum_times]


def max_estimation_and_hour(data):
    previsions_list = list_of_previsions(data)
    maximum_estimation = max(previsions_list)
    maximum_times = [d["fields"]["bm_heure"] for d in data["records"] if d["fields"]["bm_prevision"] == maximum_estimation]
    return [maximum_estimation, maximum_times]


def average_prevision_for_day(data):
    previsions_list = list_of_previsions(data)
    return sum(previsions_list)/len(previsions_list)

