from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(
    "mongodb+srv://youtubepy:youtubepy123@cluster0.navybko.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
# Not a better way to keep id and password in code file. Above db is now deleted

db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    """Add a new video to the collection."""
    try:
        video_collection.insert_one({"name": name, "time": time})
        print("✅ Video added successfully!")
    except Exception as e:
        print("❌ Error adding video:", e)

def list_videos():
    """List all videos."""
    print("\n🎥 All Videos:")
    try:
        videos = list(video_collection.find())
        if not videos:
            print("⚠️ No videos found.")
            return
        for video in videos:
            print(f"ID: {video['_id']} | Name: {video['name']} | Time: {video['time']}")
    except Exception as e:
        print("❌ Error listing videos:", e)

def update_video(video_id, new_name, new_time):
    """Update video details by ID."""
    try:
        result = video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": {"name": new_name, "time": new_time}}
        )
        if result.modified_count:
            print("✅ Video updated successfully!")
        else:
            print("⚠️ No video found with that ID.")
    except Exception as e:
        print("❌ Error updating video:", e)

def delete_video(video_id):
    """Delete a video by ID."""
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("✅ Video deleted successfully!")
        else:
            print("⚠️ No video found with that ID.")
    except Exception as e:
        print("❌ Error deleting video:", e)

def main():
    """Main CLI menu."""
    while True:
        print("\n📺 YouTube Manager App")
        print("1️⃣  List all videos")
        print("2️⃣  Add a new video")
        print("3️⃣  Update a video")
        print("4️⃣  Delete a video")
        print("5️⃣  Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            new_name = input("Enter the updated video name: ")
            new_time = input("Enter the updated video time: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("👋 Exiting app. Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    try:
        # ✅ Test connection first
        client.admin.command('ping')
        print("✅ Connected to MongoDB successfully!")
        main()
    except Exception as e:
        print("❌ Failed to connect to MongoDB:", e)
