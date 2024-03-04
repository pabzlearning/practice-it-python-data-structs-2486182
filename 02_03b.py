from collections import deque

DEFAULT_TASK = ["PRI005", "PRI010", "PRI0015"]
task_list = deque(DEFAULT_TASK)

class TaskList:
    
    # def __init__(self):

    def add_item(self, item, hasPriority=False):
        print("before: {}".format(task_list))
        if hasPriority:
            task_list.appendleft(item)
        else:
            task_list.append(item)

        print("after: {}".format(task_list))
    


def main():
    #add code here
    task_listing = TaskList()
    item_priority = "PRIO001"
    task_listing.add_item(item_priority, hasPriority=True)
    item_no_priority = "PRI999"
    task_listing.add_item(item_no_priority)

    return

if __name__ == "__main__":
    main()