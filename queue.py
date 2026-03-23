queue = []

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        queue.append(item)
        print("Enqueued:", item)

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Dequeued:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", queue[0])

    elif choice == 4:
        print("Queue:", queue)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice")