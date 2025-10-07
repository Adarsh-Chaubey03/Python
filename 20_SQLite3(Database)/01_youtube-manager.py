import sqlite3   # database

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor() # can communicate to database directly in form of queries

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)               
''')

def list_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE ID = ?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE ID = ?",(video_id,))
    conn.commit()

def main():
     while True:
        print("\n Youtube Manager | Choose an option ")
        print("\n1. List all youtube videos ")
        print("2. Add a youtube videos")
        print("3. Update a youtube video details")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        
        choice = input("Enter your choice: ")
        
        # prefer match - case 
        
        if choice == '1':
            list_video()
            
        elif choice == '2':
           name = input("Enter the video name: ")
           time = input("Enter the video time: ")
           add_video(name,time)
           
        elif choice == '3':
           video_id = input("Enter the video ID to update: ")
           name = input("Enter the new video name: ")
           time = input("Enter the new video time: ")
           update_video(video_id,name,time)
        
        elif choice == '4':
           video_id = input("Enter the video ID to delete: ")
           delete_video(video_id)
        elif choice == '5':
           break
        
        else:
            print("Invalid Choice!")
    
     conn.close()


if __name__=="__main__":
    main()