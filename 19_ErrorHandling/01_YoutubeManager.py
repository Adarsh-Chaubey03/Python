import json







def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    # finally:
    #     pass


def list_all_videos(videos):
    pass


def  add_videos(videos):
    pass


def list_all_videos(videos):
    pass


def update_videos(videos):
    pass


def delete_videos(videos):
    pass

def main():
    videos=load_data()

    while True:
        print("\n Youtube Manager | Choose an option ")
        print("\n 1. List all youtube videos ")
        print("3. Update a youtube video details")
        print("3. Add a youtube videos")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)  
            case '3':
                update_videos(videos)  
            case '4':
                delete_videos(videos)  
            case '5':
                break
            case _:
                print("Invalid Choice")
                

if __name__ == "__main__":
    main() 