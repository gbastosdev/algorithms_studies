states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "mt", "id"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["az", "ca"])

final_stations = set()
while states:
    best_station = None
    covered_states = set()
    for station, stater_per_station in stations.items():
        covered = states & stater_per_station
        if len(covered) > len(covered_states):
            best_station = station
            covered_states = covered

    states -= covered_states
    final_stations.add(best_station)
    

print("Final stations to cover all states:", final_stations)