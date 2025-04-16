def assign(activist, workshop, network, assignments, total_workshops):
    for partner in network[activist]:
        if partner in assignments and assignments[partner] == workshop:
            return False
    return True

def assign_workshop(activists, network, assignments, total_workshops, index):
    if index == len(activists):
        return True
    activist = activists[index]
    for workshop in range(1, total_workshops + 1):
        if assign(activist, workshop, network, assignments, total_workshops):
            assignments[activist] = workshop
            if assign_workshop(activists, network, assignments, total_workshops, index + 1):
                return True
            del assignments[activist]
    return False

def schedule_workshops(total_workshops, network):
    activists = list(network.keys())
    assignments = {}
    if assign_workshop(activists, network, assignments, total_workshops, 0):
        return assignments
    else:
        return {}

total_workshops = int(input())
network = eval(input())

result = schedule_workshops(total_workshops, network)
print(result)
